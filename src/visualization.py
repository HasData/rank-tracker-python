import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import xlsxwriter


def make_graph(target_domain: str, domain_data: dict):
    image_width = 1920
    image_height = 1080
    dpi = 100

    plt.figure(figsize=(image_width / dpi, image_height / dpi), dpi=dpi)

    for query, rank_data in domain_data[target_domain].items():
        x_axis = [datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S") for x in rank_data]
        y_axis = [x[1] for x in rank_data]

        plt.plot(x_axis, y_axis, label=f"Query: {query}")

    plt.axhline(y=1, linestyle="--", label="Rank 1")
    plt.xlabel("Timeline")
    plt.ylabel("SEO Rank")
    plt.title(f"SEO Rank Changes for {target_domain}")
    plt.legend()
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gcf().autofmt_xdate()
    ax.invert_yaxis()
    plt.tight_layout()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'output', f'{target_domain}.png')
    plt.savefig(file_path, dpi=dpi, bbox_inches="tight")
    plt.close()


def make_excel_report(target_domain, domain_data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.join(script_dir, '..', 'output', f'{target_domain}.xlsx')

    workbook = xlsxwriter.Workbook(output_filename)
    worksheet = workbook.add_worksheet()

    COLOR_DARK = '#B4C6E7'
    COLOR_LIGHT = '#D9E1F2'

    title_format = workbook.add_format({
        'font_size': 16,
        'align': 'center',
        'valign': 'vcenter'
    })

    def get_header_format(bg_color, bold=False):
        return workbook.add_format({
            'bg_color': bg_color,
            'align': 'center',  # Headers are centered
            'valign': 'vcenter',
            'border': 1,  # Add border to all sides
            'bold': bold
        })

    def get_data_format(bg_color):
        return workbook.add_format({
            'bg_color': bg_color,
            'align': 'right',  # Data values are right-aligned
            'valign': 'vcenter',
            'border': 1
        })

    border_only = workbook.add_format({'border': 1})
    datetime_format = get_data_format(COLOR_DARK)
    queries = domain_data[target_domain]
    datetimes = []
    for q_data in queries.values():
        for item in q_data:
            if item[0] not in datetimes:
                datetimes.append(item[0])

    query_names = list(queries.keys())
    total_cols = 1 + (len(query_names) * 2)  # 1 Datetime col + (Rank & Delta) per query

    # --- Write Headers ---
    # Row 1: Merged Title Row
    worksheet.merge_range(0, 0, 0, total_cols - 1, target_domain, title_format)
    worksheet.set_row(0, 25)  # Make title row slightly taller

    # Column A Width
    worksheet.set_column(0, 0, 18)

    # Establish Row 2 & Row 3 headers for the Datetime column
    worksheet.write(1, 0, "", border_only)
    worksheet.write(2, 0, "Datetime", get_header_format(COLOR_DARK, bold=True))

    # Alternate colors for each query block, starting with the Light color
    colors = [COLOR_LIGHT, COLOR_DARK]
    query_formats = []

    col_idx = 1
    for i, query_name in enumerate(query_names):
        bg_color = colors[i % len(colors)]

        # Merge Row 2 for the query name across "Rank" and "Rank Delta"
        worksheet.merge_range(1, col_idx, 1, col_idx + 1, f"Query: {query_name}", get_header_format(bg_color))

        # Row 3 Subheaders
        worksheet.write(2, col_idx, "Rank", get_header_format(bg_color, bold=True))
        worksheet.write(2, col_idx + 1, "Rank Delta", get_header_format(bg_color, bold=True))

        # Set column width for Rank and Delta to comfortably fit the text
        worksheet.set_column(col_idx, col_idx + 1, 12)

        # Keep track of formats tied to this data block
        query_formats.append(get_data_format(bg_color))
        col_idx += 2

    # --- Write Logic and Data ---
    row_idx = 3  # Starting row for actual data variables

    for dt in datetimes:
        # Write Datetime explicitly
        worksheet.write(row_idx, 0, dt, datetime_format)

        col_idx = 1
        for i, query_name in enumerate(query_names):
            data_points = queries[query_name]
            fmt = query_formats[i]

            curr_rank = None
            prev_rank = None

            # Find the rank at this datetime and the previous one for Delta calculation
            for idx, item in enumerate(data_points):
                if item[0] == dt:
                    curr_rank = item[1]
                    if idx > 0:
                        prev_rank = data_points[idx - 1][1]
                    break

            # Formate and Calculate Rank Delta
            delta = 0
            if curr_rank is not None and prev_rank is not None:
                try:
                    delta = float(curr_rank) - float(prev_rank)

                    # Convert to integer if cleanly divisible, to prevent trailing .0
                    if delta.is_integer():
                        delta = int(delta)

                except (ValueError, TypeError):
                    delta = 0  # Failsafe if the dictionary passes string literals ('rank1')

            # Write mapped cells
            if curr_rank is not None:
                worksheet.write(row_idx, col_idx, curr_rank, fmt)
                worksheet.write(row_idx, col_idx + 1, delta, fmt)
            else:
                worksheet.write(row_idx, col_idx, "", fmt)
                worksheet.write(row_idx, col_idx + 1, "", fmt)

            col_idx += 2

        row_idx += 1

    workbook.close()

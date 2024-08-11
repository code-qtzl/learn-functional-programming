
from functools import reduce


def create_html_table(data_rows):
    tag_cell = create_tagger("td")
    tag_header = create_tagger("th")
    tag_row = create_tagger("tr")
    tag_table = create_tagger("table")

    def create_table_headers(headers):
        # Create header cells using tag_header
        header_cells = map(tag_header, headers)
        # Join header cells and wrap them in a row
        header_row = tag_row("".join(header_cells))
        
        # Convert each list in data_rows into HTML rows using reduce
        def row_to_html(row):
            # Convert each item in the row to a table cell
            cells = map(tag_cell, row)
            # Combine cells into a table row
            return tag_row("".join(cells))
        
        # Use reduce to create a single string of all table rows
        rows_html = reduce(lambda acc, row: acc + row_to_html(row), data_rows, "")

        # Combine the header row and data rows into the table
        table_html = tag_table(header_row + rows_html)
        return table_html

    return create_table_headers


# don't touch below this line


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger

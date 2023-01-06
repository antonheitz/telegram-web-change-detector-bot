from typing import List


def create_table(table: List[List[str]]) -> str:
    table_str: str = "\n"
    for index, row in enumerate(table):
        new_row: str = "|"
        for cell in row:
            new_row += cell + "|"
        if index == 0:
            new_row += "\n|"
            for cell in row:
                new_row += "---|"
        table_str += new_row + "\n"
    return table_str.replace("|", "\|").replace("-", "\-").replace("<", "\<").replace(">", "\>")
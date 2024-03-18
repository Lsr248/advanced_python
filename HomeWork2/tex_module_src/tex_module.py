DOCUMENT_SETTINGS = (
    "\documentclass[12pt, a4paper] {article} \n\\usepackage[utf8] {inputenc} \n\\usepackage[T2A]{"
    "fontenc} \n\\usepackage[english, russian] {babel} \n\\usepackage[top=30pt,bottom=30pt,left=48pt,"
    "right=46pt]{geometry}\n \\usepackage{graphicx}"
)

TABLE_TEMPLATE = "\\begin{{center}}\n\\begin{{tabular}}{tabular_settings}\n{table}\\end{{tabular}}\n\\end{{center}}\n"
DOCUMENT_TEMPLATE = (
    "{document_settings}\n\\begin{{document}}\n\n{content}\n\n\\end{{document}}"
)
IMAGE_TEMPLATE = "\\begin{{figure}}[t]\n\\includegraphics[width=8cm]{{{image_path}}}\n\\centering\n\\end{{figure}}"


def save_code_in_tex_file(tex_code: str, file_abs_path: str):
    """
    Saves tex_code to file file_abs_path
    """
    with open(file_abs_path, "w") as file:
        file.write(tex_code)
        file.close()


def generate_table(table: list[list]) -> str:
    """
    Generates content without "begin" commands in tex format
    """
    if not check_table(table):
        raise Exception("Wrong dimensions of table")
    tex_str_template = " {row} \\\\\n \\hline\n"
    cols_names = ""
    for elem in table[0]:
        cols_names += str(elem) + " & "
    cols_names = cols_names[: len(cols_names) - 2] + "\\\\"

    result = " \\hline\n {cols_names}\n \\hline\\hline\n".format(cols_names=cols_names)

    for row in table[1:]:
        result_table_row = ""
        for elem in row:
            result_table_row += str(elem) + " & "
        result += tex_str_template.format(
            row=result_table_row[: len(result_table_row) - 2]
        )

    return result


def generate_image_content(image_path: str) -> str:
    """
    Generates tex_code for adding image
    """
    return IMAGE_TEMPLATE.format(image_path=image_path)


def create_tabular(cols_number: int) -> str:
    return "{{||{settings}||}}".format(settings=" c " * cols_number)


def generate_table_content(table: list[list]) -> str:
    """
    Generates tex_code for table from arguments in str
    Table should contain columns names in table[0] and all elements must have same non-zero size.
    Table also must contain first line
    """
    return TABLE_TEMPLATE.format(
        tabular_settings=create_tabular(len(table[0])), table=generate_table(table)
    )


def check_table(table: list[list]) -> bool:
    if len(table) < 2:
        return False
    size = len(table[0])
    for row in table:
        if len(row) != size:
            return False
    return True


def generate_tex_file_in_str(content: str) -> str:
    """
    Generates .tex file for str
    """

    result = DOCUMENT_TEMPLATE.format(
        document_settings=DOCUMENT_SETTINGS, content=content
    )
    return result

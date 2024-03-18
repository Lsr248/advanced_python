DOCUMENT_SETTINGS = "\documentclass[12pt, a4paper] {article} \n\\usepackage[utf8] {inputenc} \n\\usepackage[T2A]{" \
                    "fontenc} \n\\usepackage[english, russian] {babel} \n\\usepackage[top=30pt,bottom=30pt,left=48pt," \
                    "right=46pt]{geometry}"

BEGINS_TEMPLATE = "\\begin{{document}}\n\\begin{{center}}\n\\begin{{tabular}}{tabular_settings}"
ENDS = "\\end{tabular}\n\\end{center}\n\\end{document}"
DOCUMENT_TEMPLATE = "{document_settings}\n\n{begins}\n\n{content}\n\n{ends}"

class TexBody:
    def __init__(self, begins: str, content: str, ends: str):
        self.begins = begins
        self.content = content
        self.ends = ends


def save_code_in_tex_file(tex_code: str, file_abs_path: str):
    with open(file_abs_path, "w") as file:
        file.write(tex_code)


def generate_table(table: list[list]) -> str:
    if not check_table(table):
        raise Exception("Wrong dimensions of table")
    tex_str_template = " {row} \\\\\n \\hline\n"
    cols_names = ""
    for elem in table[0]:
        cols_names += str(elem) + " & "
    cols_names = cols_names[:len(cols_names) - 2] + "\\\\"

    result = " \\hline\n {cols_names}\n \\hline\\hline\n".format(cols_names=cols_names)

    for row in table[1:]:
        result_table_row = ""
        for elem in row:
            result_table_row += str(elem) + " & "
        result += tex_str_template.format(row=result_table_row[:len(result_table_row) - 2])

    return result


def generate_table_tex_body(table: list[list]) -> TexBody:
    begins = BEGINS_TEMPLATE.format(tabular_settings=create_tabular(len(table[0])))
    content = generate_table(table)
    return TexBody(begins, content, ENDS)


def create_tabular(cols_number: int) -> str:
    return "{{||{settings}||}}".format(settings=" c " * cols_number)


def check_table(table: list[list]) -> bool:
    if len(table) < 2:
        return False
    size = len(table[0])
    for row in table:
        if len(row) != size:
            return False
    return True


def generate_tex_file_in_str(tex_body: TexBody) -> str:
    """
       Generates .tex file for creating table from arguments
       Table should contain columns names in table[0] and all elements must have same non zero size.
       Table also must contain first line
    """

    result = DOCUMENT_TEMPLATE.format(document_settings=DOCUMENT_SETTINGS, begins=tex_body.begins,
                                      content=tex_body.content, ends=tex_body.ends)
    return result

from HomeWork2.tex_module.tex_module import (
    save_code_in_tex_file,
    generate_table_content,
    generate_image_content,
    generate_tex_file_in_str,
)
import os
from pdflatex import PDFLaTeX

ARTIFACT_RELATIVE_PATH = "/artifacts/task2/"


def main():
    table = [["col1, col2, col3"], ["row11, row12, row13"], ["row21, row22, row23"]]
    tex_code = ""
    try:
        table_content = generate_table_content(table)
        image_content = generate_image_content("image1.png")
        tex_code = generate_tex_file_in_str(table_content + image_content)
        abs_path_for_saving_file = (
            os.path.abspath(os.getcwd()) + ARTIFACT_RELATIVE_PATH + "example.tex"
        )
        save_code_in_tex_file(tex_code, abs_path_for_saving_file)

        pdfl = PDFLaTeX.from_texfile(abs_path_for_saving_file)
        pdf, log, completed_process = pdfl.create_pdf()

        with open(
            os.path.abspath(os.getcwd()) + ARTIFACT_RELATIVE_PATH + "example.pdf", "wb"
        ) as file:
            file.write(pdf)
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()

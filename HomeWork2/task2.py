from tex_module import *
from pdflatex import PDFLaTeX


def main():
    table = [["col1, col2, col3"], ["row11, row12, row13"], ["row21, row22, row23"]]
    tex_code = ""
    try:
        table_content = generate_table_content(table)
        image_content = generate_image_content("image1.png")
        tex_code = generate_tex_file_in_str(table_content + image_content)
        save_code_in_tex_file(tex_code, "HomeWork2/artifacts/task2/example.tex")

        pdfl = PDFLaTeX.from_texfile("HomeWork2/artifacts/task2/example.tex")
        pdf, log, completed_process = pdfl.create_pdf()

        with open("HomeWork2/artifacts/task2/example.tex", "wb") as file:
            file.write(pdf)
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()

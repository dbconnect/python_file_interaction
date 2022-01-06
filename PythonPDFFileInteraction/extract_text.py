import PyPDF2


def extract_text():
    with open("input_1.pdf", "rb") as pdfFile:
        pdf_file_reader = PyPDF2.PdfFileReader(pdfFile)
        for i in range(pdf_file_reader.numPages):
            page = pdf_file_reader.getPage(i)
            print(page.extractText())


if __name__ == '__main__':
    extract_text()

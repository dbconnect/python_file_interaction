import PyPDF2


def merge():
    with open("input_1.pdf", "rb") as pdfFile1:
        with open("input_2.pdf", "rb") as pdfFile2:
            pdf_file_reader_1 = PyPDF2.PdfFileReader(pdfFile1)
            pdf_file_reader_2 = PyPDF2.PdfFileReader(pdfFile2)
            pdf_writer = PyPDF2.PdfFileWriter()
            for i in range(pdf_file_reader_1.numPages):
                page = pdf_file_reader_1.getPage(i)
                pdf_writer.addPage(page)

            for i in range(pdf_file_reader_2.numPages):
                page = pdf_file_reader_2.getPage(i)
                pdf_writer.addPage(page)

            with open("output_merged.pdf", "wb") as outFile:
                pdf_writer.write(outFile)


if __name__ == '__main__':
    merge()

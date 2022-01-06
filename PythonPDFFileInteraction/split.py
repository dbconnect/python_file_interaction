import PyPDF2


def split():
    with open("input_1.pdf", "rb") as pdfFile1:
        pdf_file_reader_1 = PyPDF2.PdfFileReader(pdfFile1)

        for i in range(pdf_file_reader_1.numPages):
            pdf_writer = PyPDF2.PdfFileWriter()
            page = pdf_file_reader_1.getPage(i)
            pdf_writer.addPage(page)
            with open("output_part_%s.pdf" % i, "wb") as outFile:
                pdf_writer.write(outFile)


if __name__ == '__main__':
    split()

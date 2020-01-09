import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)  # goes through each page on template
    page.mergePage(watermark.getPage(0))  # merges watermark 0 on top of each template page
    output.addPage(page)  # add each page to output file

    with open('watermarked_output.pdf', 'wb') as file:  # create new file with this name
        output.write(file)  # write the file to output

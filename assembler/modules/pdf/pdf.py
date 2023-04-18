"""
Generate PDF file from published JPG files
"""

from reportlab.pdfgen import canvas


def add_page_number(pdf_file, num, page):
    """
    Draw page number on each pdf page

    :param pdf_file:
    :param num:
    :param page:
    :return:
    """

    pos_x = 20
    if num % 2 != 0:
        pos_x = 2450

    pdf_file.setFont('Helvetica', 60)
    pdf_file.drawString(pos_x, 20, page.page_number)


def generate_pdf(book, path_pdf, versioned_pages):
    """
    Generate PDF file from book pages
    """

    size_x = 2598
    size_y = 3366
    pdf_file = canvas.Canvas(path_pdf, pagesize=(size_x, size_y))
    pdf_file.setTitle('The Secret Code of Superheroes')

    for num, page in enumerate(book.list_pages):

        if not num == 0:  # Make next page
            pdf_file.showPage()

        version = page.get_published_version()

        if not version:
            continue

        jpg_path = '{0}/{1}_{2}.jpg'.format(versioned_pages, page.page_number, version)
        pdf_file.drawImage(jpg_path, 0, 0, size_x, size_y)
        add_page_number(pdf_file, num, page)

    pdf_file.save()

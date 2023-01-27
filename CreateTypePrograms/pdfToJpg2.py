import pypdfium2 as pdfium




# print(imgFileName)



def pdfToJpg2(Location, fileName):
    if __name__ == '__main__':
            pdfToJpg2Function(Location, fileName)

def pdfToJpg2Function(Location, fileName):

    imgFileName = fileName.split('.')[:-1][0]

    pathToJpgFile = Location +'\\' + imgFileName

    pathToPdfFile = Location + '\\' + fileName
    pdf = pdfium.PdfDocument(pathToPdfFile)
    # version = pdf.get_version()  # get the PDF standard version
    n_pages = len(pdf)  # get the number of pages in the document


    page_indices = [i for i in range(n_pages)]  # all pages
    # print(page_indices)
    renderer = pdf.render_to(
        pdfium.BitmapConv.pil_image,
        page_indices = page_indices,
        scale = 300/72,  # 300dpi resolution
    )

    # print(renderer)



    for i, image in zip(page_indices, renderer):
        # print(i)
        # print(pathToJpgFile + '_'+ str(i) + '.jpg' )
        
        image.save(pathToJpgFile + '_'+ str(i) + '.jpg' )
        # print(image)

    # print('Done')




Location = r'C:\Users\Tigereye\Desktop\New folder'

fileName = 'temp_PASSOS PARA ATIVAÇÃO DO SEU OFFICE 2019 (2) (2) (1) (4) (1) (1) (1) (1) (4) (1) (1)_aRy4vDN.pdf'

pdfToJpg2(Location, fileName)
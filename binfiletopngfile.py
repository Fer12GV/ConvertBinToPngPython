from libtiff import TIFF
from wand.image import Image as wi


#Convert bin file to pdf(really tiff format) file

cont = 0
file = open('fer.pdf', 'wb')
for line in open('18340.bin', 'rb').readlines():
    cont += 1
    print(line)
    file.write(line)
    if cont == 7000:
        file.close()
        break


#Convert the first pdf format(really is Tiff format) in other pdf format (Use the LIBTIFF Library)

tiff = TIFF.open('fer.pdf', mode='r')
tiff2 = TIFF.open('ferCopy.pdf', mode='w')
image = tiff.read_image()

#Copy the file in other file
for image in tiff.iter_images():
    tiff2.write_image(image)
tiff2.close()

#Convert and separate the pdf pages in png files (Use the WAND Library)
pdf = wi(filename="ferCopy.pdf", resolution=300)
pdfimage = pdf.convert("png")
i=1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".png")
    i +=1

from dataclasses import dataclass
import qrcode 
qr = qrcode.QRCode(
    version = 15,   # higher the number of version, higher the quality(complexity) of the qr code
    box_size = 10,  # size of the box in which qr code will be shown
    border = 5      # border from all the four sides
)
data = "http://www.mmmut.ac.in/"   # data that the qr code shows after scanning 
qr.add_data(data)  # adding data in qr variable
qr.make(fit=True)  # if size is not provided it finds the best fit for the data
img = qr.make_image(fill = "black", back_color="white")
img.save("QRCode Generator\qr.png")
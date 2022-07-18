import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image ,ImageFont, ImageDraw
myFont = ImageFont.truetype('trebuc.ttf', 16)
try:
    minimumTableNo = int(input("Enter the minimum table number: "))
    maximumTableNo = int(input("Enter the maximum table number: "))
except  ValueError:
    print("Please enter a valid number")
else:
    for tableNo in range(minimumTableNo, maximumTableNo+1):
        s = f"https://order.coverallweb.in?tableNo={tableNo}"
        url = pyqrcode.create(s)
        url.png(f'qr codes/table-{tableNo}.png', scale = 6)
        qrCode = Image.open(f'qr codes/table-{tableNo}.png')
        background = Image.open("Scan Template.png")
        blackFrame = Image.open("Black frame.png")
        blackFrame.paste(qrCode, (0, 0), qrCode)
        background.paste(blackFrame, (0, 100), blackFrame)
        I1 = ImageDraw.Draw(background)
        I1.text((10, 380), f"Table No: {tableNo}", font=myFont, fill =(0, 0, 0))
        background.save(f"Generated Templates/table-{tableNo}.png")
    print("Program run successfully")
    
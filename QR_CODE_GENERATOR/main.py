
import qrcode
# Simple One - Simple Text
# img = qrcode.make("Hello World, This is Benben.")
# img.save("QR_CODE_GENERATOR/QRCODE_SAVED/benben.png")

# QR Object - Works for URLs
qr = qrcode.QRCode(version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4)

qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("QR_CODE_GENERATOR/QRCODE_SAVED/advanced.png")
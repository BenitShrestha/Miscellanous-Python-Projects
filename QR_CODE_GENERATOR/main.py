
import qrcode
import qrcode.image.svg
# Simple One - Simple Text
# img = qrcode.make("Hello World, This is Benben.")
# img.save("QR_CODE_GENERATOR/QRCODE_SAVED/benben.png")

# QR Object - Works for URLs
# qr = qrcode.QRCode(version=1, 
#     error_correction=qrcode.constants.ERROR_CORRECT_H, 
#     box_size=10, 
#     border=4) # These parameters can be changed

# qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# qr.make(fit = True)

# # Colors not working currently
# img = qr.make_image(fill_color = "red", back_color = "green")
# img.save("QR_CODE_GENERATOR/QRCODE_SAVED/advanced.png")

# QR Code - Vector Graphics, SVG files
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory = factory)
svg_img.save(r"QR_CODE_GENERATOR\QRCODE_SAVED\myqr.svg")

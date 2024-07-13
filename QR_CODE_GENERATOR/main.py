
import qrcode
import qrcode.image.svg
# Simple One - Simple Text
img = qrcode.make(''' Hello World, This is Benben.
    I am learning how to make QR Codes.''')
img.save("QR_CODE_GENERATOR/QRCODE_SAVED/benben_one.png")

# QR Object - Works for URLs
qr = qrcode.QRCode(version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=8, 
    border=5) # These parameters can be changed

qr.add_data("https://www.bestbuy.com/site/asus-rog-zephyrus-g14-14-oled-3k-120hz-gaming-laptop-amd-ryzen-9-8945hs-16gb-lpddr5x-nvidia-geforce-rtx-4060-1tb-ssd-platinum-white/6570270.p?skuId=6570270")
qr.make(fit = True)

# Colors not working currently
img = qr.make_image(fill_color = "red", back_color = "green")
img.save("QR_CODE_GENERATOR/QRCODE_SAVED/zephyrusG14.jpg")

# QR Code - Vector Graphics, SVG files
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hola! Espanyol", image_factory = factory)
''' Generates vector graphics, doesn't lose quality in zoomed in or out '''
svg_img.save(r"QR_CODE_GENERATOR\QRCODE_SAVED\myqr_vector.svg")

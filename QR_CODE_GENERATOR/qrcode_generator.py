
import qrcode
# Simple One 
img = qrcode.make("Hello World, This is Benben.")
img.save("QR_CODE_GENERATOR/QRCODE_SAVED/benben.png")
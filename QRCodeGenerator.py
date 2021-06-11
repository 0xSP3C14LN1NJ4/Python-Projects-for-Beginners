import qrcode

# Data to put in the QR code
img = qrcode.make("Helllo World!")

# Save the QR code as an image
img.save("image.png")
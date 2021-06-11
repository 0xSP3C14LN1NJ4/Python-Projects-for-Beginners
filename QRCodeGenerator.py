import qrcode

# Data to put in the QR code
data = input("Enter the data you want in the QR code: ")

# Generate the QR code
img = qrcode.make(data)

# Save the QR code as an image
img.save("image.png")
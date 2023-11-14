import qrcode
import time

# Get the link from the user
link = input("Enter the link: ")

# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

#Time Sleep Stop
time.sleep(3)

# Save the QR code image
img.save("qrcode.png")

#Time Sleep Stop
time.sleep(2)

print("QR code generated successfully!")

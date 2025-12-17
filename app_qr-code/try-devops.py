"""
Script to generate the custom QR code for your application
"""

import qrcode
import datetime
from qrcode.constants import ERROR_CORRECT_H

# Get current script runtime
script_runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"The script ran at: {script_runtime}")

# Get URL from user
url = input("Enter the URL to generate QR code for: ")

# Create QR code
trydevops = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
trydevops.add_data(url)
trydevops.make(fit=True)

# Generate and save image
img = trydevops.make_image(fill_color="black", back_color="white")
img.save("trydevops_qr.png")

print("QR code generated and saved as 'trydevops_qr.png'.")


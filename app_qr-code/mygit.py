"""
Python Script to generate QR for your application
"""

import qrcode, datetime
run_time = datetime.datetime.now().strftime("%Y-%m-%d")
print(f"QR has created at this time: {run_time}")

#variables
url="https://github.com/thangacodes"

from qrcode.constants import ERROR_CORRECT_H
thangacodes = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
thangacodes.add_data(url)
thangacodes.make(fit=True)

img = thangacodes.make_image(fill_color="black", back_color="white")
img.save("thangacodes_qr.png")

import qrcode
from qrcode.constants import ERROR_CORRECT_H
trydevops = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
trydevops.add_data("https://www.try-devops.xyz/")
trydevops.make(fit=True)

img = trydevops.make_image(fill_color="black", back_color="white")
img.save("trydevops_qr.png")

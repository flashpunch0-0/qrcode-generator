import qrcode
import os
# List of links you want to generate QR codes for
links = ["https://www.youtube.com/", "https://best.aliexpress.com/?spm=a2g0o.best.1000002.1.1f852c25lXF7nw&browser_redirect=true", "https://www.perplexity.ai/"]

# Output directory where QR codes will be saved
output_directory = "qr_codes/"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate QR codes for each link
for i, link in enumerate(links):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(output_directory + f"qrcode_{i+1}.png")

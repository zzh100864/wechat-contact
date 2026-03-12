import qrcode
from PIL import Image, ImageDraw, ImageFont

# The URL to encode
url = "https://e4eec692fa6b9d.lhr.life/wechat-contact.html"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Add text below the QR code (optional but helpful)
try:
    # Create a new image with extra space for text
    width, height = img_qr.size
    new_height = height + 50
    new_img = Image.new('RGB', (width, new_height), 'white')
    new_img.paste(img_qr, (0, 0))

    draw = ImageDraw.Draw(new_img)
    # Use default font since we might not have a specific font file
    # Or load a default font if possible
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    # Draw text
    text = "Scan to Contact"
    # Calculate text size using getbbox (for Pillow >= 9.2.0)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = height + (50 - text_height) // 2
    
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    img_final = new_img
except Exception as e:
    print(f"Error adding text: {e}")
    img_final = img_qr

# Save the image
img_final.save("wechat-contact-qr.png")
print("QR code saved as wechat-contact-qr.png")

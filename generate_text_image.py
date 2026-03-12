from PIL import Image, ImageDraw, ImageFont

# The URL to encode
url = "https://e4eec692fa6b9d.lhr.life/wechat-contact.html"

# Image dimensions
width = 800
height = 200
background_color = "white"
text_color = "black"

# Create a new image
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load font
try:
    # Try to load Arial
    font = ImageFont.truetype("arial.ttf", 24)
    font_large = ImageFont.truetype("arial.ttf", 36)
except IOError:
    # Fallback to default font
    font = ImageFont.load_default()
    font_large = ImageFont.load_default()

# Text to draw
title = "咨询请手动复制或输入以下链接："
footer = "(请在浏览器中打开)"

# Calculate positions (center text)
# Title
bbox_title = draw.textbbox((0, 0), title, font=font)
title_w = bbox_title[2] - bbox_title[0]
title_x = (width - title_w) // 2
title_y = 40

# URL
bbox_url = draw.textbbox((0, 0), url, font=font_large)
url_w = bbox_url[2] - bbox_url[0]
url_x = (width - url_w) // 2
url_y = 90

# Footer
bbox_footer = draw.textbbox((0, 0), footer, font=font)
footer_w = bbox_footer[2] - bbox_footer[0]
footer_x = (width - footer_w) // 2
footer_y = 150

# Draw text
draw.text((title_x, title_y), title, fill="gray", font=font)
draw.text((url_x, url_y), url, fill="blue", font=font_large)
draw.text((footer_x, footer_y), footer, fill="gray", font=font)

# Save the image
image.save("link_text.png")
print("Link text image saved as link_text.png")

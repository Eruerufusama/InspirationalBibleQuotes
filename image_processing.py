from PIL import Image, ImageFont, ImageDraw, ImageFilter    # pip install Pillow
from textwrap import wrap


def put_quote_on_wallpaper(wallpaper, biblequote):
    lines = wrap(biblequote, 40)  # Split verse into multiple lines if needed
    font = ImageFont.truetype('./fonts/Roboto-Medium.ttf', 48)  # Define font-parameters

  # Open layers
    image = Image.open(wallpaper)  # Background
    text_layer = Image.new('RGBA', (image.size[0], image.size[1]), None)  # Text-layer

  # Create draw-object
    draw = ImageDraw.Draw(text_layer)

  # Draw text onto text-layer
    x = 100
    y = 100
    offset = 2

  # Draws shadow
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x + offset, y + offset), line, "black", font)
        y += height
    y = 100

  # Draws overlaid text
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x, y), line, "white", font)

        y += height

  # Merges layers
    image.paste(text_layer, (0, 0), text_layer)

  # Debug
    # image.show()

    image.save('./photo_of_the_day.jpg')

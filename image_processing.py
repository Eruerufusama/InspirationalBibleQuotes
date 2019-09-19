import sys
from PIL import Image, ImageFont, ImageDraw, ImageFilter    # pip install Pillow
from textwrap import wrap
import pre_processing
import logger

def create_text_layer(canvas_size, lines, settings):

    # Applies settings to text from settings.json
    text_align_horizontal = settings["text"]["horizontal align"]
    text_align_vertical = settings["text"]["vertical align"]
    shadow_offset = settings["text"]["shadow offset"]
    font_type = sys.path[0] + settings["text"]["font"]
    font_size = settings["text"]["font-size"]
    margin = settings["canvas"]["margin"]

    # Define font-parameters
    font = ImageFont.truetype(font_type, font_size)  
    # Create layer
    text_layer = Image.new('RGBA', (canvas_size[0], canvas_size[1]), None)  # Text-layer

    # Create draw-object
    draw = ImageDraw.Draw(text_layer)

    # Variable dump
    text_height = font.getsize(lines[0])[1]
    paragraph_height = text_height * len(lines)

    # Aligns text vertically based on settings
    if text_align_vertical.lower() == "center":
        y = int(canvas_size[1] / 2 - paragraph_height / 2)
    elif text_align_vertical.lower() == "top":
        y = int(canvas_size[1] * margin)
    elif text_align_vertical.lower() == "bottom":
        y = int(canvas_size[1] * (1 - margin) - paragraph_height)
    else:
        msg = f'Error: invalid text-alignment used'
        logger.log('Error', None, None, None, msg)
        exit()

    # Alignes text horisontally based on settings
    for line in lines:
        text_width = font.getsize(line)[0]

        if text_align_horizontal.lower() == "center":
            start_position = canvas_size[0] / 2 - text_width / 2
        elif text_align_horizontal.lower() == "left":
            start_position = canvas_size[0] * margin
        elif text_align_horizontal.lower() == "right":
            start_position = canvas_size[0] * (1 - margin) - text_width
        else:
            msg = f'Error: invalid text-alignment used'
            logger.log('Error', None, None, None, msg)
            exit()

        # Draw actual text
        if shadow_offset > 0:

            # Shadow
            draw.text((start_position + shadow_offset, y + shadow_offset), line, "black", font)

        # Overlaid text
        draw.text((start_position, y), line, "white", font)

        # Move down to draw next line
        y += text_height

    return text_layer

def put_quote_on_wallpaper(wallpaper, biblequote, settings):
    # Variables
    max_characters_per_line = settings["text"]["characters per line"]

    lines = wrap(biblequote, max_characters_per_line)  # Split verse into multiple lines if needed

    # Create layers
    image = Image.open(wallpaper)  # Background
    text_layer = create_text_layer(image.size, lines, settings)  # Text

    # Merges layers
    while True:
        try:
            image.paste(text_layer, (0, 0), text_layer)
            break
        except:
            pre_processing.get_img(settings)

    # Debug
    # image.show()

    image.save(sys.path[0] + '/resources/photo_of_the_day.jpg')
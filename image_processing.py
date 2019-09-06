from PIL import Image, ImageFont, ImageDraw, ImageFilter    # pip install Pillow
from textwrap import wrap
import pre_processing

def create_text_layer(canvas_size, lines, text_align_horizontal, text_align_vertical, shadow_offset):
  font = ImageFont.truetype('./fonts/Roboto-Medium.ttf', 44)  # Define font-parameters
  # Create layer
  text_layer = Image.new('RGBA', (canvas_size[0], canvas_size[1]), None)  # Text-layer

  # Create draw-object
  draw = ImageDraw.Draw(text_layer)

  # Vars
  text_height = font.getsize(lines[0])[1]
  paragraph_height = text_height * len(lines)
  margin = 0.1

  if text_align_vertical.lower() == "center":
    y = int(canvas_size[1] / 2 - paragraph_height / 2)
  elif text_align_vertical.lower() == "top":
    y = int(canvas_size[1] * margin)
  elif text_align_vertical.lower() == "bottom":
    y = int(canvas_size[1] * (1 - margin) - paragraph_height)

  for line in lines:
    # Define some variables on each iteration
    text_width = font.getsize(line)[0]
    if text_align_horizontal.lower() == "center":
      start_position = canvas_size[0] / 2 - text_width / 2
    elif text_align_horizontal.lower() == "left":
      start_position = canvas_size[0] * margin
    elif text_align_horizontal.lower() == "right":
      start_position = canvas_size[0] * (1 - margin) - text_width

    # Draw actual text
    if shadow_offset > 0:
      draw.text((start_position + shadow_offset, y + shadow_offset), line, "black", font) # Shadow
    draw.text((start_position, y), line, "white", font) # Overlaid text

    # Move down to draw next line
    y += text_height

  return text_layer

def put_quote_on_wallpaper(wallpaper, biblequote):
  lines = wrap(biblequote, 40)  # Split verse into multiple lines if needed
  # Create layers
  image = Image.open(wallpaper)  # Background
  text_layer = create_text_layer(image.size, lines, "left", "bottom", 2)
  # Merges layers
  while True:
    try:
      image.paste(text_layer, (0, 0), text_layer)
      break
    except:
      pre_processing.get_img()

# Debug
  #image.show()

  image.save('./photo_of_the_day.jpg')

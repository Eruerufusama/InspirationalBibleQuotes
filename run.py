def main():
    put_quote_on_wallpaper("maxresdefault.jpg", "Kermit the frog did 9/11")

def put_quote_on_wallpaper(wallpaper, biblequote):
    from PIL import Image, ImageFont, ImageDraw

# Open image --------------------------------------- #
    image = Image.open(wallpaper)

# Select Font-type, Font-size ---------------------- #
    font = ImageFont.truetype("comic.ttf", 48)

# Draw text onto wallpaper ------------------------- #
    draw = ImageDraw.Draw(image)
    draw.text((100, 100), biblequote, "black", font)

# Debug
    image.save("1.png")


if __name__ == "__main__":
    main()
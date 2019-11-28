# Home-made family recipes
from functions import open_json, file_to_list

# Third party modules
from PIL import Image as IMG
from PIL import ImageDraw, ImageFont, ImageFilter
from random import randint
from urllib.request import urlretrieve
import sys
from textwrap import wrap


class Image:
    '''

    Object that controls the image mounted to the tweet-object.
    By default, this object will be empty.

    To create an image, run the 'image'-method associated with this class.

    '''

    def __init__(self):
        self.load_settings()
        self.evaluate_settings()
        

    def create(self):
      # DOCUMENTATION
        '''

        Creates the image.

        '''

      # LOGIC
        self.create_background_image()
        self.create_text_layer()
        self.merge_layers()


    def create_background_image(self, source=None):
      # DOCUMENTATION
        '''

        Retrieves an image from piscum.photos by default.

        To access the image itself, refer to the 'image'-parameter associated with this object.

        '''

      # EVALUATE ARGS
        if source == None:
            source = "https://picsum.photos"

      # LOGIC
        while True:
            # Saves a random image from lorem ipsum website to a local file location.
            urlretrieve(f'{source}/{self.width}/{self.height}/', self.image_path)

            image = IMG.open(self.image_path)

            # Check that the image is not faulty.
            if self.is_image_valid(image):
                break

        self.image = image


    def is_image_valid(self, image, pixels=None):
      # DOCUMENTATION
        '''

        Makes sure the image in not empty by checking for black pixels.

        '''

      # EVALUATE PARAMS
        if pixels == None:
            pixels = 10

      # LOGIC

        # 10 is number of pixels to check. For more security, raise the number.
        for i in range(pixels):

            # Chooses random coordinates to choose a pixel from.
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)

            pixel = image.getpixel((x, y))

            # If any pixel returns a non-black value, the image did likely successfully load.
            if pixel[0] != 0 and pixel[1] != 0 and pixel[2] != 0:
                return True

        # If every pixel ended up being black, the image likely failed to load.
        
        print(f"Image failed to load...")
        return False


    def create_text_layer(self):
      # DOCUMENTATION
        '''

        Create text-layer based on randomly fetched text from file.

        '''

      # LOGIC
        self.text_layer = IMG.new('RGBA', (self.width, self.height), None)
        self.create_font()
        self.create_draw_object()
        self.get_text()
        self.split_text()
        self.draw_text()


    def save(self):
      # DOCUMENTATION
        '''

        Saves the image to file based on the object's image-path.

        '''

      # LOGIC
        self.image.save(self.image_path)


    def get_text(self):
      # DOCUMENTATION
        '''

        Fetches a random string of text from this object's 'text_source' into this object's 'text'-property.

        '''

      # LOGIC
        list_of_text = file_to_list(self.text_source)
        i = randint(0, len(list_of_text) - 1)

        self.text = list_of_text[i]


    def draw_text(self):
      # DOCUMENTATION
        '''

        Draws text onto the text-layer.

        '''

      # LOGIC
        self.get_text_height()
        self.get_paragraph_height()

        y = self.get_vertical_pos()

        for line in self.lines:
            x = self.get_horizontal_pos(line)

            if self.has_shadow():
                self.draw.text((x + self.shadow_offset, y + self.shadow_offset), line, "black", self.font)

            self.draw.text((x, y), line, "white", self.font)

            y += self.text_height


    def get_vertical_pos(self):
      # DOCUMENTATION
        '''

        Returns the vertical starting position of text to be drawn.

        '''

      # LOGIC
        if self.text_align_vertical.lower() == "center":
            return int(self.height / 2 - self.paragraph_height / 2)

        elif self.text_align_vertical.lower() == "top":
            return int(self.height * self.margin)

        elif self.text_align_vertical.lower() == "bottom":
            return int(self.height * (1 - self.margin) - self.paragraph_height)


    def get_horizontal_pos(self, line):
      # DOCUMENTATION
        '''

        Returns the horizontal starting position of text to be drawn.

        '''

      # LOGIC
        text_width = self.font.getsize(line)[0]

        if self.text_align_horizontal.lower() == "center":
            return self.width / 2 - text_width / 2

        elif self.text_align_horizontal.lower() == "left":
            return self.width * self.margin

        elif self.text_align_horizontal.lower() == "right":
            return self.width * (1 - self.margin) - text_width


    def has_shadow(self):
      # DOCUMENTATIOn
        '''

        Returns true if the text has shadow.

        '''

      # LOGIC
        return True if self.shadow_offset > 0 else False


    def create_font(self):
      # DOCUMENTATION
        '''

        Creates a font-object based on settings.

        '''

      # LOGIC
        self.font = ImageFont.truetype(self.font_type, self.font_size)


    def create_draw_object(self):
      # DOCUMENTATION
        '''

        Creates a draw-object from the text-layer.

        '''

      # LOGIC
        self.draw = ImageDraw.Draw(self.text_layer)


    def get_text_height(self):
      # DOCUMENTATION
        '''

        Retrieves the height of the font-size and stores it in the 'text_height'-parameter.

        '''

      # LOGIC
        self.text_height = self.font.getsize(self.lines[0])[1]


    def get_paragraph_height(self):
      # DOCUMENTATION
        '''

        Retrieves the height of the entire paragraph and stores it in the 'paragraph_height'-parameter.

        '''

      # lOGIC
        self.paragraph_height = self.text_height * len(self.lines)


    def split_text(self):
      # DOCUMENTATION
        '''

        Takes incoming text from the object's 'text'-parameter and splits it based on how many characters we want per line.

        Stores the resulting text in the 'lines'-parameter of the object.

        '''

      # LOGIC
        self.lines = wrap(self.text, self.chars_per_line)


    def merge_layers(self):
      # DOCUMENTATION
        '''

        Merges the background-layer and text-layer, and stores the resulting image in the 'image'-parameter of the object.

        '''

      # LOGIC
        self.image.paste(self.text_layer, (0, 0), self.text_layer)


    def load_settings(self, filepath=None):
      # DOCUMENTATION
        '''

        Loads settings

        '''

      # EVALUATE ARGS
        if filepath == None:
            filepath = "/resources/settings.json"

      # LOGIC
        settings = open_json(filepath)

        self.text_source = settings["image"]["image text source"]
        self.text_align_horizontal = settings["image"]["horizontal align"]
        self.text_align_vertical = settings["image"]["vertical align"]
        self.shadow_offset = settings["image"]["shadow offset"]
        self.font_type = sys.path[0] + settings["image"]["font source"]
        self.font_size = settings["image"]["font size"]
        self.margin = settings["image"]["margin"]
        self.width = settings["image"]["size"]["width"]
        self.height = settings["image"]["size"]["height"]
        self.chars_per_line = settings["image"]["chars per line"]
        self.image_path = sys.path[0] + settings["image"]["image file"]


    def evaluate_settings(self):
      # DOCUMENTATION
        ''' 

        Makes sure the settings are valid.

        '''

      # LOGIC
        max_size = 5000
        min_size = 240

        for size in [self.width, self.height]:
            if size > max_size:
                raise SizeError(f'Error: Given size can not exceed {max_size}px')
            if size < min_size:
                raise SizeError(f'Error: Given size can not be less than {min_size}px')


class SizeError(Exception):
    '''

    Returns if the size of the image is not valid.

    '''
    pass
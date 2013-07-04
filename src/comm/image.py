import cStringIO
from PIL import Image as PilImage
from PIL import ImageOps as PilImageOps
import os

#http://www.riisen.dk/dop/pil.html
class Image(object):
    '''
    directory = os.path.join(os.getcwd(),"uploads/")
    img_file = os.path.join(os.getcwd(),"uploads/xhzwdp.jpg")
    image = Image(img_file)
    save_path = directory + "t4_clip.jpg"
    image.resize(120, 120, save_path,mode='clip')
    save_path = directory + "t4_scale.jpg"
    image.resize(120, 120, save_path,mode='scale')
    save_path = directory + "t6_crop.jpg"
    image.crop(250, 249, 250, 350, save_path)
    '''
    MODES = ["scale", "clip"]
    FORMATS = ["PNG", "JPEG", "JPG"]

    def __init__(self, stream):
        self.stream = stream

    def resize(self, width, height,save_path,mode=None):
        """Returns a buffer to the resized image for saving"""
        if mode is not None and mode not in self.MODES:
            raise ImageModeError("Invalid image mode: '%s'" % mode)
        img = PilImage.open(self.stream)
        if img.format not in self.FORMATS:
            raise ImageFormatError("Unknown format: '%s'" % img.format)
        size = (int(width), int(height))
        if mode == "clip":
            resized = img
            resized.thumbnail(size)
        elif mode == "scale":
            resized = img.resize(size,Image.NEAREST)
        else:
            pos = (0.5, 0.5)
            resized = PilImageOps.fit(img, size, PilImage.NEAREST, 0, pos)

        resized.save(save_path, img.format)
        return True
    def crop(self,x,y,w,h,save_path):
        box = (x, y, x+w, y+h)
        #box = (x, y, x + w, y + h)
        img = PilImage.open(self.stream)
        region = img.crop(box)
        region.save(save_path,img.format)
        
class ImageModeError(Exception): pass
class ImageFormatError(Exception): pass
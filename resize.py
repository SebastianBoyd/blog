from PIL import Image
import os

INPUT_DIR = 'images/full-res/'
OUTPUT_DIR = 'images/scaled/'

IMAGES = ['katsobushi.jpg']
OUTPUT_WIDTHS = [400]

os.system('rm ' + OUTPUT_DIR + '*')

def resize(img, width):
    hw = img.size
    dim = (hw[0] / 4, hw[1] / 4)
    img.thumbnail(dim, Image.ANTIALIAS)
    return img

def load(location):
    return Image.open(location)

def save(img, location):
    img.save(location)
    return True

for i in IMAGES:
    img = load(INPUT_DIR + i)
    no_suffix = i.split('.', 1)[0]
    suffix = i.split('.', 1)[1]
    print(no_suffix)

    for w in OUTPUT_WIDTHS:
        resized = resize(img, w)
        print resized
        output_loc = OUTPUT_DIR + no_suffix + '@' + str(w) + 'px.' + suffix
        save(resized, output_loc)



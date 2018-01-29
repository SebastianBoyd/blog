from PIL import Image

INPUT_DIR = 'images/full-res/'
OUTPUT_DIR = 'images/scaled/'

img = Image.open(INPUT_DIR + 'katsobushi.jpg')
hw = img.size
small = (hw[0] / 4, hw[1] / 4)
print(small)
small = img.thumbnail(small, Image.ANTIALIAS)
img.save(OUTPUT_DIR + 'katsobushi' + '4' + '.jpg')
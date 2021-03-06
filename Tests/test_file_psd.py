from tester import *

from PIL import Image

# sample ppm stream
file = "Images/lena.psd"
data = open(file, "rb").read()

def test_sanity():
    im = Image.open(file)
    im.load()
    assert_equal(im.mode, "RGB")
    assert_equal(im.size, (128, 128))
    assert_equal(im.format, "PSD")

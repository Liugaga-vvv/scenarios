# Load Images and Convert to Grayscale

In the first sub-challenge, participants must load both the source image and the template image using OpenCV. Additionally, both images should be converted to grayscale, as this is a crucial preprocessing step for template matching.

## TODO:

Please complete the `load_and_convert_images` function in the file `/home/labex/project/load_and_convert_images.py`.
You can use the images "test_source.jpg" and "test_template.jpg" for testing.

1. Load the source image and the template image using OpenCV's `imread()` function.
2. Convert both images to grayscale using OpenCV's `cvtColor()` function.
3. Input the path of the source image and template image, and return a tuple containing the source image and the template image that were converted to grayscale.

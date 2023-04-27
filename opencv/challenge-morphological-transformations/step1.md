# Implement a Binary Image Generator

In this sub-challenge, you will create a function that generates a binary image with random shapes. This image will be used as input for the subsequent morphological transformation operations.

## Requirements:

- Generate a binary image with a black background.
- Randomly place various shapes (circles, rectangles, lines) with different sizes and colors (white or black) on the image.

## TODO:

Please complete the `generate_binary_image` function in the file `/home/labex/project/generate_binary_image.py`.

1. The `generate_binary_image` function takes the following parameters:
   - `width`: The width of the generated image.
   - `height`: The height of the generated image.
   - `num_shapes`: The number of shapes to be placed randomly in the image.
2. Generate a binary image with a black background using the provided dimensions.
3. Randomly place shapes on the image.
4. Please use `cv2.circle()` to draw circles, `cv2.rectangle()` to draw rectangles, and `cv2.line()` to draw lines.
5. Return the generated binary image.

## example

Take `generate_binary_image(400, 400, 100)` as an example to generate a binary image.

![example_image](assets/example_image.jpg)

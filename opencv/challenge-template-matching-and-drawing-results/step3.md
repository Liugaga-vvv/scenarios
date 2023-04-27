# Draw Rectangles Around Matches

After obtaining the best match locations, the next step is to visualize the results. In this sub-challenge, participants must draw rectangles around the best matches for each method, showcasing the location of the template within the source image.

## TODO:

1. For each template matching method, draw a rectangle around the best match using OpenCV's `rectangle()` function.
2. Ensure the rectangles are drawn with different colors to distinguish between different methods.
3. Rectangle using color (0, 255, 0) drawing method 'cv2.TM_SQDIFF_NORMED'; Rectangle using color (255, 0, 0) drawing method 'cv2.TM_CCOEFF_NORMED'; Rectangle using color (0, 0, 255) drawing method 'cv2.TM_CCORR_NORMED'.
4. Input the path of the source image and template image.
5. Returns a dictionary whose keys are strings of the three methods and whose values are arrays of the three images whose rectangles have been drawn.

## Example output:

```python
{
'cv2.TM_SQDIFF_NORMED': np.ndarray,
'cv2.TM_CCOEFF_NORMED': np.ndarray,
'cv2.TM_CCORR_NORMED': np.ndarray
}
```

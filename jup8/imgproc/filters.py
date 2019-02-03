import numpy as np

def center_crop(input_img, out_width, out_height):
    """Return a center cropped copy of an image array

    Args:
        input_img:  numpy array (rows, cols)
        out_width:  output x dimension
        out_height: output y dimension
    """
    img = np.copy(input_img)
    x, y = img.shape[:2]
    if (out_width > x) or (out_height > y):
        raise RuntimeError("Output shape must be smaller than img shape")
    dx = x - out_width
    dy = y - out_height
    if img.ndim == 2:
        cropped = img[dx/2: x - dx/2, dy/2: y - dy/2]
    elif img.ndim == 3:
        cropped = img[dx/2: x - dx/2, dy/2: y - dy/2, :]
    else:
        raise RuntimeError("image must be 2-D or 3-D array, %d dimensions not supported"
            % img.ndim)
    return cropped


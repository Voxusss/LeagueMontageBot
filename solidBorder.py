import cv2
from PIL import ImageColor

def add_solid_border(image_path, border_width=10):
    # Load the image
    image_path = "splash/" + image_path
    img = cv2.imread(image_path)
    # Create a border image

    border_image = cv2.copyMakeBorder(img, border_width, border_width, border_width, border_width, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    # Save the final image
    return border_image

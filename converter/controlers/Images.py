import cv2

def convert_png_to_jpg(png_path, jpg_path):
    """
    Convert a PNG image to JPEG format and save it.
    
    Args:
    - png_path (str): Path to the input PNG image file.
    - jpg_path (str): Path to save the output JPEG image file.
    
    Returns:
    - None
    """
    # Loading .png image 
    png_img = cv2.imread(png_path)
    
    # Check if the image is loaded successfully
    if png_img is None:
        print("Error: Unable to load the PNG image.")
        return
    
    # converting to jpg file and saving the jpg file 
    cv2.imwrite(jpg_path, png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Example usage:
# convert_png_to_jpg('img.png', 'modified_img.jpg')

def convert_jpg_to_png(jpg_path, png_path):
    """
    Convert a JPEG image to PNG format and save it.
    
    Args:
    - jpg_path (str): Path to the input JPEG image file.
    - png_path (str): Path to save the output PNG image file.
    
    Returns:
    - None
    """
    # Loading .jpg image 
    jpg_img = cv2.imread(jpg_path)
    
    # Check if the image is loaded successfully
    if jpg_img is None:
        print("Error: Unable to load the JPEG image.")
        return
    
    # converting to png file and saving the png file 
    cv2.imwrite(png_path, jpg_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# Example usage:
# convert_jpg_to_png('modified_img.jpg', 'converted_img.png')
def convert_jpg_to_webp(jpg_path, webp_path):
    """
    Convert a JPEG image to PNG format and save it.
    
    Args:
    - jpg_path (str): Path to the input JPEG image file.
    - webp_path (str): Path to save the output PNG image file.
    
    Returns:
    - None
    """
    # Loading .jpg image 
    jpg_img = cv2.imread(jpg_path)
    
    # Check if the image is loaded successfully
    if jpg_img is None:
        print("Error: Unable to load the JPEG image.")
        return
    
    # converting to png file and saving the png file 
    cv2.imwrite(webp_path, jpg_img, [int(cv2.IMWRITE_WEBP_QUALITY), 9])

# Example usage:
# convert_jpg_to_png('modified_img.jpg', 'converted_img.png')

import cv2
import os
from PIL import Image
import fitz
import zipfile

def convert_image(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Unable to load the image.")
        return
    if(True):
        cv2.imwrite(output_path, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

def resize_image_to_filesize(input_image_path, output_image_path, target_filesize_kb):
    """
    Resize the input image to meet the target filesize in kilobytes.
    :param input_image_path: Path to the input image.
    :param output_image_path: Path to save the resized image.
    :param target_filesize_kb: Target filesize in kilobytes.
    """
    image = Image.open(input_image_path)
    width, height = image.size
    image = image.convert("RGB")
    quality = 95

    image.save(output_image_path, optimize=True, quality=quality)
    current_filesize = os.path.getsize(output_image_path)

    while current_filesize > target_filesize_kb * 1024:
        ratio = (target_filesize_kb * 1024) / current_filesize
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_image_path, optimize=True, quality=quality)

        current_filesize = os.path.getsize(output_image_path)
        width, height = new_width, new_height
        quality -= 5
        if quality <= 0:
            break  # Break loop if quality falls below 0

    return output_image_path

def pdf_to_jpg_and_zip(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    pdf_document = fitz.open(pdf_path)
    image_paths = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{page_num+1}.jpg")
        pix.save(image_path, "jpeg")
        image_paths.append(image_path)
    pdf_document.close()
    zip_filename = str(output_folder + os.path.splitext(os.path.basename(pdf_path))[0] + '.zip')
    print(zip_filename)
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for image_path in image_paths:
            zipf.write(image_path, os.path.basename("uploads/compresed_file"+image_path))    
    return zip_filename


def truncate_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024)

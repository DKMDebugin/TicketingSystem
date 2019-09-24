import os
import random

def get_filename_ext(filepath):
    """Split file path into name & extension"""
    base_name   = os.path.basename(filepath)
    name, ext   = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    """Create New File Name"""
    new_filename    = random.randint(1, 3910209312)
    name, ext       = get_filename_ext(filename)
    final_filename  = f"{new_filename}{ext}"
    return f'tickets/{new_filename}/{final_filename}'

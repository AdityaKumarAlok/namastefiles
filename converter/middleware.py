import os

from django.conf import settings

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024)  # Convert bytes to megabytes

def truncate_folder(folder_path):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            os.remove(file_path)

class CheckFolderSizeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        size = get_folder_size("uploads")
        if size >= 100:
            truncate_folder("uploads")
        return self.get_response(request)

import os

def format_music_filename(file_path):
    base_name = os.path.basename(file_path)
    formatted_name = os.path.splitext(base_name)[0]
    return formatted_name
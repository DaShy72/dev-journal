"""
A simple script, which sorts files in a folder by type
"""

import os
import shutil
from pathlib import Path
import argparse


FILE_TYPES = {
    'images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
    'documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.txt', '.rtf'],
    'archives': ['.zip', '.tar', '.gz', '.bz2', '.rar', '.7z'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'video': ['.mp4', 'mkv', '.mov', 'avi', 'webm'],
    'code': ['.py', '.js', '.java', '.cpp', '.html', '.css', '.json', '.xml', '.sh'],
    'others': []
}

def get_category(extension: str) -> str:
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'others'

def organize_files(folder_path: str, move: bool = True, recursive: bool=False):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print(f'___NOT FOUND___{folder}')
        return

    pattern = '**/*' if recursive else '*'
    files = [f for f in folder.glob(pattern) if f.is_file()]

    if not files:
        print('___There are no files in the folder to sort.___')
        return

    for file_path in files:
        ext = file_path.suffix
        category = get_category(ext)
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        new_path = target_dir / file_path.name

        counter = 1
        while new_path.exists():
            new_path = target_dir / f'{file_path.stem}_{counter}{file_path.suffix}'
            counter += 1

        if move:
            shutil.move(str(file_path), str(new_path))
            action = 'Moved'
        else:
            shutil.copy2(str(file_path), str(new_path))
            action = 'Copied'

        print(f'{action}: {file_path.name} - {category}/')
    print('\n Sorting completed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Organizer')
    parser.add_argument('--path', '-p', required=True, help='Folder path for sorting')
    parser.add_argument('--copy', action='store_true', help='Copy files instead of move')
    parser.add_argument('--recursive', '-r', action='store_true', help='Scan subfolders')

    args = parser.parse_args()
    organize_files(args.path, move=not args.copy, recursive=args.recursive)
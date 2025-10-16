import os

def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except Exception:
                pass  # for example, if there is no access
    return total_size


def analyze_folder(root_path, top_n=10):
    folder_sizes = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        folder_sizes[dirpath] = get_folder_size(dirpath)

    # Sort by size (largest to smallest)
    top_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)[:top_n]

    print(f"\nTOP-{top_n} the heaviest folders in '{root_path}':\n")
    for i, (folder, size) in enumerate(top_folders, 1):
        print(f"{i}. {folder} — {size / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    path = input("Enter the path to the folder to be analyzed: ").strip()
    if not os.path.isdir(path):
        print("The specified path does not exist or is not a folder.")
    else:
        analyze_folder(path)

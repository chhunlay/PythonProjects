import os

def count_files_and_directories(path):
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(path):
        file_count += len(files)
        dir_count += len(dirs)

    return file_count, dir_count

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    if os.path.exists(path):
        files, dirs = count_files_and_directories(path)
        print(f"Total files: {files}")
        print(f"Total directories: {dirs}")
    else:
        print("The specified path does not exist.")

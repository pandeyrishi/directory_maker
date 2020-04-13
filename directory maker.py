import os, shutil
extension_direc = {
        "audios": {".mp3", ".m4a", ".wav", ".flac"},   #   more you can add
        "videos": {"mp4", ".mkv", ".MKV", ".flv", ".mpeg"},
        "documents": {".doc", ".pdf", ".txt"},
        "pictures": {".jpg", ".jpeg", ".jfif", ".gif", ".png"},
        "compress": {".rar", ".zip", ".sitx"},
        "applications": {".exe"}
    }
folderpath = input("Enter folder path")

def file_finder(folder_path, file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)

    return files


for extension_name, extension_type in extension_direc.items():
    c = file_finder(folderpath, extension_type)
    if len(c) > 0:
        folder_name = extension_name
        folder_path = os.path.join(folderpath, folder_name)
        os.makedirs(folder_path, exist_ok=True)    # to not show error for same name folders

        for item in file_finder(folderpath, extension_type):
            item_path = os.path.join(folderpath, item)
            item_new_path = os.path.join(folder_path, item)
            shutil.move(item_path, item_new_path)




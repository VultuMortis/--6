import os

def set_working_directory(path):
    if os.path.exists(path) and os.path.isdir(path):
        os.chdir(path)
        print(f"Рабочая директория установлена в: {path}")
    else:
        print("Указанный путь не существует или не является директорией.")

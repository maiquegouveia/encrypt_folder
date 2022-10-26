import os
from cryptography.fernet import Fernet

def getFiles(dir_path):
    paths = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            paths.append(path)
    return paths

def encryptFiles():
    dir_path = input("Enter dir path: ")
    paths = getFiles(dir_path)

    key_file = input("Enter encrypt key file path: ")

    with open(key_file,'rb') as file:
        key = file.read()

    f = Fernet(key)

    for file in paths:
        file_to_encrypt = dir_path + '\\' + file

        with open(file_to_encrypt,'rb') as original_files:
            original = original_files.read()

        encrypted = f.encrypt(original)

        try:
            with open(file_to_encrypt,'wb') as encrypted_files:
                encrypted_files.write(encrypted)
        except:
            pass

encryptFiles()

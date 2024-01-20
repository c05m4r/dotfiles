import os
import re
import shutil
import sys
from itertools import product

def get_paths(root):
    all_paths = list()
    for dirpath, dirnames,filenames in os.walk(root, topdown=False):

        for file in filenames:
            path = f"{os.getcwd()}/{os.path.join(dirpath, file)}" 
            all_paths.append(path)
            
    return all_paths

def normalizer(name):
    new_name = name.lower()
    new_name = new_name.translate(str.maketrans("áéíóú", "aeiou"))
    new_name = new_name.translate(str.maketrans("àèìòù", "aeiou"))
    new_name = re.sub(r"[^0-9a-z_]", "_", new_name)
    return new_name

def renamer(root):
    for old_path in get_paths(root):
        pwd = os.getcwd()
        filepath = old_path.split("/")[-1]
        name, ext = os.path.splitext(filepath)
        new_name = normalizer(name)

        path = old_path[len(pwd):]
        
        path_list = path.split("/")[:-1]
        path_list = map(normalizer, path_list)
        path = "/".join(path_list)
        
        new_path = f"{pwd}{path}/{new_name}{ext}"

        print(old_path)
        print(new_path)
        print(len(old_path) * "=")

        try:
            shutil.copy2(old_path, new_path)
        except FileNotFoundError:
            os.makedirs(f"{pwd}{path}", exist_ok=True)
            shutil.copy2(old_path, new_path)
       
def main():
    path = sys.argv[1]
    renamer(path)
    # shutil.rmtree(path)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python rename.py <path>")
        sys.exit(1)

    main()


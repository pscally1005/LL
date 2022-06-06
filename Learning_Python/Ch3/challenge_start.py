import os, sys
from os import path

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def main(): 
    p = path.realpath("newfile.txt")
    root_dir, tail = path.split(p)
    new_folder = "results"
    new_path = os.path.join(root_dir, new_folder)

    if os.path.exists(new_path) == False:
        os.mkdir(new_path)

    os.chdir(new_path)
    myfile = open("results.txt", "w+")

    contents = os.listdir(root_dir)
    size = get_size(root_dir)
    myfile.write("Total bytecount: " + str(size) + "\n")
    myfile.write("Files list:\n")
    myfile.write("-----------\n")
    for i in contents:
        if i.endswith(".py") or i.endswith('.txt') or i.endswith(".bak"):
            myfile.write(str(i) + "\n")

    myfile.close()


if __name__ == "__main__":
    main()

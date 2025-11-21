import os

path = ".."
# path = r"c:\workspaces\multi01_pytho"

for dir_name, sub_dir_names, file_names in os.walk(path):
    print(dir_name)
    for sub_dir_names in sub_dir_names:
        print(f"\t [d] {sub_dir_names}")
    for file_name in file_names:
        print(f"\t [f] {file_name}")
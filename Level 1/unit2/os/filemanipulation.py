import os
basepath = "C:\Workspace\.vscode\Test_Folder"
fsize = 0
fname = ""
entries = os.scandir(basepath)
for entry in entries:
    if entry.is_file():
        info = entry.stat()
        print(f'{entry.name} {info.st_size}')
        if fsize < info.st_size:
            fsize = info.st_size
            fname = entry.name
print(f"Biggest file in the directory {os.path.abspath(basepath)} is {fname}, with the size {fsize}")
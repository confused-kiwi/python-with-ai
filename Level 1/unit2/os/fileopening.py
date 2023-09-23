doz = open("C:/Workspace/.vscode/unit2/os/thoseleafplayers.txt", "r")
print("'Ooh yeah those Maple Leaves have a lot of players,' said Joe ")
print("'I wonder what will happen if I...'\n")
for line in doz:
    values = line.split()
    print(values[0],values[1], values[2], values[3])   

doz.close()

print("Here will be the contents of the file:")
with open("x-files.txt", "r") as f:
    #inside here the f file is open for reading
    print(f.read())

    #once I am out, the file is closed

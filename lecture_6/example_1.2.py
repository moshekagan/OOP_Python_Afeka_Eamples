is_ok = False

while not is_ok:
    file_path = input("insert file path: ")
    try:
        with open(file_path) as file:
            file.read()
        is_ok = True
    except FileNotFoundError:
        print(f"Couldn't open the file: {file_path}")

print("Done!")

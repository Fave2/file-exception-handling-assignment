def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("\n File Content:\n")
            print(file.read())
    except FileNotFoundError:
        print(f" Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f" Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f" Unexpected error: {e}")

user_filename = input(" Enter the filename you want to read: ")
read_file(user_filename)

def modify_content(text):
    return text[::-1]

try:
    with open("input.txt", "r") as source_file:
        original_content = source_file.read()

    updated_content = modify_content(original_content)

    with open("output.txt", "w") as target_file:
        target_file.write(updated_content)

    print(" Content modified and saved to 'output.txt'.")

except FileNotFoundError:
    print(" 'input.txt' not found. Please check the file name.")
except IOError as e:
    print(f" I/O error occurred: {e}")

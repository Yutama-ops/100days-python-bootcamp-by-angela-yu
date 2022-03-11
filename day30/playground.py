#FileNotFound

try:
    file = open("a_file.txt")
    dict = {"key": "value"}
    print(dict["key"])
except FileNotFoundError:
    file =open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message}doesnt exist")
else:
    content = file.read()
    print("content")
finally:
    file.close()
    print("File was closed.")
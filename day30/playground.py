# #FileNotFound
#
# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file =open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message}doesnt exist")
# else:
#     content = file.read()
#     print("content")
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise KeyError("This an error that i made")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not over 3 meters.")

bmi = weight/height ** 2
print(bmi)
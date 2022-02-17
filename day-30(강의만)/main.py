#FileNotFound

# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     print("no file.")
# except KeyError as error_message:
#     print(f"no {error_message} key.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is error")

#KeyError
# a_dictionary = {"key":"value"}
#   value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)


fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " Pie")
    except:
        print("Fruit pie")

make_pie(6)
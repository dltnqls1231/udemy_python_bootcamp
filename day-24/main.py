# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("C:/Users/dltnq/OneDrive/바탕 화면/new_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents[8:12])

with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

for name in names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter = letter_file.read()
    letter = letter.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/{name.strip()}.txt", "w") as output:
        output.write(letter)


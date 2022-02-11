# numbers = [1,1,2,3,5,8,13,21,34,55]
# # squared_numbers = [num**2 for num in numbers]
# # print(squared_numbers)
#
# # result = [num for num in numbers if num%2 == 0]
# # print(result)
#
# with open("file1.txt") as file1:
#     f1 = file1.readlines()
# with open("file2.txt") as file2:
#     f2 = file2.readlines()
#
# same_num = [int(num) for num in f1 if num in f2]
# # for i in range(len(same_num)):
# #     same_num[i].replace("\n", "")
# #     same_num[i] = int(same_num[i])
#
# print(same_num)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence = sentence.split()
# result = {word:len(word) for word in sentence}
# print(result)

# weather_c = {
#     "Monday":12,
#     "Tuesday":14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday":24,
#
# }
#
# weather_f = {day:c*1.8+32 for day, c in weather_c.items()}
# print(weather_f)
import pandas as pd
# student_dict = {
#     "student":["Angela", "James", "Lily"],
#     "score":[56,76,98],
# }
#
# df_student_dict = pd.DataFrame(student_dict)
# print(df_student_dict)
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row_value.letter:row_value.code for index, row_value in df.iterrows()}
user_word = input("Enter a word: ").upper()
# result = []
# for char in user_word.upper():
#     result.append(nato_dict[char])
# print(result)
result = [nato_dict[char] for char in user_word]
print(result)
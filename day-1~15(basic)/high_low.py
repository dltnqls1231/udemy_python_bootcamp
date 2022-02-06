from art import vs, data
import random


len_data = len(data)
A_index = random.randint(0, len_data - 1)
B_index = random.randint(0, len_data - 1)
indices = []
while A_index == B_index:
    B_index = random.randint(0, len_data - 1)
indices.append(A_index)
indices.append(B_index)
is_correct = True
score = 0


def find_answer(ans, dat, A, B, scr):
    global logo
    if ans == 'A':
        if dat[A]['follower_count'] > dat[B]['follower_count']:
            return True
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {scr}")
            return False
    else:
        if dat[B]['follower_count'] > dat[A]['follower_count']:
            return True
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {scr}")
            return False


while is_correct:
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data[A_index]['name']}, {data[A_index]['description']}, from {data[A_index]['country']}")
    print(f"\n{vs}\n")
    print(f"Compare B: {data[B_index]['name']}, {data[B_index]['description']}, from {data[B_index]['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = find_answer(answer, data, A_index, B_index, score)
    score += 1
    indices.append(A_index)
    indices.append(B_index)
    new_index = random.randint(0, len_data - 1)
    while new_index in indices:
        new_index = random.randint(0, len_data - 1)
    A_index = B_index
    B_index = new_index


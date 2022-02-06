import random
logo = '''PLAY BLACKJACK'''
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def want_play():
    keep = input("Do you want to play BLACKJACK? y or n")
    if keep == 'y':
        return True
    else:
        return False


def get_next_card():
    next_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if next_card == 'y':
        return True
    else:
        return False


def print_sum(your_cards, computer_cards):
    print(f"your cards, sum = {your_cards} {sum(your_cards)}")
    print(f"computer cards, sum = {computer_cards} {sum(computer_cards)}")


while want_play():
    print(logo)
    your_cards = []
    computer_cards = []
    for i in range(2):
        your_cards.append(cards[random.randrange(0, 13)])
        computer_cards.append(cards[random.randrange(0, 13)])
    your_sum = sum(your_cards)
    computer_sum = sum(computer_cards)
    if your_sum > 21 and your_cards.count(11) > 0:
        your_cards[your_cards.index(11)] = 1
        your_sum = sum(your_cards)
    print(f"Your cards: {your_cards}, current score: {your_sum}")
    print(f"Computer's first card: {computer_cards[0]}")

    while get_next_card():
        your_cards.append(cards[random.randrange(0, 13)])
        your_sum = sum(your_cards)
        if your_sum > 21 and your_cards.count(11) > 0:
            your_cards[your_cards.index(11)] = 1
            your_sum = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {your_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
        if your_sum > 21:
            break

    if your_sum > 21:
        print_sum(your_cards, computer_cards)
        print("You went over")
    else:
        while computer_sum < 17:
            computer_cards.append(cards[random.randrange(0, 13)])
            computer_sum = sum(computer_cards)
            if computer_sum > 21 and computer_cards.count(11) > 0:
                computer_cards[computer_cards.index(11)] = 1
        if computer_sum > 21:
            if computer_cards.count(11) > 0:
                computer_cards[computer_cards.index(11)] = 1
            else:
                print_sum(your_cards, computer_cards)
                print("Computer went over")
                print("You Win!")
        elif your_sum == computer_sum:
            print("DRAW")
        else:
            print_sum(your_cards, computer_cards)
            winner = "You" if your_sum > computer_sum else "Computer"
            print(f"{winner} Win!")
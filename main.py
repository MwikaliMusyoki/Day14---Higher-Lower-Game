from art import logo
from art import vs
from game_data import data
import random

print(logo)

answer = True
score = 0
first_index = random.randint(0, len(data))
second_index = random.randint(0, len(data))

while answer == True:
    print(
        f"Compare A: {data[first_index]['name']} a {data[first_index]['description']} from {data[first_index]['country']}")

    print(vs)

    print(
        f"Against B: {data[second_index]['name']} a {data[second_index]['description']} from {data[second_index]['country']}")

    user_choice = input("Who has more followers? Type A or B : ")

    if user_choice == "A":
        if data[first_index]['follower_count'] > data[second_index]['follower_count']:
            answer = True
            score += 1
            print(f"You're right. Current svore: {score}")
            first_index = second_index
            second_index = random.randint(0, len(data))

        else:
            answer = False
            print(f"Ooops you got that wrong. Your final score is:  {score}")

    else:
        if data[second_index]['follower_count'] > data[first_index]['follower_count']:
            answer = True
            score += 1
            print(f"You're right. Current svore: {score}")
            first_index = second_index
            second_index = random.randint(0, len(data))
        else:

            answer = False
            print(f"Ooops you got that wrong. Your final score is:  {score}")

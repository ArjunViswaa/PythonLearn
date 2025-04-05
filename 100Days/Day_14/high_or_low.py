import random
from art import logo, vs
from game_data import data

def check_answer(user_guess, a_followers, b_followers) : 
    if user_guess == 'A' and a_followers > b_followers : 
        return True
    elif user_guess == 'B' and b_followers > a_followers : 
        return True
    else : 
        return False

score = 0
game_should_continue = True
accountB = random.choice(data)

print(logo)

while game_should_continue : 
    accountA = accountB
    accountB = random.choice(data)
    if accountA == accountB : 
        accountB = random.choice(data)

    print(f"Compare A : {accountA["name"]}, a {accountA["description"]}, from {accountA["country"]}")
    print(vs)
    print(f"Compare B : {accountB["name"]}, a {accountB["description"]}, from {accountB["country"]} \n")

    guess = input("Who has more followers ? Type 'A' or 'B'")

    accAFollowers = accountA["follower_count"]
    accBFollowers = accountB["follower_count"]

    is_correct = check_answer(guess, accAFollowers, accBFollowers)

    if is_correct : 
        score += 1
        print(f"You are correct! Current score is {score}")
    else : 
        print("Sorry You got it wrong")
        game_should_continue = False
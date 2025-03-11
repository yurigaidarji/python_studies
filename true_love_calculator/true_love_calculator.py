# The rules are:
# write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.  
# credits to 100-days-of-code from Dr. Angela Yu

def calculate_love_score(name1, name2):
    w_true = "TRUE"
    w_love = "LOVE"

    l_name1 = list(str(name1).upper())
    l_name2 = list(str(name2).upper())
    l_names = l_name1 + l_name2
    p_true = 0
    p_love = 0
    count = 0

    for letter in w_true:
        count = l_names.count(letter)
        print(f"{letter} occurs {count} times")
        if count > 0:
            p_true += count
    print(f"Total = {p_true}")


    for letter in w_love:
        count = l_names.count(letter)
        print(f"{letter} occurs {count} times")
        if count > 0:
            p_love += count

    print(f"Total = {p_love}")

    print(f"Love Score = {p_true}{p_love}")

calculate_love_score("Kanye West", "Kim Kardashian")
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
words = []


def Word_bank():
    user_input = input("Enter a word: ")
    words.append(user_input)
    
    promp = input("Do you want to add another word? y/n : ")
    if promp == "y":
        return Word_bank()
    else:
        for word in words:
            print(word)

Word_bank()
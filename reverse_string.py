def reverse_string(input_string):
    return input_string[::-1]

def main():
    original_word = input("Enter a word or phrase: ")

    reversed_word = reverse_string(original_word)



    print(f"Original Word: {original_word}")
    print(f"Reversed Word: {reversed_word.upper()}")
    print(f"Character Count: {len(original_word)} characters")


    #print(f"{word, reversed}")
if __name__ == "__main__":
    main()

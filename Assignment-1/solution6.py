def take_user_input():
    user_input = raw_input("Enter a long string\n")
    list_of_words_in_user_input = user_input.split(" ")
    print ' '.join(list_of_words_in_user_input[::-1])

take_user_input()
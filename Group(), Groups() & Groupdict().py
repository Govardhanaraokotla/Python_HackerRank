if __name__ == "__main__":
    string = input()
    char_prev = ""
    for char in string:
        if char == char_prev and char.isalnum():
            print(char)
            exit()
        char_prev = char
    print(-1)

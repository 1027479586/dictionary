import itertools

def main():
    words = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp = itertools.permutations(words,8)
    passwords = open("dic.txt","a")


    for i in temp:
        passwords.write("".join(i))
        passwords.write("".join("\n"))
    passwords.close()
    pass


if __name__ == '__main__':
    main()
def tiggerfy(word):
    substrings = ['t', 'i', 'gg', 'er']
    for sub in substrings:
        if sub in word or sub.upper() in word:
            word = word.replace(sub,'')
            word = word.replace(sub.upper() ,'')
    return word


def main():
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))

main()
def words(word):
    wordcount={}

    if "\n" in word:
        wordlist = word.splitlines()
    else:
        wordlist = word.split()

    print("\nworld list after splitting ", wordlist,"\n")

    for i_word in wordlist:
        try:
            key=int(i_word)
            wordcount[key] = wordlist.count(i_word)

        except ValueError:
            wordcount[i_word] = wordlist.count(i_word)


    return wordcount




print("from the My function ",words('testing 1 2 testing'))
print("from the Tests       ",{'testing': 2, 1: 1, 2: 1})
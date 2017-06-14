def words(word):
    wordcount={}

    if "\n" in word:
        wordlist = word.splitlines()
    else:
        wordlist = word.split()

    print("\n\nworld list after splitting ", wordlist,"\n\n")

    for i_word in wordlist:
        if type(i_word)== int:
            wordcount[int(i_word)] = word.count(i_word)
        else:
            wordcount[i_word]=word.count(i_word)


    return wordcount



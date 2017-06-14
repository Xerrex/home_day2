def words(word):
    wordcount={}

    if "\n" in word:
        wordlist = word.splitlines()
    else:
        wordlist = word.split()

    print("\n\nworld list after splitting ", wordlist,"\n\n")

    for i_word in wordlist:
        wordcount[i_word]=wordlist.count(i_word)

    return wordcount



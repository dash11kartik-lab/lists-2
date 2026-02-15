def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len[word] > 3 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        
    print("List the words with the first and last letters as the same\n", lst)
    return ctr
count=match_words(['abc','cfc','xyz','aba', '1221'])
print("Number of words having the same first and last letters:", count)
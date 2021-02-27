def expressiveWords(S, words):
    count = 0
    for word in words:
        pt1 = 0
        pt2 = 0
        tmp1 = 0
        tmp2 = 0
        while pt1 < len(S) and pt2 < len(word):
            while pt2+1 < len(word) and word[pt2] == word[pt2+1]:
                tmp2 += 1
                pt2 += 1
            while pt1+1 < len(S) and S[pt1] == S[pt1+1]:
                tmp1 += 1
                pt2 += 1
            if S[pt1] == word[pt2]:
                if tmp1 == tmp2 or tmp1 >= 3*tmp2:
                    pt1 += 1
                    pt2 += 1
                if pt1 == len(S)-1 and pt2 == len(word)-1:
                    count += 1
                tmp1 = 0
                tmp2 = 0
            else:
                break
                
    return count
                    
S = "heeellooo"
words = ["hello", "hi", "helo"]
print(expressiveWords(S, words))
                
                    
class Solution:
    def reorderLogFiles(self, logs):

        # O[NlogN] Time
        # O[2N] Space 

        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)


                # The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
        # letters = ['let2 own kit dig', 'let1 art zzz', 'let3 art aaa']
                
        letters.sort(key = lambda x: x.split()[0])            #when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])           #sort by suffix
        
        result = letters + digits                                        #put digit logs after letter logs
        return result























# letters = ['let2 own kit dig', 'let1 art zero', 'let3 art one']

# letters.sort(key = lambda x: x.split()[1])
# print(letters)

# letters.sort(key = lambda x: x.split()[1:])
# print(letters)




# letters = ['let2 c kit dig', 'let3 b zero', 'let1 a can']
# letters.sort(key = lambda x: x.split()[1])

# print(letters)



    # print(letter, letter.split()[1:])
# letters.sort(key= lambda x: x.split()[1])
# print(letters)



    

        
                
        
    
                
                
                
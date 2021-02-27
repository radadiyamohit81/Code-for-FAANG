
# 2 STACKS Approach 
# 4 CASES: 
    # string[i].isdigit() 
    # string[i].isalpha()
    # string[i] == '['
    # string[i] == ']'

# time : O(N)
# space : O(N)

class Solution:
    def decodeString(self, s: str) -> str:
        numStack, stringStack = [], []
        currentNum, currentSt = 0, ''
        
        for ch in s:
            if ch.isdigit():
                currentNum = currentNum*10 + int(ch)
            elif ch == '[':
                numStack.append(currentNum)
                stringStack.append(currentSt)
                currentNum, currentSt = 0, ''         # reset num, st
            elif ch == ']':                           # compute the result string so far from the stored and times and character and the present []
                times = numStack.pop()
                newSt = times*currentSt
                currentSt = stringStack.pop()
                currentSt += newSt
            else:
                currentSt += ch
        return currentSt
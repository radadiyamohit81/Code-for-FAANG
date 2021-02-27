class Solution:
    def basicCalcultor2(self, s):
        if s == '':
            return 0
        
        result = 0
        lastNum = 0
        lastOperation = '+'
        curNum = 0
        for i in range(len(s)):
            if s[i].isdigit():
                curNum = curNum*10 + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:
                if lastOperation == '+':
                    result += lastNum
                    lastNum = +curNum
                elif lastOperation == '-':
                    result += lastNum
                    lastNum = -curNum
                elif lastOperation == '*':
                    lastNum = lastNum * curNum
                elif lastOperation == '/':
                    lastNum = int(lastNum / curNum)
                lastOperation = s[i]
                curNum = 0
        result += lastNum
        return result
                
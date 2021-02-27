class Solution:
    # OPTIMIZED
    # Time Complexity : O(n) where n is the length of the string
    # Space Complexity : O(n) for the stack
    def decodeString(self, s: str) -> str:
        if s == '':
            return ''
        
        st = []
        curNum = 0
        curStr = ''
        for ch in s:
            if ch == '[':
                st.append(curNum)
                st.append(curStr)
                curNum, curStr = 0, ''
            elif ch == ']':
                lastStr = st.pop()
                lastNum = st.pop()
                curStr = lastStr + (lastNum * curStr)
            elif ch.isdigit():
                curNum = curNum*10 + int(ch)
            elif ch.isalpha():    
                curStr += ch
        return curStr
    
        
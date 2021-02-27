
# STACK approach
# time : O(N)
# space : O(N)
# runs on leetcode: yes

class Solution:
    def isValid(self, s):
        if s == '':
            return True
        if len(s) % 2 != 0:
            return False
        
        st = []
        for ch in s:
            if ch == '[':
                st.append(']')
            elif ch == '(':
                st.append(')')
            elif ch == '{':
                st.append('}')
            else:
                if st != [] and st.pop() == ch:
                    continue
                return False
            
        if st == []:
            return True
        return False      

    def isValid(self, s):
        if s == '' or len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        
        st = []
        opens = '([{'
        closers =')]}'

        for symbol in s:
            if symbol in opens:
                ind = opens.index(symbol)
                st.append(closers[ind])
            else:
                if st == []:
                    return False
                top = st.pop()
                if top != symbol:
                    return False
                
        if st != []:
            return False
        return True                  
        

        
obj = Solution()
print(obj.isValid(s='({'))
print(obj.isValid(s='({})'))
print(obj.isValid(s='({]}'))
print(obj.isValid(s='({[]})'))

            

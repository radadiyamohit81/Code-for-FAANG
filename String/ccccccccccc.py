class Solution:
    def candyCrush(self, s):
        st = []
        ans = ''
        i =0

        while i < len(s):
            if st == []:
                st.append((s[i], 1))
                print("At i == ", i, "Stack is ", st)
                i += 1
                continue

            a, b = st.pop()
            if a == s[i]:  
                while i < len(s) and s[i] == a :
                    b += 1
                    i += 1      
                if b >2:
                    continue
                st.append((a, b))
                print("At i == ", i, "Stack is ", st)
            else:
                st.append((a, b))
                st.append((s[i], 1))
                print("At i == ", i, "Stack is ", st)
                i += 1
        
        print("Stack looks like: ",st)
        while st != []:    
            a, b = st.pop(0)
            for i in range(b):
                ans += a

        print('\n')
        return ans         

obj = Solution()
print(obj.candyCrush(s='aabbacc'))
                


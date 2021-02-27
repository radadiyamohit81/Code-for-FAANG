class Solution:
    def calculate(self, s):
        if not s:
            return 0

        lastSign = '+'
        num = 0
        st = []

        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])

            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:
                if lastSign == '+':
                    st.append(num)
                if lastSign == '-':
                    st.append(-num) 
                if lastSign == '*':
                    lastVal = st.pop()
                    st.append(lastVal * num)
                if lastSign == '/':
                    lastVal = st.pop()
                    st.append(int(lastVal / num))
                lastSign = s[i]
                num = 0
            print("lastSign becomes: ", lastSign, "num becomes: ",num, "stack becomes ",st, "\n")

        print('\nres st', st)
        res = 0
        while st:
            res += st.pop()
        return res             

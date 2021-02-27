class Solution:
    def calculate(self, s):
        res = 0
        st = []
        num = 0
        sign = +1

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '+':
                res += sign*num
                sign = +1
                num = 0
            elif ch == '-':
                res += sign*num
                sign = -1
                num = 0
            elif ch == '(':
                st.append(res)
                st.append(sign)
                sign = +1
                res = 0
                num = 0
            elif ch == ')':
                res += sign*num
                res *= st.pop()
                res += st.pop()
                sign = +1
                num = 0
        return res + (sign*num)


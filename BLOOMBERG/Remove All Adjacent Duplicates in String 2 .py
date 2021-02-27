# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s 
# and removing them causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed that the answer is unique.

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

class Solution:
    def removeDuplicates(self, s, k):
        
        st = []
        for ch in s:
            if st == []:
                st.append([ch, 1])
            else:
                print(st[-1][0])
                if st[-1][0] == ch:
                    ch, count = st.pop()
                    count += 1
                    if count == k:
                        continue
                    st.append([ch, count])
                else:
                    st.append([ch, 1])
        
        print(st)
        res = ''
        while st != []:
            ch, count = st.pop()
            res = ch * count + res
        return res
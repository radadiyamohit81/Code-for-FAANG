class Solution:
    def minWindow(self, s, t):
        if s == '' or t == '':
            return ''
        
        # 1) Maintain a COUNTER of all characters of t
        d = {}
        for ch in t:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1 
        required_match = len(d)
        
        # 2) BUILD SUB-STRING WINDOW COUNTER 
        substr_Window_count = {}
        match = 0
        ans = (float('inf'), None, None)
        right, left = 0, 0
        while right < len(s):
            # ADD THE INCOMING CHARACTER TO SUB-STRING WINDOW COUNTER
            if s[right] not in substr_Window_count:
                substr_Window_count[s[right]] = 1
            else:
                substr_Window_count[s[right]] += 1
                
            if s[right] in d and substr_Window_count[s[right]] == d[s[right]]:
                match += 1
                
            # 3) CHECKING MATCH & UPDATING THE LENGTH & FORMING OTHER SUB-STRING WINDOWS
            while left <= right and match == required_match:
                if right+1 -left < ans[0]:
                    ans = (right+1-left, left, right)
                
                # MOVING THE LEFT POINTER TO TRY OTHER WINDOW COMBINATIONS
                substr_Window_count[s[left]] -= 1
                if s[left] in d and s[left] in substr_Window_count and substr_Window_count[s[left]] < d[s[left]]:
                    match -= 1
                left += 1
                
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]
                
                    
        
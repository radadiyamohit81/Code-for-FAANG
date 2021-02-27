class Solution:
    def expand(self, S: str) -> List[str]:
        self.result = []
        
        # Build blocks 
        i =0
        blocks = []
        while i < (len(S)):
            block = []
            if S[i] == '{':
                i += 1
                while S[i] != '}':
                    if S[i] != ',':
                        block.append(S[i])
                    i += 1
            else:
                block.append(S[i])
                
            i += 1    
            blocks.append(block)
        
        self.dfs(blocks, 0, '')
        self.result.sort()
        
        return self.result
    
    def dfs(self, blocks, index, s):

        # Base case
        if index == len(blocks):
            self.result.append(s[::])
            return
        
        # Logic
        for i in blocks[index]:
            # Action
            s += i
            # Recurse
            self.dfs(blocks, index+1, s)

            # Backtrack to find the other combinations
            s = s[:-1]
                
                

class Solution:
    def __init__(self):
        # HashMap: {col_name:[[cell_num, value]],,,}
        self.d = {}

    def update(self, cellKey, value):
        # get column and row number,
        col = ''
        row = ''
        for i in cellKey:
            if i.isalpha():
                col += i
            else:
                row += i
        if col not in self.d:
            self.d[col] = []
            self.d[col].append([row, value])
        else:
            self.d[col].append([row, value])

    def getAllCellValues(self):
        result = []
        for col in self.d:
            for entries in self.d[col]:
                result.append(entries[1])
        return result


    def getCellValue(self, cellKey):
        col = ''
        row = ''
        for i in cellKey:
            if i.isalpha():
                col += i
            else:
                row += i
        entries = self.d[col]
        for entry in entries:
            if entry[0] == row:
                # print(entry[1])
                return entry[1]

obj = Solution()
print(obj.update('A1', 3))
print(obj.update('A2', 5))
print(obj.getAllCellValues())
print(obj.getCellValue('A2'))

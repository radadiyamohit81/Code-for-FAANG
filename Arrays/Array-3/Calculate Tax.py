
class Solution:
    def calculateTax(self, taxBracketLevels, salary):
        previouslyTaxedBracket = 0
        tax = 0

        i = 0
        while salary > 0:
            if taxBracketLevels[i][0] == None:
                tax += salary * taxBracketLevels[i][1]
                return tax

            taxableAmount = min( taxBracketLevels[i][0] - previouslyTaxedBracket, salary )
            salary -= taxableAmount
            tax += taxableAmount * taxBracketLevels[i][1]
            previouslyTaxedBracket = taxBracketLevels[i][0]
            i += 1
        return tax

obj = Solution()
print(obj.calculateTax(taxBracketLevels=[[10000, 0.1], [20000, 0.2], [30000, 0.3], [None, 0.4]], salary=45000))
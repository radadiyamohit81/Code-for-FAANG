# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

# Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

# Sample input:

# user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]


# user2 = ["a", "/one", "/two"]
# user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
# user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
# user5 = ["a"]
# user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

# Sample output:

# findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
# findContiguousHistory(user0, user2) => [] (empty)
# findContiguousHistory(user2, user1) => ["a"] 
# findContiguousHistory(user5, user2) => ["a"]
# findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
# findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

# n: length of the first user's browsing history
# m: length of the second user's browsing history


domainList = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


test_output =[]

# mail.yahoo.com, yahoo.com, com

class Solution:
    def domainCount(self, domainList):
        
        result = {}
        for domain in domainList:
            hits = domain.split(',')[0]
            domain = domain.split(',')[1]
            subDomains_lst = domain.split('.')
            l = len(subDomains_lst)
            
                
            # Find all possible SubDomains, and their count
            for i in range(l):
                subDomain = subDomains_lst[i:]
                stringg = ''
                for elem in subDomain:
                    stringg += "."+elem
                
                stringg = stringg.lstrip('.')
                if stringg not in result:
                    result[stringg] = int(hits)
                else:
                    result[stringg] += int(hits)
            
                    
        return result
                
                
obj = Solution()
print(obj.domainCount(domainList = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]))
                
                    
                
            

def matchUrlPath(user1, user2):
    if user1 == [] or user2 == []:
        return []
    
    result = []
    maxString = ''
    for i in range(len(user1)):
        for j in range(len(user2)):
            stringg = ''
            while i < len(user1) and j < len(user2):
                if user1[i] == user2[i]:  # match found
                    stringg += user1[i]
                    i += 1
                    j += 1
                break
    return stringg
            
    
            
            
                
    
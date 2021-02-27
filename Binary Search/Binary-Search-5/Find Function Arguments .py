def f(x, y):
    return x**2 +y
    #blackbox

# N = Natural numbers, all positive integers starting from 1

def find_all_pairs(z):
    ans = []
    for x in range(1, z + 1):
        low, high = 1, z
        while low <= high:
            y = mid = (low + high) // 2
            if f(x, y) == z:
                ans.append([x, y])
                break
            elif f(x, y) > z:
                high = mid -1
            else:
                low = mid + 1
    return ans


def find_all_pairs(z):
    result = []

    for x in range(1, z+1):
        if z - x*x > 0:
            result.append([x, z-(x*x)])
        if z - x*x <= 0:
            return result

print(find_all_pairs(50)) 
#ANS: [[1, 49], [2, 46], [3, 41], [4, 34], [5, 25], [6, 14], [7, 1]]

import sys

from dict_ref import dref




def solve(letters, center):
    if len(letters) != 7 or len(set(letters)) != 7:
        return "didn't enter 7 unique characters for surrounding letters"
    if len(center) != 1:
        return "didn't enter 1 character for center letter"
    if center not in letters:
        return "center letter not a part of overall letters"
    
    letters = ''.join(sorted(letters))

    lset = set(letters)

    ans = []

    with open("dict_short.txt", "r") as dr:
        for line in dr:
            line = line.strip()
            if (set(line).issubset(lset) and center in line):
                ans.append(line)

    #print(len(ans))
    return ans
    
    #with open "dict_short.txt" as d:

if __name__ == "__main__":
    l = sys.argv[1]
    c = sys.argv[2]
    print(solve(l, c))
    

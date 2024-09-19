def permute_unique(s):
    def backtrack(start):
        if start == len(s):
            result.add("".join(s))
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]

    result = set()
    s = list(s)
    backtrack(0)
    return list(result)

s = "AAB"
print(permute_unique(s))

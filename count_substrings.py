def count_substrings_with_k_distinct(s, k):
    from collections import defaultdict

    n = len(s)
    count = 0
    left = 0
    char_count = defaultdict(int)
    distinct_count = 0

    for right in range(n):
        char_count[s[right]] += 1
        if char_count[s[right]] == 1:
            distinct_count += 1

        while distinct_count > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                distinct_count -= 1
            left += 1

        if distinct_count == k:
            count += right - left + 1

    return count

s = "abcba"
k = 2
print(count_substrings_with_k_distinct(s, k)) 

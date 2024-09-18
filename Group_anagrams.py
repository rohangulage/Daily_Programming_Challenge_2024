def group_anagrams(strs):



  anagrams = {}

  for str in strs :

    sorted_str = ''.join(sorted(str))

    if sorted_str not in anagrams:

      anagrams[sorted_str] = []

    anagrams[sorted_str].append(str)



  return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "bat", "nat"]

result = group_anagrams(strs)

print(result)
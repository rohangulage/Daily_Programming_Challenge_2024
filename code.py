def reverse_string_word_by_word(s):
    
 


    words = s.split()

    
    words.reverse()
    reversed_string = " ".join(words)

    reversed_string = reversed_string.strip()

    return reversed_string

s = "  This is a test string.   "
reversed_string = reverse_string_word_by_word(s)
print(reversed_string)
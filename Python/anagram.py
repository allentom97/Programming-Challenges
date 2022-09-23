def is_anagram(string1, string2):
    array1 = list(string1)
    array2 = list(string2)

    array1.sort()
    array2.sort()

    if array1 == array2:
        return True
    else:
        return False
        
print(is_anagram("typhoon", "opython"))

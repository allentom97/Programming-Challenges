'''
dictionary = {
    "name": "Thomas",
    "age": 24,
    "occupation": "Teacher",
    "adult": True
}

print(dictionary)

#dictionary.update({"name": "Tom", "occupation": "Software Engineer"})
dictionary["fav_food"] = "Pizza"
print(dictionary)
'''

def palindrome(string):
    string_rev = string[::-1]

    if string == string_rev:
        return True
    else:
        return False
    
print(palindrome("abba"))

list = "Thomas".split()
reversed = list.reverse()

print(list == reversed)





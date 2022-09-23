def validate(code_string):
    if code_string.find("def") == -1:
        return "missing def"
    elif code_string.find(":") == -1:
        return "missing :"
    elif code_string.find("(") == -1 or code_string.find(")") == -1:
        return "missing paren"
    elif code_string.find("()") == "()":
        return "missing param"
    elif code_string.find("    ") == -1:
        return "missing indent"
    elif code_string.find("validate") == -1:
        return "wrong name"
    elif code_string.find("return") == -1:
        return "missing return"
    else:
        return True
        
print(validate('''def validate(code_string):
    if code_string.find("def") == -1:
        return "missing def"
    elif code_string.find(":") == -1:
        return "missing :"
    elif code_string.find("(") == -1 or code_string.find(")") == -1:
        return "missing paren"
    elif code_string.find("()") == "()":
        return "missing param"
    elif code_string.find("    ") == -1:
        return "missing indent"
    elif code_string.find("validate") == -1:
        return "wrong name"
    elif code_string.find("return") == -1:
        return "missing return"
    else:
        return True'''))
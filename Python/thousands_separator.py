def format_number(num):
    num_string = str(num)
    output_string = ""
    while num / 1000 >= 1:
        output_string = "," + num_string[-3:] + output_string
        num_string = num_string[:-3]
        num = num / 1000
    
    output_string = num_string + output_string
    
    return output_string
    
print(format_number(1203224))


    
#Create a function that will take a string as an input and return the 1st non-unique
#letter of a string
#Google -> "l"
#Amazon -> "m"
#if there are no unique letter, return an empty string "xoxoxo" -> ""

def unique_string(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    for l in string:
        if string.count(l) == 1:
            return l
        return ""
print(unique_string('mission college'))

def unique_letter_optimal(string:str):
    if not string:
        raise ValueError
    string = string.lower()
    d = {}
    #google
    for l in string:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for k,v in d.items():
        if v == 1:
            return k
    return ""
print(unique_letter_optimal("mission college"))
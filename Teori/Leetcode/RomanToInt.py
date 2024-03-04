def romanToInt(s):
    k = 0
    dict1 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    dict2 = {
        'CM': -200,
        'XC': -20,
        'IV': -2,
    }
    for i in s :
        k += dict1[i]
    for i in dict2 :
        if i in s :
            k += dict2[i]
    return k
def intToRoman(num):
    try:
        val = int(num)
    except ValueError:
        print("not supported input")
        return "not supported input"
    if int(num) != num:
        print("not supported input")
        return "not supported input"
    count = 0
    o =[]
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    for n in d.keys():
        while num >= n:
            num = num - n
            o.append(d[n])
    print(''.join(o))
    return (''.join(o))
if __name__ == '__main__':
    intToRoman(2)
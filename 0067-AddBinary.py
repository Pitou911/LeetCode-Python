#input a = "11"(3) , b = "1"(1)
#output result = "100"(4)
# def addBinary(a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         #convert both to integer
#         aBin, bBin = int(a,2), int(b,2)
#         #sum the integer
#         sumDe = aBin + bBin
#         #convert it back to decimal
#         result = bin(sumDe).replace("0b","")
#         return result

#second method
def addBinary(a, b):
    res = ""
    carry = 0
    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0
        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2
    if carry:
        res = "1" + res
    return res

print(addBinary("11","1"))
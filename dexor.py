values = [198,202,213,207,203,205,204,222,204,205,215,193,157,208,197,196,221,198,254,234,230,253]
indexValue = 4366
finalString = ""
for i, element in enumerate(values):
    finalString += chr(( element ^ indexValue ^ 170) & 0xFF)
    indexValue = indexValue + 1
print("Last string => " + finalString)
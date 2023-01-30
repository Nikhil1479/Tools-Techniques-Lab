def performSliceWithoutStep(str1):
    print(f"Slice 1 on str1: {str1[5:]}")

    str = slice(0,12)
    print(f"Slice 2 on str1: {str1[str]}")

    str = slice(2,10)
    print(f"Slice 3 on str1: {str1[str]}")

    str = slice(5, 8)
    print(f"Slice 4 on str1: {str1[str]}")

    print(f"Slice 5 on str1: {str1[9:15]}")

def performSliceWithStep(str1):
    print(f"Slice Step 1 on str1: {str1[0:12:2]}")

    str = slice(0,12,2)
    print(f"Slice Step 2 on str1: {str1[str]}")

    print(f"Slice Step 3 on str 1: {str1[5,15,4]}")

    print(f"Slice Step 4 on str 1: {str1[2,16,5,]}")
    
    print(f"Slice Step 4 on str 1: {str1[5,10,5,]}")

name = input("What is your name ?")

str1 = "My name is " + name

print(str1)

print(f"No. of characters are {len(str1)}")

print(f"str1 to UPPERCASE: {str1.upper()}")

print(f"str1 in lowercase: {str1.lower()}")

print(f"Split Operation on str1: {str1.split(' ')}")

print(f"Split by setting delimiter 'a': {str1.split('a')}")

# performSliceWithoutStep(str1)
# performSliceWithStep(str1)

print(f"str1 in reverse: {str1[::-1]}")

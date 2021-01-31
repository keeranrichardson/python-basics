# using recursion as iteration
def hello(start, numberLeftToPrint):
    if numberLeftToPrint < 0:
        return
    print("hello",start)
    hello(start+1, numberLeftToPrint-1)

hello(10, 66)

# calculate number to some power using recursion
def power(num, powe):
    if powe == 0:
        return 1
    return num*power(num, powe-1)

print(power(10, 10))
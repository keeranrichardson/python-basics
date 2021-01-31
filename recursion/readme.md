## Recursion

Recursion is when a function calls itself.

It is important that a recursive function doesnt run forever.

So to stop it running forever we return a value.

### Bad example

The following code is an example of a bad recursive function.

```
def hello(x=1):
    print("hello",x)
    hello(x+1)
```

The code above:

- The hello function takes `x` as an argument.
- If no value for `x` is provided then `x=1`.
- The function prints `hello` with the current value of `x`.
- The funtion calls itself with an incremented value of `x`. ie `x+1`.

Because this runs infinitely, this is a bad example of recursion.

### Improving this

We can improve this by passing in a number of `hello`s to print.

```
def hello(start, numberLeftToPrint):
    if numberLeftToPrint < 0:
        return
    print("hello",start)
    hello(start+1, numberLeftToPrint-1)
```

This is an example of using recursion as an alternative for iteration.

Normally recursion is used as a simpler way to solve problems.

### Solving a problem with recursion

To calculate a number to the power of a number we can multiply it by itself the amount of times we want to calculate the power of. eg. to calculate 10^10 we would `10*10*10*10*10*10*10*10*10*10`

```
def power(num, powe):
    if powe == 0:
        return 1
    return num*power(num, powe-1)
```

- The code above is a recursive function that implements an algorithm to calculate the power of something.
- Anything to the power of 0 is 1 so the first `if` statement represents this condition.
- The recursive multiplies the number by itself until we reach the power of zero. ie. `10*(10*(10*(10*(10*(10*(10*(10*(10*(10*1)))))))))`

### Increasing the recursion call stack

If we have an algorithm that requires more recursion than the call stack allows then we can change the call stack in python using `sys.setrecursionlimit` eg. `sys.setrecursionlimit(1500)`
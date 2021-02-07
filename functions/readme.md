## Functions

A function is a named block of code that can be called at any time and returns a value.

```
def hello():
    return "hello"
```

The function `hello`:

- this function takes no arguments.
- returns the string: `"hello"`.

e.g.

```
assert hello()=="hello"
```

### Calling a function with arguments

```
def squared(value):
    result=value*value
    return result
```

This function takes an argument and returns a calculation result. The calculation squares the value given to the function.

I didn't need to assign the calculation to a result variable but I did to make it more readable and easier to maintain.

e.g.

```
assert squared(3)==9
assert squared(4)==16
```

If we call `squared` without passing in a value, it will trigger a syntax error.

### Default function arguments

We can set default values for arguments in case we dont supply a value.

```
def greet(name="there"):
    return "Hello "+name
```

e.g.

```
assert "Hello Bob" == greet("Bob")
assert "Hello there" == greet()
```

### Function scope

A function only knows about variables that are passed into the function or are declared as variables inside the function itself.

This helps avoid side effects where changing one thing in your code impacts something else.

e.g.

```
lives=3

def life_lost():
    print("You have lost a life")
    global lives
    lives -= 1
    print("You now have ", lives, " lives left")

life_lost()
assert lives==2
```

The above function, `life_lost` has the side effect that the value of the variable `lives` outside the function got changed.

Here is a safer approach that avoids side effects.

```
def livesLost(lives):
    print("You have lost a life")
    lives -=1
    print("You now have ", lives, " lives left")
    return lives

lives=livesLost(lives)
assert lives==1
```

This function avoids side effects because it doesnt access anything outside its scope. In order to change the value of `lives` outside the scope we have to assign it the value of `lives` returned from the function.

### Multiple parameters

Functions can take multiple parameters.

e.g.

```
def volume(width, height, depth):
    volume=width*height*depth
    return volume

assert volume(3, 4, 5) == 60
```


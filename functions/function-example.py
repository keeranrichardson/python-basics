def hello():
    return "hello"

assert hello()=="hello"

def squared(value):
    result=value*value
    return result

assert squared(3)==9
assert squared(4)==16

def greet(name="there"):
    return "Hello "+name
    
assert "Hello Bob" == greet("Bob")
assert "Hello there" == greet()

lives=3

def life_lost():
    print("You have lost a life")
    global lives
    lives -= 1
    print("You now have ", lives, " lives left")

life_lost()
assert lives==2

def livesLost(lives):
    print("You have lost a life")
    lives -=1
    print("You now have ", lives, " lives left")
    return lives

livesLost(lives)
assert lives==2

lives=livesLost(lives)
assert lives==1

def volume(width, height, depth):
    volume=width*height*depth
    return volume

assert volume(3, 4, 5) == 60
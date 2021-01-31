# this is a bad example of recursion 
# it runs until the maximum recursion depth exceeded
def hello(x=1):
    print("hello",x)
    hello(x+1)
hello()
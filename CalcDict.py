#This file reviews the built-in functions of Python
#In order to supply a permissive environment for all of the built-in functions a dictionary will be created.
#Built-in functions A: abs(), aiter(), all(), any(), anext(), ascii()
#Built-in functions B: bin(), bool(), breakpoint(), bytearray(), bytes()
#Built-in functions C: callable(), chr(), classmethod(), compile(), complex()
#Built-in functions D: delattr(), dict(), dir(), divmod()
#Built-in functions E: enumerate(), eval(), exec()
#Built-in functions F: filter(), float(), format(), frozenset()
#Built-in functions G: getattr(), globals()
#Built-in functions H: hasattr(), hash(), help(), hex()
#Built-in functions I: id(), input(), int(), isinstance(), issubclass(), iter()
#Built-in functions L: len(), list(), locals()
#Built-in functions M: map(), max(), memoryview(), min()
#Built-in functions N: next()
#Built-in functions O: object(), oct(), open(), ord()
#Built-in functions P: pow(), print(), property()
#Built-in functions R: range(), repr(), reversed(), round()
#Built-in functions S: set(), setattr(), slice(), sorted(), staticmethod(), str(), sum(), super()
#Built-in functions T: tuple(), type(+)   
#Built-in functions V: vars()
#Built-in functions Z: zip()
import string


def dictionary(x, y, z, t):
    '''This function is built for studying built-in functions and returns many values with different types:
    1: Returns mathematical results when two numbers (x,y) a math operator(z) and a mod(t="c") are entered as arguments
    2: Returns ASCII calculations as lists when two lists (x,y) a math operator(z) and a mod(t="a") are entered as arguments
    3:
    4:
    '''
    if t == "c" and (type(x) == int and type(y) == int) or (type(x) == float and type(y) == float):
        if z == "+":
            return(x + y)
        elif z == "-":
            return(x - y)
        elif z == "*":
            return(x * y)
        elif z == "/":
            return(x / y)
        elif z == "**":
            return(x ** y)
        else:
            return("invalid")
    if t == "a" and (type(x) == str and type(y) == str):
        if z == "+":
            return chr(ord(x) + ord(y))
        elif z == "-":
            return chr((ord(x) - ord(y)))
        elif z == "*":
            return chr((ord(x) * ord(y)))
        elif z == "/":
            return chr((ord(x) / ord(y)))
        elif z == "**":
            return chr((ord(x) ** ord(y)))
        else:
            return ("invalid")
        
        
print("integer calculation: ", dictionary(3, 4, "+", "c"))
print("float calculation: ", dictionary(3.14, 3.14, "+", "c"))
print("ASCII calculation: ", dictionary("f", "r", "+", "a"))
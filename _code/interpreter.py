from textx import metamodel_from_file
from textx.export import metamodel_export, model_export

kryptoskript_mm = metamodel_from_file('FILE_PATH_HERE') # filepath to krypto_skript.tx
kryptoskript_model = kryptoskript_mm.model_from_file('FILE_PATH_HERE') # filepath to program.ks or any kryptoskript program

class KryptoSkript:
    def __init__(self):
        self.model = kryptoskript_model
        self.varmap = {}  # stores variables
        self.alphabet = {chr(i + 96): i for i in range(1, 26)} # store alphabet
        self.calphabet = {chr(i + 64): i for i in range(1, 26)}
        self.alphabet.update(self.calphabet)
        self.alphabet[" "] = "27"
        self.alphabet["'"] = "28"
        self.loop = False

    def math(*expression):
        com = expression[0]
        if(com.sum):
            return com.sum.left + com.sum.right
        else:
            return 1
    
    def interpret(self, *commands):
        if self.loop == False:
            commands = self.model.commands
        else:
            commands = commands[0]
        for c in commands:
            if(c.__class__.__name__ == "Assignment"): # assignment command
                self.varmap.update({c.var: c.value})
            if(c.__class__.__name__ == "Print"): # print command
                if(c.var):
                    print(self.varmap.get(c.var))
                elif(c.str):
                    print(c.str)
            if(c.__class__.__name__ == "Loop"): # for loop
                self.loop = True
                for x in range(0, self.varmap.get(c.var)):
                    self.interpret(c.commands)
                self.loop = False
            if(c.__class__.__name__ == "Condition"): # condition statement
                if c.left == c.right:
                    self.interpret(c.commands)
            if(c.__class__.__name__ == "EncryptCommand"):
                if(c.algorithm.caesar):
                    for c in c.text:
                        new = (int)(self.alphabet.get(c)) + 4
                        print(new, end=' ')
                    print()
            if(c.__class__.__name__ == "Fizzbuzz"):
                for x in range(1, c.loop + 1):
                    if(x % c.left == 0 and x % c.right == 0):
                        print("FizzBuzz")
                    elif(x % c.left == 0):
                        print("Fizz")
                    elif(x % c.right == 0):
                        print("Buzz")
                    else:
                        print(x)

def main():
    krypto = KryptoSkript()
    krypto.interpret()
main()

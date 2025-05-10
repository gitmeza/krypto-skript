from textx import metamodel_from_file
from textx.export import metamodel_export, model_export

kryptoskript_mm = metamodel_from_file('/Users/nathan/Desktop/textX/krypto_skript/krypto_skript.tx')
kryptoskript_model = kryptoskript_mm.model_from_file('/Users/nathan/Desktop/textX/krypto_skript/program.ks')

class KryptoSkript:
    def __init__(self):
        self.model = kryptoskript_model
        self.varmap = {}  # stores variables
        self.loop = False

    def math(self, *expression):
        com = expression[0]
        if(com.sum):
            return com.sum.left + com.sum.right
        else:
            return 1
        
    def caesar_cipher(self, shift, text, decrypt=False, var=False):
        result = ""
        if var == True:
            text = self.varmap.get(text)
        if decrypt == True:
            shift = -shift
        for char in text:
            if char.isalpha():
                if char.isupper():
                    base = ord('A') 
                else: 
                    base = ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                result += chr(shifted)
            else:
                result += char
        return result
    
    def vigenere_cipher(self, key, text, decrypt=False, var=False):
        key = key.lower()
        keyindex = 0
        result = ''
        if var == True:
            text = self.varmap.get(text)
        for char in text:
            if char.isalpha():
                keychar = ord(key[keyindex % len(key)]) - ord('a')
                if decrypt == True:
                    keychar = -keychar
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                shift = (ord(char) - base + keychar) % 26 + base
                result += chr(shift)
                keyindex += 1
            else:
                result += char
        return result
    
    def encryption_parser(self, encryption):
        if(encryption.algorithm.caesar):
            if(encryption.var):
                new = self.caesar_cipher(encryption.algorithm.caesar.key, encryption.var, var = True)
                return new
            else:
                new = self.caesar_cipher(encryption.algorithm.caesar.key, encryption.text)
                return new
        elif(encryption.algorithm.vigenere):
            if(encryption.var):
                new = self.vigenere_cipher(encryption.algorithm.vigenere.key, encryption.var, var=True)
                return new
            else:
                new = self.vigenere_cipher(encryption.algorithm.vigenere.key, encryption.text)
                return new
    
    def decryption_parser(self, encryption):
        if(encryption.algorithm.caesar):
            if(encryption.var):
                new = self.caesar_cipher(encryption.algorithm.caesar.key, encryption.var, decrypt=True ,var=True)
                return new
            else:
                new = self.caesar_cipher(encryption.algorithm.caesar.key, encryption.text, True)
                return new
        elif(encryption.algorithm.vigenere):
            if(encryption.var):
                new = self.vigenere_cipher(encryption.algorithm.vigenere.key, encryption.var, True, True)
                return new
            else:
                new = self.vigenere_cipher(encryption.algorithm.vigenere.key, encryption.text, True)
                return new

    def interpret(self, *commands):
        if self.loop == False:
            commands = self.model.commands
        else:
            commands = commands[0]
        for c in commands:
            if(c.__class__.__name__ == "Assignment"): # assignment command
                if(c.value):
                    self.varmap.update({c.var: c.value})
                elif(c.encryption):
                    self.varmap.update({c.var: self.encryption_parser(c.encryption)})
                elif(c.decryption):
                    self.varmap.update({c.var: self.decryption_parser(c.decryption)})
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
                new = self.encryption_parser(c)
                print(new)
            if(c.__class__.__name__ == "DecryptCommand"):
                new = self.decryption_parser(c)
                print(new)
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

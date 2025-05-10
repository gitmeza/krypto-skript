begin

let a = "It's hot outside"
let b = encrypt caesar, 4, a
print b
decrypt caesar, 4, b

let c = "Thank you"
let d = encrypt vigenere, "UrWelcome", c
print d
decrypt vigenere, "UrWelcome", d

end

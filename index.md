---
layout: default
---

# Purpose

The purpose of this programming language is to provide an introduction into cryptology. It serves as a learning tool
to experiment with different ciphers, conversions, etc.

## Sample Grammar

>EncryptCommand:
>  'encrypt' algorithm=Algorithm ',' text=STRING
>;
>
>DecryptCommand:
>  'decrypt' algorithm=Algorithm ',' text=STRING
>;
>
>ConvertCommand:
>  'convert' conversion=Conversions ',' text=STRING
>;

### Run Interpreter for KryptoSkript

```python
def main():
    krypto = KryptoSkript()
    krypto.interpret()
main()
```

```txt
begin
encrypt caesar, "It's hot outside"
end
```

```
13 24 32 23 31 12 19 24 31 19 25 24 23 13 8 9
```

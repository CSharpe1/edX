# Problem Set 6

### PROBLEM 1: ENCRYPTION (APPLYCODER)  (15/15 points)

Next, define the function applyCoder, which applies a coder to a string of text.

##### Test Cases

    >>> applyCoder("Hello, world!", buildCoder(3))
    'Khoor, zruog!'
    >>> applyCoder("Khoor, zruog!", buildCoder(23))
    'Hello, world!'


```python
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    
    ans = ''
    test= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    for l in text:
        if l in test: 
            ans += coder[l]
        else:
            ans += l
        
    return ans
    
```

	Correct
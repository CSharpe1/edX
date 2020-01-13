# Problem Set 6

### PROBLEM 1: ENCRYPTION (APPLYSHIFT)  (5/5 points)

Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

##### Test Cases

    >>> applyShift('This is a test.', 8)
    'Bpqa qa i bmab.'
    >>> applyShift('Bpqa qa i bmab.', 18)
    'This is a test.'

```python
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    
    coder = buildCoder(shift)
    
    return applyCoder(text, coder)
```

	Correct

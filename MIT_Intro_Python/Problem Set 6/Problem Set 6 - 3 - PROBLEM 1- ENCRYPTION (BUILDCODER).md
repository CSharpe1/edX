# Problem Set 6

### PROBLEM 1: ENCRYPTION (BUILDCODER)  (15/15 points)

You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.

**Be sure you have fully read and understood the introduction to this problem!**

```python
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO
    OrigineUp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OrigineLo = 'abcdefghijklmnopqrstuvwxyz'
    ShiftedUp = OrigineUp[shift:] + OrigineUp[0:shift]
    ShiftedLo = OrigineLo[shift:] + OrigineLo[0:shift]
    ShiftedAll = ShiftedUp+ShiftedLo
    ans= {}
    
    for i in range(len(OrigineUp)):
        
        ans[OrigineUp[i]] = ShiftedUp[i]
        ans[OrigineLo[i]] = ShiftedLo[i] 
    
    return ans 

```

	Correct
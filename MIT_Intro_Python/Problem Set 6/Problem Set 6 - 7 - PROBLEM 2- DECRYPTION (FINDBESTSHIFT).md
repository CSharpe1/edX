# Problem Set 6

### PROBLEM 2: DECRYPTION (FINDBESTSHIFT)  (15/15 points)

Your friend, who is also taking 6.00.1x, is really excited about the program she wrote for Problem 1 of this problem set. She sends you emails, but they're all encrypted with the Caesar cipher!

If you know which shift key she is using, then decrypting her message is an easy task. If the string message is the encrypted message and k is the shift key she is using, then calling applyShift(message, 26-k) returns her original message. Do you see why?

The problem is, you don't know which shift key she is using. The good news is, you know your friend only speaks and writes English words. So if you can write a program to find the decoding that produces the maximum number of real English words, you can probably find the right decoding (there's always a chance that the shift may not be unique. Accounting for this would use statistical methods that we won't require of you.)

### PSEUDOCODE

Right now, you should take time to write some pseudocode! Think about an algorithm you could use to solve this problem and write the steps down. Then, you can verify your algorithm with the supplied pseudocode in ps6_pseudo.txt before coding.

After you've done writing and checking your pseudocode, implement findBestShift(). This function takes a wordList and a sample of encrypted text and attempts to find the shift that encoded the text. A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words. Note that this only means that most of the words obtained are actual words. It is possible to have a message that can be decoded by two separate shifts into different sets of words. While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.

To assist you in solving this problem, we have provided a helper function, isWord(wordList, word). This simply determines if word is a valid word according to the wordList. This function ignores capitalization and punctuation.

```python
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    shiftBook = {}
    maxNW = 0
    
    for shift in range(0, 26):
        nw = 0
        coder = buildCoder(shift)
        CText = applyCoder(text, coder)
        words = CText.split(' ')
        for w in words:
            if isWord(wordList, w):
                nw += 1
        shiftBook[shift] = nw        
        maxNW = max(shiftBook.values())

    for k in shiftBook.keys():
        if shiftBook[k]== maxNW:
            return k
    return None        
                
            

```

	Correct
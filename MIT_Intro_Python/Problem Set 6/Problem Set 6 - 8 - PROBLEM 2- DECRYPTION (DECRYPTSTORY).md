# Problem Set 6

### PROBLEM 2: DECRYPTION (DECRYPTSTORY)  (5/5 points)

Now that you have all the pieces to the puzzle, please use them to decode the file **story.txt**. In the skeleton file, you will see a method **getStoryString()** that will return the encrypted version of the story. Fill in the following function; it should create the wordList, obtain the story, and then decrypt the story. Be sure you've read through the whole file to see what helper functions we've defined for you that may assist you in these tasks! This function will be only a few lines of code (our solution does it in 4 lines).

```python
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    CText = getStoryString ()
    wordList = loadWords()
    shift = findBestShift(wordList, CText)
    text = applyShift(CText, shift)
    return text

```

	Correct
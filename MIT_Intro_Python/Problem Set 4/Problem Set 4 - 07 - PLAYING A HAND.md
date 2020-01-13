### PLAYING A HAND  (15/15 points)

In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

**Note**: Do **not** assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

**Testing**: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:

    def playHand(hand, wordList, n):
        """
        Allows the user to play the given hand, as follows:
    
        * The hand is displayed.
        * The user may input a word or a single period (the string ".") 
          to indicate they're done playing
        * Invalid words are rejected, and a message is displayed asking
          the user to choose another word until they enter a valid word or "."
        * When a valid word is entered, it uses up letters from the hand.
        * After every valid word: the score for that word is displayed,
          the remaining letters in the hand are displayed, and the user
          is asked to input another word.
        * The sum of the word scores is displayed when the hand finishes.
        * The hand finishes when there are no more unused letters or the user
          inputs a "."
    
          hand: dictionary (string -> int)
          wordList: list of lowercase strings
          n: integer (HAND_SIZE; i.e., hand size required for additional points)
          
        """
        
        n = calculateHandlen(hand)
        h = hand.copy()
        l = calculateHandlen(h)
        s = 0    # score of each word
        ts = 0   # total score
        
        while  l > 0:
            # show the current hand
            showHand(h)
            # ask user to input the word and save it
            word = raw_input ('Enter word, or a "." to indicate that you are finished: ')
            # check if input word is "."
            if word == '.':
                print 'Goodbye! ',
                break
            # if it's a valid word then calculate the score, total score and print them
            elif isValidWord(word, h, wordList):
                s = getWordScore(word, n)
                ts += s
                print '"'+str(word)+'"'+' earned '+str(s)+' points. Total: '+str(ts)+' points'
                # reset the current hand and l
                h = updateHand(h, word)
                l = calculateHandlen(h)
            else:
                print 'Invalid word, please try again.'
            if l == 0:
                print 'Run out of letters. ',
        
        print 'Total score: '+ str(ts)
    
    # -----------------------------------
    def showHand(hand):
        h = hand.copy()
        print "Current Hand:  ",
        for k in h.keys():
            while h[k]>0:
                print str(k) ,
                h[k] -= 1
        print        
        
    """
    -------------------------------------
        getWordScore(word, n)
            Returns the score for a word. Assumes the word is a valid word.
            word: string (lowercase letters) 
            n: integer (HAND_SIZE; i.e., hand size required for additional points)
    --------------------------        
        updateHand(hand, word)        ->    current hand
    --------------------------
        isValidWord(word, hand, wordList)    ->    True/False
    --------------------------    
        calculateHandlen(hand)    ->    length (number of letters) in the current hand
     """
    

	Correct
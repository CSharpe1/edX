from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):    
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for w in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(w, hand, wordList):    
            # Find out how much making that word is worth
            s = getWordScore(w, n)
            # If the score for that word is higher than your best score
            if s > bestScore:
                # Update your best score, and best word accordingly
                bestScore = s
                bestWord = w    
    # return the best word you found.
    return bestWord



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    h = hand.copy()
    l = calculateHandlen(h)
    s = 0    # score of each word
    ts = 0   # total score
    
    while  l > 0:
        print 'Current Hand: ',
        displayHand(h)
        word = compChooseWord(h, wordList, n)
        if word == None:
            break
        else:
            s = getWordScore(word, n)
            ts += s
            print '"'+str(word)+'"'+' earned '+str(s)+' points. Total: '+str(ts)+' points'
            print
            # reset the current hand and l
            h = updateHand(h, word)
            l = calculateHandlen(h)
    print 'Total score: '+str(ts)+' points.'
            
    
#
# Problem #8: Playing a game
#
# a helper for playGame function
def play(hand, wordList, n):
    while True:
        print
        player = raw_input ('Enter u to have yourself play, c to have the computer play: ')
        if player == 'u':
            print
            #hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, n)
            break
        elif player == 'c':
            print
            #hand = dealHand(HAND_SIZE)
            compPlayHand(hand, wordList, n) 
            break
        else:
            print 'Invalid command.'
            print
                


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    import sys
    hand = {}
    
    while True:
        command = raw_input ('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if command == 'n':
            hand = dealHand(HAND_SIZE)
            play(hand, wordList, HAND_SIZE)
            
        elif command == 'r':
            if hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:    
                play(hand, wordList, HAND_SIZE)
                
        elif command == 'e':
            break
            sys.exit
            
        else:
            print 'Invalid command.'
            print
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



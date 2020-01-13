# Problem Set 7

### Conflict with Grader

To avoid getting an error from the grader about using the class variables title, subject, or summary, rename any variable you have used with these names to something else. Thank you!

---

### PART 3: FILTERING  (10/10 points)

At this point, you can run ps7.py, and it will fetch and display Google and Yahoo news items for you in little pop-up windows. How many news items? All of them.

Right now, the code we've given you in ps7.py gets all of the feeds every minute, and displays the result. This is nice, but, remember, the goal here was to filter out only the the stories we wanted.

### PROBLEM 10

Write a function, filterStories(stories, triggerlist) that takes in a list of news stories and a list of triggers, and returns a list of only the stories for which any of the triggers fires on. The list of stories should be unique - that is, do not include any duplicates in the list. For example, if 2 triggers fire on StoryA, only include StoryA in the list one time.

After completing Problem 10, run the file ps7_test.py. All the tests should now pass.

**Canopy specific instructions:** Every time you modify code inps7.pygo to
Run -> Restart Kernel (or hit the CTRL with the dot on your keyboard)

before running ps7_test.py. You have to do this every time you modify the fileps7.pyand want to run the fileps7_test.py, otherwise changes to the former will not be incorporated in the latter.

Also after completing Problem 10, you can try running ps7.py, and various RSS news items should pop up, filtered by some hard-coded triggers defined for you in some code near the bottom. The code runs an infinite loop, checking the RSS feed for new stories every 60 seconds. Press "Exit" at the bottom of the popup window to exit out of the program.

**Note:** In addition to the function filterStories, please provide your definitions of WordTrigger, TitleTrigger, SubjectTrigger, SummaryTrigger, and PhraseTrigger in the following box.

```python
# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box

import string

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word        
    def isWordIn(self, text):
        w = self.word.lower()
        text = text.lower()
        for char in text:
            if char in string.punctuation:
                text = text.replace(char,' ')               
        textList = text.split()
        if w in textList:
            return True
        else:
            return False
            
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
                
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase    
    def evaluate(self, story):
        p = self.phrase
        pInSubject = p in story.getSubject()
        pInSummary = p in story.getSummary()
        pInTitle = p in story.getTitle()        
        if pInSubject or pInSummary or pInTitle:       
            return True
        else:
            return False

def filterStories(stories, triggerlist):
    report = []
    for S in stories:
        for T in triggerlist:
            if T.evaluate(S):
                if not S in report:
                    report.append(S)
    return report                
                    
    
        
```

	Correct

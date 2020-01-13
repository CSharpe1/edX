### PROBLEM 7  (20/20 points)

Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

```python
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    ans=[]
    value = None
    for k in aDict.keys():
      if countValue(aDict[k], aDict) == 1:
          ans.append(k)
    return ans      
  
def countValue(value, aDict):
    '''
    aDict: a dictionary
    value: a value in the dictionary
    
    return: how many of that value is in the dictionary
    '''
    counter = 0
    for v in aDict.values():
          if v == value:
              counter += 1
    return counter            
  
  
                                                                                                                    
```

	Correct
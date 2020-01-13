### PROBLEM 5  (10/10 points)

Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

    def primesList(N):
        '''
        N: an integer
        Returns a list of prime numbers
        '''
        # Your code here

```python
def primesList(N):
    '''
    N: an integer
    '''
    ans = []
    for n in range(2,N+1):
        if isPrime(n):
            ans.append(n)
    return ans                         

def isPrime(N):
    for i in range(2,N+1):
        if N%i == 0:
            if i == N:
                return True
            else:
                return False
    return False      

      
```

	correct
	
	
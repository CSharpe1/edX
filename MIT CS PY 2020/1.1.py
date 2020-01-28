# REMOVE BEFORE SUBMITTING

s = 'aei'

# Global Variable
count = 0
vowle = 0

length = len(s) - 1
while count <= length:
    if s[count] == 'a' or s[count] == 'e' or s[count] == 'i' or s[count] == 'o' or s[count] == 'u':
        vowle += 1
    count += 1
print("Vowel Count", vowle);


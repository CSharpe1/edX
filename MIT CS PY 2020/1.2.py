#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

s = 'adasacabob'
#####################################

Bobcount = 0
count = 0
keyfound = 0

length = len(s) - 1
endpoint = length
print(endpoint);

while count <= length:
    if s[count] == 'b':
        keyfound += 1
        if s[count+1] == 'o':
#            print("bo found now to check for b");
            if s[count+2] == 'b':
#                print("bob found now increment bob counter");
                Bobcount += 1

    count += 1


print("Number of times bob occurs is:", Bobcount);

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh

#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc


s = 'abcxyz'
#######
Longsubstring = 'a'
length = len(s) - 1
Num = 0
it1 = 0
it2 = 1
stringlength = 0

#print(s[0:1]);
#print(s[1:2]);

#a = s[0:1]
#b = s[1:2]

while Num < length:
    if  s[it1] < s[it1+1]:            #s[it1:it2] < s[it2:it2+1] :
        stringlength += 1
#        it1 += 1
        print("smaller than previous", s[stringlength-1]);
    else:
        print("bigger than previous")



#if a < b:
#    print("smaller")

#if (s[1:1]) > (s[2:2]):
#    print("Bigger")

print("Longest substring in alphabetical order is: ", Longsubstring);

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

s = 'adabobobobsacabob'
#####################################

Bobcount = 0
Num = 0
length = len(s) - 1



while Num <= length:
    if s[Num:Num+3] == 'bob' :      #and check[Num:Num+3] == 3 :
        Bobcount += 1
    Num += 1
print("Number of times bob occurs is:", Bobcount);



#keyfound = 0
#new_count = 0
#check = s
#endpoint = length

#while Num <= length:
# #  count()
#    if s[Num] == 'b' :#and check[Num:Num+3] == 3 :
#        keyfound += 1
#  #      print("first b");
#        print("Slice", check[Num:Num+3]);
#        if s[Num+1] == 'o':
#            if s[Num+2] == 'b':
#                Bobcount += 1
#    Num += 1
#print("Number of times bob occurs is:", Bobcount);




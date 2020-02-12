animals = { 'a': ['aardvark', 'aca','agaga','aaaa'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# We want to write some simple procedures that work on dictionaries to return information.
# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.

# If there are no values in the dictionary, biggest should return None.

#def biggest(aDict):
#    '''
#    aDict: A dictionary, where all the values are lists.
#
#    returns: The key with the largest number of values associated with it
#    '''
#    # Your Code Here



x = 0
# print(animals.keys());
# print(animals.values());

# for key in animals	:
	# print(x);
	# x+= 1
	
# for i in sorted(animals.values()):
	# print(i);

# print(	animals				);
print("########################");
#print(animals.values);

# values = animals.values()


# best = max(values)
# words	=	[]
# for x in animals:
	# if animals[x]	==	best:
		# words.append(x)
	# print(words, best);

# print(animals);

# print("########################");
# print(best);




# result = None
# biggestValue = 0
# for key in aDict.keys():
    # if len(aDict[key]) >= biggestValue:
        # result = key
        # biggestValue = len(aDict[key])
# print(result);


key = 'b'
print(len(animals[key]));

print("########################");
print("########################");




for key in animals.keys():
	print(key);


size = 0
result = None
for key in animals.keys():
	print(key);
	if len(animals[key]) >= size:
#		print(key, "is bigger than size");
		result	=	len(animals[key]
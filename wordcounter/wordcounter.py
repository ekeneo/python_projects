# 1 Get the name of the file and open it

fname = input("Enter file: ")
#This is so that you do not necessarily need to type in the full name of the
#file in the prompt. You can just press enter and it would open fname.
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

# 2 Next count word frequency

di = dict()  #Creates a dictionary di
for lin in hand:
    lin = lin.rstrip()  # Strip the spaces on the right side of the line.
    wds = lin.split()  # Split the line into a list of words
    for w in wds:

#Using the if else statement method
    #    if w in di :
    #        di[w] = di[w] + 1
    #    else:
    #        di[w] = 1
    #    print(w, di[w])

#Or using the get() method (idiom that retrieves/creates/updates counter)
# i.e it takes a new word w in the dictionary and assigns its count to 0
# Therefore, if the key is not there, the count is zero
    #    oldcount = di.get(w,0)
    #    print(w,'old',oldcount)
    #    newcount = oldcount + 1
    #    di[w] = newcount
    #    print(w,'new',newcount)

# Or An alternaive approach to using the get()
# Its eliminated the need to write the 5 lines code as before
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])
#print(di)

# 3 Now we want to find the most common words

#Using a max loop
largest = -1
theword = None
for k,v in di.items():
#items() is a method in dictionary that gives the key-value pairs
# Therefore, we need two iteration variables k for key and v for values
    #print(k,v)
    if v > largest:
        largest = v
        theword = k  # to capture/remember the word that was largest
        totalwords = sum(di.values()) # to calculate the total no o words in the file

# print out results
print('Filename:',fname)
print("Word with the largest count:",'"',theword,'"',"with", largest, "occurences.")
print('The total number of words:',totalwords)

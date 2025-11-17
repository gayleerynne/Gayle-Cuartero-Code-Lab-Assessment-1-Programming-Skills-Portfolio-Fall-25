
# All loops in a single project
# I used numbers a-e to differentiate the loops

print ("loop that counts up from 0 to 50 in increments of 1")
for a in range(51): # counts up to 50, ending before 51.
    print(a)

print ("loop that counts down from 50 to 0 in decrements of 1")
for b in range (50, -1, -1): # the third value determines the decrement or increment value.
    print (b)

print ("loop that counts up from 30 to 50 in increments of 1")
for c in range (30, 51): # starts at 30 and counts up to 50, ending before 51.
    print (c)

print ("loop that counts down from 50 to 10 in decrements of 2")
for d in range (50, 9, -2): # the 3 values show the start, end, and steps. A negative number means decreasing.
    print (d)

print ("loop that counts up from 100 to 200 in increments of 5")
for e in range (100, 201, 5): # the 3 values show the start, end, and steps.
    print (e)


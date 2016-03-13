def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4,8,16,17,23,45]

small = count_small(lost)

print "The result of the 'count_small' function is: " + str(small)

print ('')
print ('String Looping: ')
print ('')

for letter in "Supermarket":
    print letter

print ('')

sentence = "Coding is fun!"

for letter in sentence:
    # Only print out the letter i
    if letter == "i":
        print letter

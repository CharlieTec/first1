def adder(N):
    i = 0
    accumulator = 0
    while (i < N):
        i = i + 1
        accumulator = accumulator + i
    return accumulator

#
print "adder(5): ", adder(5)
print "adder(10): ", adder(10)


###
done = False
while not done:
    character = input("Enter some value: ")
    if character.isdigit():
        print "Is Digit"
    elif character.isalpha():
        print "Is Letter"
    else:
        done = True
print "Thaks for using this program"


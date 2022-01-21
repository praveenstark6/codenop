for a in range(10):
    if a == 5:
        continue
    print(a, "helloworld")

# when using while loop, be careful of infinite loops 
# TO AVOID INFINITE LOOP IN WHILE
# remember to increment or decrement the variable(i) value everytime 
# remember not to use continue statement before increment code inside the loop

i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
print("end of the program")

print(i)







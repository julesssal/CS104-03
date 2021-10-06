
average = 0
total = 0
howManyEntered=0
howMany= int(input('How many test scores would you like to enter \n'))

while( howManyEntered < howMany ):
        testScore=int(input('Enter test score \n'))
        total=total+testScore
        howManyEntered+=1


average= total/howMany
print('The average for the test scores you entered is: ')
print(average)

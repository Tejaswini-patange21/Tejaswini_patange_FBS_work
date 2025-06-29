#program to find minimum no.of notes for given amount
amount = int(input("Enter amount:"))
#500

n500 = amount//500
r_amount = amount%500

#200
n200 = amount//200
r_amount = amount%200

#n100
n100 = amount//100
r_aomunt= amount%100

#n50
n50 = amount//50
r_amount = amount%50

#n20
n20 = amount//20
r_amount = amount%20

#n10
n10 = amount//10
r_amount = amount%10

print("Enter no of the notes  500:",n500)
print("Enter no of the notes 200:",n200)
print("Enter no of the notes 100:",n100)
print("Enter no of the notes 50:",n50)
print("Enter no of the notes 20:",n20)
print("Enter no of the notes 10:",n10)
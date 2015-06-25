#this program creates a function that acts like list count

print("This program has a function that acts like the list count method.")

#creates new empty list
lst = []
#sets max length for list
maxLength = eval(input("How many items are in your list? "))
#creates list with inputs from user
while len(lst) < maxLength:
    item = input("Enter your next list item: ")
    lst.append(item)

#item that is counted in list
x = input("Which value would you like the program to count? ")

def count(lst, x):
    count = 0
    for i in lst:
        #if x equals the current element then the counter is increased
        if x == i:
            count+=1
    print(str(x) + " appeared " + str(count) + " times in your list.")
count(lst, x)



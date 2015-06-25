#this program has the user create a list and then asks the user to pick an element to remove
#the program tells the user if the element is in list or not

print("Please insert your list")

#creates new empty list
lst = []
#sets max length for list
maxLength = eval(input("How many items are in your list? "))
#creates list with inputs from user
while len(lst) < maxLength:
    item = input("Enter your next list item: ")
    lst.append(item)
    #sorts list in case list is not entered as sorted
    lst.sort()

#element we are removing from list
x = input("What would you like to remove from your list? ")

#this function removes the first occurance of the element from the list
#if element is  not found in list it will notify user of such
def sortedRemove(lst, x):
    if x in lst:
        #removes first occurance of element x in list
        lst.remove(x)
        print("Your new list with " + str(x) + " removed is: " + str(lst))
    else:
        print("You do not have " + str(x) + " in your list.")
    #sorts list again
    lst.sort()
    

sortedRemove(lst,x)

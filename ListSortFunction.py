#this program has a function that acts like the list sort method

print("This program has a function that acts like the list sort method.")

#list filled with user's inputs
lst = []
maxLength = eval(input("How many items are in your list? "))
#create lst with inputs from users
while len(lst) < maxLength:
    item = input("Enter your next list item: ")
    lst.append(item)

#this function sorts the lst list and then prints the sorted list
def sort(lst):
    for i in range(1,len(lst)):
        value = lst[i]
        i = i-1
        while i>=0:
            #if element is less than next element the elements are swapped
            if value < lst[i]:
                lst[i+1] = lst[i]
                lst[i] = value
                i -= 1
            else:
                break
    print("\nYour sorted list is: ")
    print(lst)
            
sort(lst)


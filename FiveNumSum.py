#this program creates the 5 number summary with a user's entered list

#predefined list
lst = [1,2,3,4,5,6]


#main function that calls each function
def main():
    med = median(lst)
    fq = first(lst)
    lq = last(lst)
    printResults(min, max, med, fq, lq)


#min and maximum values
min = lst[0]
max = lst[len(lst)-1]


#returns the median of list
def median(l):
    half= len(l)//2
    int(half)
    l.sort()
    #if there are an even number of elements the program averages
    #the middle two values of the list
    if len(l) % 2 == 0:
        num1= l[half]
        num2=l[half-1]
        med = (num1+num2)/2.0
        return (med)
    else:
        med = l[half]
        return med

#returns the first quartile median
def first(l):
    half = len(l) // 2
    quarter = half//2
    l.sort()
    #if there are an even number of elements the program averages
    #the middle two values in the first quartile of the list
    if len(l) % 2 == 0:
        sum = float(l[quarter-1] + l[quarter])
        fq = sum/2.0
        return fq
    else:
        fq = l[quarter]
        return fq

#returns last quartile median of the list
def last(l):
    half = len(l) // 2
    quarter = half//2
    quarter += half
    l.sort()
    if len(l) % 2 == 0:
        #if there are an even number of elements the program averages
    #the middle two values in the last quartile of the list
        sum = float(l[quarter-1] + l[quarter])
        lq = sum/2.0
        return lq
    else:
        lq = l[quarter]
        return lq

#prints results for each value
def printResults(min, max, med, fq, lq):
    print("\nThe minimum is: "+str(min))
    print("The maximum is: " + str(max))
    print("The median is: " + str(med))
    print("The first quartile is: " + str(fq))
    print("The last quartile is: " + str(lq))

main()

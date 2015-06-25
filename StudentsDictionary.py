#utilizing dictionaries

#dictionaries for each subject
English = {}
History = {}
Math = {}
Biology = {}
Spanish = {}


#reads data from file and puts last name and score into correct dictionary
with open('Students.txt') as f:
 for line in f:
    listedline = line.split() 
    if len(listedline) > 1:
        English[listedline[0]] = listedline[1]
        History[listedline[0]] = listedline[2]
        Math[listedline[0]] = listedline[3]
        Biology[listedline[0]] = listedline[4]
        Spanish[listedline[0]] = listedline[5]

#converts score from string to int
English = dict((k,int(v)) for k,v in English.items())
History = dict((k,int(v)) for k,v in History.items())
Math = dict((k,int(v)) for k,v in Math.items())
Biology = dict((k,int(v)) for k,v in Biology.items())
Spanish = dict((k,int(v)) for k,v in Spanish.items())

#prints dictionaries
print("English: ")
print(English)
print("History: ")
print(History)
print("Math: ")
print(Math)
print("Biology: ")
print(Biology)
print("Spanish: ")
print(Spanish)


#prints the students that failed for each subject
for keys in English:
    if English[keys] < 60:
        print("\nThe students that failed English are: ")
        print(keys)


print("\nThe students that failed History are: ")
for keys in History:
    if History[keys] < 60:
        print(keys)

print("\nThe students that failed Math are: ")
for keys in Math:
    if Math[keys] < 60:
        print(keys)

print("\nThe students that failed Biology are: ")
for keys in Biology:
    if Biology[keys] < 60:
        print(keys)

print("\nThe students that failed Spanish are: ")
for keys in Spanish:
    if Spanish[keys] < 60:
        print(keys)

"""Common Data types in Python
1. Numbers
2. Strings
3. Lists
4. Tuples
5. Dictionaries
6. Sets"""



x = 145
print x

x = 14 + 6j
y = 14 + 8j
print x + y

x = "Hello Ajita, You are so sweet. Ajita's smile is beautiful."
print x

print x.split(" ")
print "-lol ".join(x)
print x.join("lol")

print x.count('A')


arry = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

squared_array = [x*x for i in arry for x in i]

print squared_array




def variableArg(*args):
    print args
    print "======="
    return args

r = variableArg(1, 2, 3)
print r


def variableKArgs(**kwargs):
    print kwargs
    print ("======")
    return kwargs

karg1 = variableKArgs(name = 'xyz', age = '21')
print karg1



num = [1,2,3,4,5,6,7,8,9]
squared = map(lambda x: x*x, num)
print squared


num1  = range(50)
dividedBy3 = filter(lambda x: x % 3 == 0, num1)
print dividedBy3

num = [0,1,2,4,5,6,7,8,9]
sumOfList = reduce(lambda x,y: x+y, num)
print sumOfList


"""LIST COMPREHENSION, LAMBDA FUNCTION, AND GENERATOR CONCEPT ARE VERY IMPORTANT TOPICS"""


dict_name_age = {"gourav": 21, "ajita": 21, "rishabh": 22}


file = open("ajita.txt", "r")
file.next()
def print_these(a,b,c):
    print(a,"is stored in a")
    print(b,"is stored in b")
    print(c,"is stored in c")

print_these(1,2,3)

def print_these_1(a,b,c=None):
    print(a,"is stored in a")
    print(b,"is stored in b")
    print(c,"is stored in c")

print_these_1(1,2)

def print_these_2(a=None,b=None,c=None):
    print(a,"is stored in a")
    print(b,"is stored in b")
    print(c,"is stored in c")

print_these_2(a=1,c=3)

#splat operator
a=[1,2,3]
b=[*a,4,5,6]
print(b)

def printScores(student_name,*scores):
    print("Name of the student "+student_name)
    for i in scores:
        print(i)

printScores("sonu",100,90,50,80,30)

def petNames(owner,**pets):
    print("Name of the owner "+owner)
    for key,value in pets.items():
        print(key,"=",value)

petNames("sonu",dog="jimmy",monkey="hanum",cow="kal",horse="jummy")


def new_code(a,b,*args):
    print(a)
    print(b)
    for i in args:
        print(i)

new_code(1,2,3,4,5,6,7)

def new_code2(a,b,*args,**kwargs):
    print(a)
    print(b)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

new_code2(1,2,3,4,5,6,7,8,extra=10,doubleextra=20)

dict1={"key1":"up","key2":"down","key3":"left","key4":"right"}
dict2={"key5":"f1","key6":"f2"}
common_dict={**dict1,**dict2}
print(common_dict)
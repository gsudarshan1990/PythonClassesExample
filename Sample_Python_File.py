print("Hello World")

string1 = 'Good morning'
print(string1[:3])
print(string1[4:])

message='A kong string with a silly typo'
new_message=message[:2]+'l'+message[3:]
print(new_message)

pets="Dogs & Cats"
print(pets.index('&'))

email="shashank@gmail.com"
old_domain = "gmail.com"
new_domain = "yahoo.com"

def replace(email,old_domain,new_domain):
    with_symbol="@"+old_domain
    for with_symbol in email:
        index=email.index('@')
        new_email=email[:index]+new_domain
    return new_email


print(replace(email,old_domain,new_domain))

string2=" ".join(["This","is","joined"])
print(string2)

print("...".join(["This","is","a","string","joined","by","three","dots"]))

string3="This is the string splitted based on the split method"
print(string3.split())

print(string3.count('s'))
print(string3.endswith('method'))

name="Manny"
lucky_number=len(name)*3

print("Your name is {} and your lucky number is {}".format(name,lucky_number))

print("Your name is {name} and your lucky number is {number}".format(name=name,number=lucky_number))

print("Your name is {0} and your lucky number {1}".format(name,lucky_number))


price =7.5
with_tax = price*3.33

print(price,with_tax)
print("base price {:.2f} and tax is {:>50.2f}".format(price,with_tax))

list1=['Now','we','are','cooking']
print(type(list1))
print(len(list1))
print(list1)

print(list1[0])
print(list1[1])

fruits=["Pineapple","Apples","Grapes","Oranges"]
fruits.append("Jack Fruit")
fruits.insert(0,"Kiwi")

fruits.insert(len(fruits)+10,"peach")

print(fruits)

fruits.remove("Grapes")
print(fruits)

print(fruits.pop(2))
print(fruits)

fruits[2]='Strawberry'

print(fruits)

animals=['lion','monkey','zebra','dolphin']
len_chars=0
for animal in animals:
    len_chars+=len(animal)
print("Total length:{} and average:{}".format(len_chars,len_chars/len(animals)))

names=['laxman','rama','hanuman','sita']
for index,person in enumerate(names):
    print('{}-{}'.format(index+1,person))

email_list=[('laxman','laxman@gmail.com'),('rama','rama@gmail.com')]
def re_order(people):
    for name,email in people:
        print("{}<{}>".format(name,email))

re_order(email_list)

multiples=[]
for x in range(71):
    if x%7 == 0:
        multiples.append(x)
print(multiples)

multiples=[]
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

multiples=[x*7 for x in range(1,11)]
print(multiples)

programs=["Python","Java","C","C++","COBOL","VB"]
length_program=[len(x) for x in programs]
print(length_program)

multiples_of_three=[x for x in range(0,101) if x%3 == 0]
print(multiples_of_three)


file_count={"jpeg":20,"csv":24,"exe":33,"txt":52,"py":100}
print(file_count)

print(file_count["jpeg"])

print("jpeg" in file_count)

file_count["cfg"] =12

print(file_count)

file_count["csv"]=17
print(file_count)

del file_count["csv"]

print(file_count)

for key in file_count:
    print(key)

for key,value in file_count.items():
    print("There are {} and {} ".format(value,key))

for key in file_count.keys():
    print(key)

for value in file_count.values():
    print(value)


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    print(result)

count_letters("Hello")



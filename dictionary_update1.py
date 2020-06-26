#dict_comprehension
dict1={x:x**2 for x in range(10,20)}
print(dict1)

dict3={}
print(dict3.setdefault('city',['cleavedland','indiana']))


set1=set()
print(set1)

dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict1.update(dict2)
print(dict1)
print({**dict1,**dict2})
# #conditional and boolean
# if True:
#     print("condition was true")#print
#     if False:
#         print("false")#no print
language="c"
if language =="python":
            print("true")
elif language == "java":
        print("half true")
elif language == "c":
        print("half true 2")

        
else:
        print("false")




    #comparisons:
    #  equal:==
    # not equals:!=
    # greater than:>
    # lessthan : <
    #     greater than or equal:>=
    # less than or equal : <=
#object identity : is

#boolean operations
#and
#or
#not
user="admin"
logeed_in= False
if user == "admin" and logeed_in:  #both true than it runs
        print("admin page")
else:
       print("bad")
if user == "admin" or logeed_in:   #only one has to be true
 
 print("admin page")
else:
     print("bad")

if not logeed_in:#evalute the condition
       print("pleasse log in")
else:
       print("bad creds")

a=[1,2,3]
b=[1,2,3]
a=b
print(id(a))
print(id(b))
print(a is b)#has to be same id also
#falsse values:
#false
condition=False
if condition:
       print("evaluate true")
else:
       print("evaluate to false")
#none
condition=None
if condition:
       print("evaluate true")
else:
       print("evaluate to false")
     #zero of any numeric type
condition=0
if condition:
       print("evaluate true")
else:
       print("evaluate to false")  
condition=10  #evaluate true to any number except 0
if condition:
       print("evaluate true")
else:
       print("evaluate to false")
 #any empty sequence like list,set ,tuple
condition=[]
if condition:
       print("evaluate true")
else:
       print("evaluate to false")
#any empty mapping like dictionary
condition={}
if condition:
       print("evaluate true")
else:
       print("evaluate to false")
#and some user defined function alse can evaluate to false and everything other than this evaluate to true
 








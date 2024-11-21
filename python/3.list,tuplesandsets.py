#lists
cources=["history","math","physics","compsci"]
print(len(cources))
print(cources)
print(cources[0])
print(cources[3])
print(cources[-1])
# print(cources[4])#ERROR
print(cources[0:2])#slicing
# print(cources[2:])
cources.append("art")
print(cources)
cources.insert(0,"chemistry")
print(cources)
cources2=["education","pe"]
cources.insert(0,cources2)
print(cources)
# cources.extend(cources2)
# print(cources)#adds individual items
# cources.remove("math")
# popped=cources.pop()
# print(popped)
# print(cources)
# cources.reverse()
# print(cources)
# cources.sort()
# print(cources)
# nums=[9,5,7,2]
# nums.sort(reverse=True)
# print(nums)
# sorted_cources=sorted(nums)
# print(nums)#without altering the orignal list
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(cources.index("math"))
# print("math" in cources)
# for item in cources:
#     print(item)
# for index,cource in enumerate(cources,start=1):
#     print(index, cource)
#     courcess_str=", ".join(cources)
#     print(courcess_str)
#     #tuple
#     tuple_1=("history","math","physics","compsci")
#     tuple_2=tuple_1
#     print(tuple_1)
#     print(tuple_2)
#     tuple_1(0)="art"
#     print(tuple_1)
#     print(tuple_2)  #error
    #sets
# cs_cource={"history","math","physics","compsci"}
# print(cs_cource)#unordered to eliminate duplicates
# art_cource={"history","math","physics","compsci"}
# print(cs_cource.intersection(art_cource))#intersection
# print(cs_cource.difference(art_cource))
# print(cs_cource.union(art_cource))
# #empty list
# empty_list=[]
# empty_list=list()
# #empty tuples
# empty_tuples=()
# empty#_tuples=tuple()
# #emptysets
# empty_set={}#wrong  it becomes a dictionarry

# empty_set=set()
# #dictionart
# student={"name":"jhon","age":25,"cources":{"math","computer science"}}

# student.update({"name":"jane"})
# del student["cources"]
# print(student["name"])
# age=student.pop("age")
# print(age)








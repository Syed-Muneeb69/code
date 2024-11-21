# #functions
# def hello_func():
#     print("hello function.")
# hello_func()
# hello_func()
# hello_func()
# hello_func()
# hello_func()#keeping code dry
# def hello_func2(): #returns return value here is string
#      return "hello function"
# print(hello_func2().upper())
# print(len('TEST'))

# def hello_func3(greetings,name="you"):
#      return"{},{}".format(greetings,name)
# print(hello_func3("hi",name="muneeb"))
def student_info(*arge, **kwargs):
     print(arge)
     print(kwargs)
student_info('math','art',name="muneeb",age=22)
print("hello world")

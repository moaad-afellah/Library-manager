glb_var = "global"
glb_int = 3

def var_function():
    lcl_var = "local"
    print(lcl_var)


var_function()
print(glb_var)

# print(lcl_var)

def var_function_2():
    print(glb_var)

def var_function_3():
    glb_var = "local scope"
    print(glb_var)

var_function_3()




def sum():
    i=0
    print(i)

def prod():
    i=4
    print(i)

sum()
prod()



def f1():
    glb_var = "global modified"
    glb_int = 0
    print(glb_var)
    print(glb_int)

def f2():
    print(glb_var)
    print(glb_int)


f1()
f2()


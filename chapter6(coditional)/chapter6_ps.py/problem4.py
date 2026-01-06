# check username contation less then 10 words


username = input("enter username: ")

if(len(username)<10):
    print("your usernmae containes less then 10 charaters")
else:
    print("all is well")
dic={}
def SignUp():
    print("Enter UserName\n")
    user=input()
    print("Enter Password\n")
    pas=input()
    UserEncy=hash(user)
    PassEncy=hash(pas)
    if len(dic)==0:
        dic[UserEncy]=PassEncy
        print("Sign Up Completed...")
    else:
        for i in dic.keys():
            if i==UserEncy:
                print("User Already Exists !")
                break
            else:
                dic[UserEncy]=PassEncy
                print("Sign Up Completed...")
                break
        

def SignIn():
    flag=0
    print("Enter UserName\n")
    username=input()
    print("Enter Password\n")
    password=input()
    UserEncy=hash(username)
    PassEncy=hash(password)
    for i in dic.keys():
        if i==UserEncy:
            flag=1
            break
        else:
            flag=0
            
    if flag==1:
         print("Successfull Sign In...")
    else:
        print("Sign In Failed")
        
        

m=0
while m!=2:
    print("1-Signp\n2-SignIn")
    choice=int(input())
    if choice==1:
        SignUp()
        print("Do you want to Continue type 1 otherwise 2")
        n=int(input())
        m=n
    elif choice==2:
        SignIn()
        print("Do you want to Continue type 1 otherwise 2")
        n=int(input())
        m=n
    else:
        print("Choice Not Matched !")
    


    
    

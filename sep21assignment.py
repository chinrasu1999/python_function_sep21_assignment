#python functions assignment

registered_mail=[]
def register():
    print("***welcome to Register page***")
    first_name=input("enter your firstname:")
    last_name=input("enter your lastname:")
    email_id=input("enter your email id:")
    registered_mail.append(email_id)
    print(f"{first_name} {last_name} {email_id} ->Registered successfully")
    var=input("Do you want continue type yes,otherwise type no:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting Register page")    
def login():
    email_id=input("enter your email id:")
    if email_id in registered_mail:
        print("***Login Successfully***")
        print("Affiliated to Anna University colleges")
        print("press 1->Aksheyaa college")
        print("press 2->Panimalar college")
        print("press 3->Sairam college")
        choose_college=int(input("enter you want college:"))
        if choose_college==1:
            print("***your choosing Aksheyaa college***")
            aksheyaa_college()
        elif choose_college==2:
            print("***your choosing Panimalar college***")
            panimalar_college()
        elif choose_college==3:
            print("***your choosing Sairam college***") 
            sairam_college()   
        else:
            print("please type only 1 2 3")    
                
    else:
        print("This email is not registered,please go to register page")
        register()
def aksheyaa_college():
    print("aksheyaa college available departments")
    print("press ->mech")
    print("press ->civil")
    choose_dept=input("enter choose dept:")
    if choose_dept=="mech":
        print("your choosing mechanical department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 30k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 20k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 10k")  
        else:
            print("please enter the correct caste only 1 2 3")
                  
    elif choose_dept=="civil":
        print("your choosing civil department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 50k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 40k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 30k")  
        else:
            print("please enter the correct caste only 1 2 3")
           
    else:
        print("please type only available departments")
        var=input("Do you want continue press yes:")
        if var=="yes":
            main_function()
        else:
            print("Thanks for visiting")                                     

        
def panimalar_college():
    print("panimalar college available departments")
    print("press ->cse")
    print("press ->it")
    choose_dept=input("enter choose dept:")
    if choose_dept=="cse":
        print("your choosing cse department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 40k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 30k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 20k")  
        else:
            print("please enter the correct caste only 1 2 3")
                  
    elif choose_dept=="it":
        print("your choosing it department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 700k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 50k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 60k")  
        else:
            print("please enter the correct caste only 1 2 3")
           
    else:
        print("please type only available departments") 
        var=input("Do you want continue press yes:")
        if var=="yes":
            main_function()
        else:
            print("Thanks for visiting")

def sairam_college():
    print("sairam college available departments")
    print("press ->ece")
    print("press ->eee")
    choose_dept=input("enter choose dept:")
    if choose_dept=="ece":
        print("your choosing ece department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 40k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 40k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 20k")  
        else:
            print("please enter the correct caste only 1 2 3")
                  
    elif choose_dept=="eee":
        print("your choosing eee department")
        print("Fees details for schedule caste")
        print("press 1->oc caste")
        print("press 2->mbc caste")
        print("press 3->sc caste")
        choose_caste=int(input("enter your caste:"))
        if choose_caste==1:
            print("your is oc caste,so your fees details is 90k")
        elif choose_caste==2:
            print("your is mbc caste,so your fees details is 80k")
        elif choose_caste==3:
            print("your is sc caste,so your fees details is 70k")  
        else:
            print("please enter the correct caste only 1 2 3")
           
    else:
        print("please type only available departments")
        var=input("Do you want continue press yes:")
        if var=="yes":
            main_function()
        else:
            print("Thanks for visiting")                             


def main_function():
    print("ANNA UNIVERSITY")
    print("press 1->Register page")
    print("press 2->Login page")
    user=int(input("enter your number:"))
    if user==1:
        register()
    elif user==2:
        login()
    else:
        print("please type only 1 and 2") 
main_function()               
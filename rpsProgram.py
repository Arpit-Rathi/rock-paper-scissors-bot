import random
def print_choice(user,cpu):
    print("USER chooses ",user,end="")
    print()
    print("CPU chooses ",cpu,end="")
    print()

    if(user=="rock" and cpu=="paper"):
        print("CPU WINS")
    if(user=="paper" and cpu=="scissors"):
        print("CPU WINS")
    if(user=="scissors" and cpu=="rock"):
        print("CPU WINS")
    if(user==cpu):
        print("NOBODY WINS")
    if(cpu=="rock" and user=="paper"):
        print("USER WINS")
    if(cpu=="paper" and user=="scissors"):
        print("USER WINS")
    if(cpu=="scissors" and user=="rock"):
        print("USER WINS")

    f_r= open("rps.txt","r+")
    r1=f_r.readline()
    sr=int(r1[7:])
    p1=f_r.readline()
    sp=int(p1[8:])
    s1=f_r.readline()
    ss=int(s1[11:])
    f_r.close()

    if(user=="rock"):
        sr=sr+1
    if(user=="paper"):
        sp=sp+1
    if(user=="scissors"):
        ss=ss+1

    f_w= open("rps.txt","w")
    s="rock - "+str(sr)+"\n"
    f_w.write(s)
    s="paper - "+str(sp)+"\n"
    f_w.write(s)
    s="scissors - "+str(ss)
    f_w.write(s)
    f_w.close()
    return

def appoint_user(user):
    if(user=="r"):
        user="rock"
    if(user=="p"):
        user="paper"
    if(user=="s"):
        user="scissors"
    return user
def appoint_cpu(cpu):
    if(cpu==1):
        cpu="rock"
    if(cpu==2):
        cpu="paper"
    if(cpu==3):
        cpu="scissors"
    return cpu

print("ROCK PAPER SCISSORS\n")
print("Rules : ")
print("Select which mode you want to play - Easy(1) Medium(2) Hard(3)")
mode=int(input())

if(mode==1):
    print("...THE GAME IS ABOUT TO BEGIN...\n")
    for i in range(0,10):
        print("You choose from r,p and s ...")
        user=input()
        cpu=random.randint(1,3)
        print(cpu)

        user=appoint_user(user)
        cpu=appoint_cpu(cpu)
        print_choice(user,cpu)

elif(mode==2):
    print("...THE GAME IS ABOUT TO BEGIN...\n")
    for i in range(0,10):
        print("You choose from r,p and s ...")
        user=input()
        f_r= open("rps.txt","r+")
        r1=f_r.readline()
        sr=int(r1[7:])
        p1=f_r.readline()
        sp=int(p1[8:])
        s1=f_r.readline()
        ss=int(s1[11:])
        f_r.close()
        cpu=0
        if(sr>=sp and sr>=ss):
            if(cpu==0):
                cpu=2
        if(sp>=sr and sp>=ss):
            if(cpu==0):
                cpu=3
        if(ss>=sr and ss>=sp):
            if(cpu==0):
                cpu=1
        print(cpu)

        user=appoint_user(user)
        cpu=appoint_cpu(cpu)

        print_choice(user,cpu)

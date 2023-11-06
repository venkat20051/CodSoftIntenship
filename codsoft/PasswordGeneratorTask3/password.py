import random
import string
lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
spl_character=string.punctuation

password=""
while(True):
    len=int(input("\n enter the valid length of password(4 to 20) :"))
    if(len<4 or len>19):
        print("\n enter the valid lenght")
        continue
    strength=int(input('''
                       \t select\n
                       \t 1.easy(num)\n
                       \t 2.medium(num+char)\n
                       \t 3.hard(num+char+spl_character)\n'''))
    if(strength==1):
        for i in range(len):
            password+=str(random.randint(0,9))
        print("\n The Generated password is:",password)
        password=""
    elif(strength==2):
        for i in range(len-2):
            password+=str(random.randint(0,9))
        password+=random.choice(upper_case)
        password+=random.choice(lower_case)
        temp=list(password)
        random.shuffel(temp)
        password="".join(temp)
        print("\n The Generted Password is:",password)
        password=""
    elif(strength==3):
        for i in range(len-3):
            password+=str(random.randint(0,9))
        password+=random.choice(upper_case)
        password+=random.choice(lower_case)
        password+=random.choice(spl_character)
        temp=list(password)
        random.shuffle(temp)
        password="".join(temp)
        print("\n The Generated Password is:",password)
        password=""
    inn=input("press ({}) to do again or prompt ({}) to exit:".format("ENTER"," ."))
    if inn==".":
        print("Exiting.....")
        break
from spy_details import spy,Spy,ChatMessage#importing Spy class from file spy_details
from steganography.steganography import Steganography#importing Steganography module
import csv
from colorama import Fore,Style
from datetime import datetime#importing date and time
time=datetime.now()#current date and time
print time
print'Hello Buddy!'
print'Let\s get started'
Status_Message=['Sleeping','Busy','Do not disturb']
frnd1=Spy('Shubham','Mr.',21,4.2)
frnd2=Spy('Shushant','Mr.',32,5.1)
friends=[frnd1,frnd2]

def load_frnd():#loading friends in front of user when he sends the message

    with open('friends.csv','rU') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            spy=Spy(name=row[0], salutation=row[1], age=int(row[2]), rating=float(row[3]))
            friends.append(spy)
load_frnd()#calling the function

def load_chats():# to load all the chats
    with open('chats.csv','rU') as chats_data:
        reader=list(csv.reader(chats_data))

        for message,date,sent_by_me,receiver_name in reader[1:]:
            print Fore.BLACK+message,Fore.BLUE+date,Fore.RED+sent_by_me,Fore.MAGENTA+receiver_name
            print (Style.RESET_ALL)

def selected_chat():#to load the chat of selected friend only
    s_name=raw_input('Enter the friend whose chats you want to see..')
    with open('chats.csv','rU') as chats_data:
        reader=list(csv.reader(chats_data))
        for message,date,sent_by_me,receiver_name in reader[1:]:
            if s_name==receiver_name:
                print Fore.BLACK+message,Fore.BLUE+date,Fore.RED+sent_by_me,Fore.LIGHTGREEN_EX+receiver_name
                print(Style.RESET_ALL)

def add_status(c_status):#defining the function
    if c_status!=None:
        print"Your current status is "+c_status
    else:
        print"You don't have any status currently.."
    existing_status=raw_input("You want to select from old status? Y/N")
    if existing_status.upper()=='N':
        new_status=raw_input('Enter your status: ')
        if len(new_status)>0:

            with open('status.csv','a') as status_data:#adding status to status.csv
                writer=csv.writer(status_data)
                writer.writerow([new_status])
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in Status_Message:
            print str(serial_no)+old_status
            serial_no=serial_no+1
        user_choice=input('Enter your choice:')
        new_status=Status_Message[user_choice-1]
    updated_status=new_status
    return updated_status
def add_friend():
    frnd=Spy('','',0,0.0)
    frnd.sal=raw_input('what should we call you?')
    frnd.name=raw_input('Enter your name: ')
    frnd.age=input('what is your age? ')
    frnd.rating=input('what is your rating? ')
    frnd.is_online=True
    if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating:
        friends.append(frnd)
        with open('friends.csv','a') as friends_data:
            writer=csv.writer(friends_data)
            writer.writerow([frnd.name,frnd.sal,frnd.age,frnd.rating,frnd.is_online])
            print'Your friend is added successfully..'
    else:
        print'Friend cannot be added'
    return len(friends)
def select_a_frnd():
    serial_no=1
    for frnd in friends:
        print str(serial_no)+'.'+frnd.name
        serial_no=serial_no+1
    user_selected_frnd=input('Enter your choice: ')#selecting a friend
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index
def send_a_message():
    selected_friend=select_a_frnd()
    original_image=raw_input('What is the name of your image ?')
    secret_text=raw_input('What is your secret text ?')
    list=['SOS','HELP ME','SAVE ME']#if message is these words it will not be encoded
    if secret_text.upper() in list:
        print Fore.RED +'Inappropriate message..'
        print(Style.RESET_ALL)
    else:
       output_path="output.png"
       Steganography.encode(original_image,output_path,secret_text)#encoding the message
       print'Your message has been successfully encoded..'

       with open('chats.csv','a') as chats_data:#writing in chats.csv
         writer=csv.writer(chats_data)
         writer.writerow([secret_text,time,spy.name,friends[selected_friend].name])
def read_a_message():
    selected_friend=select_a_frnd()
    output_path=raw_input('Which image you want to decode? ')
    secret_text=Steganography.decode(output_path)#decoding the message
    print'Secret text is:'+secret_text
    new_chat=ChatMessage(secret_text,False)
    friends[selected_friend].chats.append(new_chat)
    print'Your secret message has been saved..'
def spy_chat(spy_name,spy_age,spy_rating):
    print'Here are your options..'+spy.name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input('What do you want to do?  \n1.Add a status \n2.Add a friend \n3.Send a message \n4.Read a message \n5.Read all chats \n6.Read chat of selected friend\n0.Exit')
        if spy_choice==1:
            current_status=add_status(current_status)
            print'Updated status is '+current_status
        elif spy_choice==2:
            no_of_friends=add_friend()
            print 'You have '+str(no_of_friends)+' friends..'
        elif spy_choice==3:
            send_a_message()
        elif spy_choice==4:
            read_a_message()
        elif spy_choice==5:
            load_chats()
        elif spy_choice==6:
            selected_chat()
        elif spy_choice==0:
            show_menu=False
        else:
            print'Invalid options..'
spy_exist=raw_input('Are you a new user: Y/N')
spy_exist = spy_exist.upper()
if spy_exist=='N':
    name=raw_input('Enter your login name: ')
    passd=raw_input('Enter your password: ')
    if name=='Rohit' and passd=='hello':
     print'Welcome back '+spy.name+' of age: '+str(spy.age)+'having rating of: '+str(spy.rating)
     spy_chat(spy.name,spy.age,spy.rating)
    else:
        print'Wrong name or password..'
elif spy_exist=='Y':
    spy=Spy('','',0,0.0)
    spy.name=raw_input('What is your spy name? ')
    print spy.name
    if len(spy.name)>2:
        print'Welcome '+spy.name+'.'
        spy.salutation=raw_input('What should we call you Mr. or Ms.?')
        if spy.salutation=='Mr.' or spy.salutation=='Ms.':
            spy.name=spy.salutation+' '+spy.name
            print'Welcome '+spy.name+'.Glad to see you back..'
            print'Alright '+spy.name+'.I would like toknow a little bit more about you.'
            spy.age=input('What is your age ?')
            if 12<spy.age<50:
                print'Your age is correct..'
                spy.rating=input('What is your rating ?')
                if spy.rating>5.0:
                    print'Great spy..'
                elif 3.5<spy.rating<=5.0:
                    print'Average Spy..'
                elif 2.5<spy.rating<=3.5:
                    print'Bad spy..'
                else:
                    print'Who hired you..'
                spy.is_online=True
                print'Authentication is completed..Welcome'+spy.name+'age: '+str(spy.age)+'raitng: '+str(spy.rating)
                spy_chat(spy.name,spy.age,spy.rating)
            else:
                print'You are not eligible to be a spy..'
        else:
            print'Invalid salutation..'
    else:
        print'Oopss please enter a valid name..'
else:
     print'Invalid Entry..'
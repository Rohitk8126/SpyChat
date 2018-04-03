from spy_details import spy ,Spy,ChatMessage#importing spy dictionary from spy_details file
from steganography.steganography import Steganography#importing Steganography module from steganography class of steganography library
from datetime import datetime #importing datetime module from datetime class
time=datetime.now() #now() function will return current date and time
print time #printing returned current date and time.
print'Hello buddy'#print hello buddy
print'Let\'s get started'
STATUS_MESSAGE=['Sleeping', 'Busy', 'Do not disturb']#list
frnd1=Spy('nidhi','Ms.',21,4.2)#object of class Spy
frnd2=Spy('pragati','Ms.',32,5.1)
friends=[frnd1,frnd2]

def add_status(c_status):
    if c_status != None: #if nothing is chosen from status
        print "Your current status is "+ c_status
    else:
        print"You don't have any status currently.."
    existing_status = raw_input("You want to select from old status? Y/N")
    if existing_status.upper() == 'N':
        new_status=raw_input('Enter your status : ')#asking new status from user
        if len(new_status) > 0: #checking length of status
            STATUS_MESSAGE.append(new_status)#adding new status to list..
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGE:#traversing the list
            print str(serial_no)+old_status
            serial_no=serial_no+1#increementing the value of serial no
        user_choice=input('Enter your choice :')
        new_status=STATUS_MESSAGE[user_choice-1]
    updated_status=new_status
    return updated_status
def add_friend():#add_friend to add a new friend
    frnd=Spy('','',0,0.0)
    frnd.name=raw_input('What is your name ?')#asking the new friend's name
    frnd.age=input('What is your age ?')#age
    frnd.rating=input('What is your rating ?')#rating
    if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating:
       friends.append(frnd)
    else:
        print 'Friend cannot be added..'
    return len(friends) # will return to add_friend()
def select_a_frnd():#selecting a frnd to send or read a message
    serial_no=1
    for frnd in friends:# traversing the dictionary friends to show the friends.
        print str(serial_no)+'.'+frnd.name
        serial_no=serial_no+1
    user_selected_frnd=input('Enter your choice : ')#user choice
    user_selected_frnd_index=user_selected_frnd-1#index of the selected frnd
    return user_selected_frnd_index

def send_a_message():#to send a message to selected friend
    selected_friend=select_a_frnd()
    original_image=raw_input('What is the name of your image ? ')#asking user about the name of image
    secret_text=raw_input('What is your secret text ? ') # asking about the secret text you want to save in image
    output_path="output.png"
    Steganography.encode(original_image,output_path,secret_text)#encoding the image with secret text..
    print 'Your message has been successfully encoded..'
    new_chat=ChatMessage(secret_text,True)
    friends[selected_friend].chats.append(new_chat) #appending in friends list the new_chat dictionary
    print'Your secret message is ready.'

def read_a_message():#to read a message
    selected_friend=select_a_frnd()
    output_path=raw_input('Which image you want to decode ? ')
    secret_text=Steganography.decode(output_path)
    print 'Secret text is:'+ secret_text
    new_chat=ChatMessage(secret_text,False)
    friends[selected_friend].chats.append(new_chat)#appending
    print'Your secret message has been saved...'

def spy_chat(spy_name,spy_age,spy_rating):#defining the function
    print'Here are your options..'+spy.name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input('What do you want to do \n 1. Add a status. \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. exit')
        if spy_choice==1:
            current_status= add_status(current_status)
            print 'Updated status is '+ current_status
        elif spy_choice==2:#elif for multiple conditions.
            no_of_friends=add_friend()
            print 'You have '+ str(no_of_friends) +' friends.'
        elif spy_choice==3:#will send encoded message
            send_a_message()
        elif spy_choice==4:#will display the decoded message
            read_a_message()
        elif spy_choice==0:
            show_menu=False
        else:
            print'Invalid options..'
spy_exist=raw_input('Are you a new user : Y/N')#asking whether you are new or not
if spy_exist.upper()=='N':#when spy is an old one
    print'Welcome back '+spy.name+' age :'+str(spy.age)+' having rating of '+str(spy.rating)
    spy_chat(spy.name,spy.age,spy.rating)#calling function
elif spy_exist.upper=='Y':
    spy=Spy("","",0,0.0)
    spy.name=raw_input('What is your spy_name?  ')#take input from user
    print spy.name
    if len(spy.name)>2:#checking the length of input
        print'Welcome '+spy.name +'.'#concatenating name with welcome.
        spy.salutation=raw_input('What should we call you Mr. or Ms. ')#input salutation from user
        if spy.salutation=='Mr.' or spy.salutation=='Ms.':
             spy.name=spy.salutation+' '+spy.name#concatenation
             print'Welcome '+spy.name +'. Glad to see you back..'
             print'Alright  '+spy.name+'. I would like to know a little bit more about you..'
             spy.age=input('What is your age..?')#input from user
             if 12<spy.age<50:#spy age should be between 12 to 50
                 print'Your age is correct....'
                 spy.rating=input('What is your rating..?')#input rating of spy
                 if spy.rating>5.0:
                     print'Great spy..'
                 elif 3.5<spy.rating<=5.0:
                     print'Average spy.'
                 elif 2.5<spy.rating<=3.5:
                     print'Bad spy..'
                 else:
                     print'Who hired you...'
                 spy.is_online=True#check if spy is online
                 #str to concat string with integer/float..
                 print'Authentication is completed..Welcome '+ spy.name +'age: '+str(spy.age)+ 'rating: '+str(spy.rating)
                 spy_chat(spy.name,spy.age,spy.rating)#calling function spy_chat
             else:
                 print'You are not eligible to be a spy....'
        else:
             print'Invalid salutation...'
    else:
        print 'Oops please enter a valid name..'
else:
    print'Invalid entry...'

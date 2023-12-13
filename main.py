import pickle as p
import sys
import time
import connec as cc
import pwdGen as pd

#key is generated

#flags
ff = 0
fff = 0
g = 0
t = ""
ddc = ''
password = ''
masterPassword = ''
run = True
a = 5
b = 5
c = 5
e = 5
#creating variables file
with open('variables.dat', 'ab') as s:
    s.close()
with open('answers.dat', 'ab') as u:
    u.close()
f = open('variables.dat', 'rb')
dataBase = cc.db_to_list()


#class for password entry
class entry:

    def __init__(self, ID, name, link, email_used, password, web_name):
        self.ID = ID
        self.name = name
        self.link = link
        self.email_used = email_used
        self.password = password
        self.web_name = web_name


user = None

#intro
print(
    '================================================================================================================================================================================================================'
)
print("""\

                                                                 _       __               __   __               __            
                                                                | |     / /___  _________/ /  / /   ____  _____/ /_____  _____
                                                                | | /| / / __ \\/ ___/ __  /  / /   / __ \\/ ___/ //_/ _ \\/ ___/
                                                                | |/ |/ / /_/ / /  / /_/ /  / /___/ /_/ / /__/ ,< /  __/ /    
                                                                |__/|__/\\____/_/   \\__,_/  /_____/\\____/\\___/_/|_|\\___/_/     
                                                                        
                                                                                  A Anmol inc. product..
                    """)
print(
    '================================================================================================================================================================================================================'
)


#for menu input
def Menu():
    time.sleep(1)
    print(
        '================================================================================================================================================================================================================'
    )
    print(
        'where you want to go.... \n1. Add a new password \n2. View an existing password\n3. View all Passwords\n4. Change existing password\n5. Delete a password\n6. To Change the masterPassword\n7. To Exit'
    )  #services
    print(
        '================================================================================================================================================================================================================'
    )
    n = input(
        'please enter the following serial number of the service you want: ')
    if n == '1' or n == '2' or n == '3' or n == '4' or n == '5' or n == '6' or n == '7':
        o = int(n)
        return o


def recovery():
    with open('answers.dat', 'rb') as s:
        v = []
        l = p.load(s)
        for i in l:
            v.append(pd.ascii_to_str(i)[0])
        return v
        #pd.checker()


#if statement for checking if the master password is not setup

try:
    while True:
        enc = pd.ascii_to_str(p.load(f))
        ddc = enc
except EOFError:
    print('')

if ddc == '':
    while ff == 0:
        print('')
        masterPassword = input('set a new master password:')
        confirmPassword = input('confirm master password:')

        if masterPassword == confirmPassword and masterPassword != '':
            print('You have succesfully setup your master password!')
            L = pd.questions()
            with open('variables.dat', 'ab') as k:
                p.dump(pd.str_to_ascii(masterPassword), k)
            with open('answers.dat', 'wb') as d:
                v = []
                for i in L:
                    v.append(pd.str_to_ascii(i))
                p.dump(v, d)
            break
        else:
            print('Invalid Option Entered!')
            ff = 0
            continue

f.seek(0)
with open('variables.dat', 'rb') as o:
    try:
        while True:
            enc = pd.ascii_to_str(p.load(o))
            password = ''.join(enc)
    except EOFError:
        print('')

#main menu loop
while run is True:
    g = Menu()
    #adding a new password
    if g == 1:
        a = 5
        while a > 0:
            i = input('Enter Master Password: ')
            #adding password
            if i == password:
                #takes input from user ad puts in it inside the table
                n = input('give website name: ')
                k = input('give website link: ')
                m = input('give the emailused: ')
                pw = pd.generator()
                u = input('enter username: ')
                user = entry(pd.ID(), n, k, m, pw, u)
                cc.insert_val(user.ID, user.web_name, user.name, user.password,
                              user.link, user.email_used)
                break
            else:
                a -= 1
                print(f'You Have {a} attempts left')
                if a == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    #view a specific password
    elif g == 2:
        while b > 0:
            l = input('Enter Master Password: ')
            if l == password:
                find = input('enter website name: ')
                for i in dataBase:
                    if i['website_name'] == find:
                        n = cc.get_val(i['website_name'])
                        pd.print_dictionary(n)
                break
            else:
                b -= 1
                print(f'You Have {a} attempts left')
                if b == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    #view all passwords
    elif g == 3:
        while b > 0:
            i = input('Enter Master Password: ')
            if i == password:
                n = cc.print_table()
                c = 1
                for i in n:
                    print(f"Entry No.{c}")
                    pd.print_dictionary(i)
                    print(c)
                    c = c + 1
                break
            else:
                b -= 1
                print(f'You Have {a} attempts left')
                if b == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    #update a password
    elif g == 4:
        while c > 0:
            i = input('Enter Master Password: ')
            if i == password:
                find = input('enter website name: ')
                for i in dataBase:
                    if i['website_name'] == find:
                        print(i['website_name'])
                        n = cc.change_val(i['website_name'])
                        print(n)
                break
            else:
                c -= 1
                print(f'You Have {a} attempts left')
                if c == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    #delete a password
    elif g == 5:
        while e > 0:
            i = input('Enter Master Password: ')
            if i == password:
                find = input('enter website name: ')
                for i in dataBase:
                    print(i['website_name'])
                    if i['website_name'] == find:
                        n = cc.delete_password(i['website_name'])
                        print(n)
                break
            else:
                e -= 1
                print(f'You Have {a} attempts left')
                if e == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    #change the masterpassword
    elif g == 6:
        while e > 0:
            i = input('Enter Master Password: ')
            if i == password:
                while fff == 0:
                    masterPassword = input('set up a new master password:')
                    confirmPassword = input('confirm master password:')
                    if masterPassword == confirmPassword:
                        print(
                            'You have succesfully changed your master password!,for changes to take effect , restart your application'
                        )
                        with open('variables.dat', 'wb') as k:
                            p.dump(pd.str_to_ascii(masterPassword), k)
                            k.close()
                        break
                    else:
                        print('Invalid Input!')
                        fff = 0
                        continue
                break
            else:
                e -= 1
                print(f'You Have {a} attempts left')
                if e == 0:
                    print('You have exceded the number of attempts')
                    run = False
                    break
    elif g == 7:
        print('Thank You For Using Password Manager \n Have A Nice Day :)')
        sys.exit()
    else:
        print('enter valid option')

#password recovery process
print('Since you forgot your password , we will ask questions to recover it')

z = pd.checker(recovery())

if z is True:
    while fff == 0:
        masterPassword = input('set up a new master password:')
        confirmPassword = input('confirm master password:')
        if masterPassword == confirmPassword:
            print(
                'You have succesfully changed your master password!,for changes to take effect , restart your application'
            )
            with open('variables.dat', 'wb') as k:
                p.dump(pd.str_to_ascii(masterPassword), k)
                k.close()
            break
        else:
            print('Passwords do not match!')
            fff = 0
            continue
else:
    print(
        'we are sorry that cannot be able to recover your passwords as you are maybe another user'
    )
    print(
        'if you are the owner of this account please contact us at mathapachi69@gmail.com'
    )

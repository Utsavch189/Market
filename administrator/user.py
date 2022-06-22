from django.core.mail import send_mail
import random
import string


def mail(email,name,role,username,password):
    subject=f'Approved By Admin for your {role} role'
    body=f'{name} Your login userID is: {username} and password is: {password}'
    mail_sender = 'utsavpokemon9000chatterjee@gmail.com'
    send_mail(subject, body, mail_sender, [email], fail_silently=False)


def Remail(email,name,password):
    subject=f'Password Recovery for {name}'
    body=f'{name} Your recovered login  password is: {password}'
    mail_sender = 'utsavpokemon9000chatterjee@gmail.com'
    send_mail(subject, body, mail_sender, [email], fail_silently=False)



def password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
    random.shuffle(characters)
    password = []
    for i in range(8):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ("".join(password))

def useID(name):
    tok=random.randint(111,999)
    return str(name).upper()+str(tok)


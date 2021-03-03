import requests
import os
import time
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
z = input("Enter your webhook: ")
y = input("Enter the username: ")
cls()
while True:
    x = input("Webhook ~> ")
    requests.post(z,json={'content': x, 'username': y})
    cls()
    time.sleep(0.0000000001)
    
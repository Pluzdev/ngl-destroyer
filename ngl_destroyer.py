import requests
import os
import random
from pystyle import Colors, Colorate
import time
import sys

def read_messages_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.readlines()
    return [message.strip() for message in messages]

def ngl():
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'
    B = '\033[34m'

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Vertical(Colors.blue_to_purple, """
    ##  ##    #####    ###              #####    ######    ######  ######   ######    #####    ## ##   ######   ######
    ### ###  #######   ###               #####    ######  ######    ######  ### ###  ### ###  ### ###   ######  ### ### 
    ### ###  ###       ###               ## ###   ##      ##         ###    ###  ##  ### ###  ### ###   ##      ###  ##
    #### ##  ##  ###  ###      ######    ##  ##  ######   #####      ###    ### ###  ##   ##  #######  ######   ### ###
    ## ####  ##   ##  ###       ######  ###  ##  #####     #####     ###    ######   ##   ##   ## ###  #####    ######
    ### ###  ### ###  ### ###           ### ###  ###          ###    ###    ### ###  ### ###      ###  ###      ### ###
    ### ###  #######  #######           ######   #######   ######    ###     ### ### #######  #######  #######   ### ###
    ##  ##   ######   #####            #####     #####   ######    #####    ### ###  #####    #####    #####    ### ###
        """))

    nglusername = input(Colorate.Vertical(Colors.blue_to_purple, "Username:"))
    messages = read_messages_from_file('messages.txt') 
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple, "Count: ")))


    total_messages_sent = 0
    total_messages_in_file = len(messages)
    live_statistics = ''

    print(" ")
    print(G + "Process started... Enjoy!")
    print(G + "CTRL + C to stop the process.")
    print(" ")

    value = 0
    notsend = 0

    while value < Count:
        message = random.choice(messages)
        headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
        if response.status_code == 200:
            notsend= 0 
            value += 1  
            total_messages_sent += 1
            live_statistics = f"{total_messages_sent}/{Count}"
            live_percentage = f"({(total_messages_sent / Count) * 100:.2f}%)"
            print(G + "[+]" + W + " Message: " + B + message + W + "  Sent: " + B + live_statistics + W + "  Percentage: " + B + live_percentage + W)
        else:
            notsend += 1
        if notsend == 10:
            print(R + "[!]" + W + " Ratelimited.. Waiting 5 Seconds")
            time.sleep(5)
            notsend = 0

    output_filename = f"output_logs.txt"

    with open(output_filename, 'a') as file:
        file.write(f"Username: {nglusername}\n")
        file.write(f"Total messages sent: {total_messages_sent}/{Count}\n")
        file.write(f"Total messages in file: {total_messages_in_file}\n")
        file.write(f"Date: {time.strftime('%d/%m/%Y %H:%M:%S')}\n\n")

    print(" ")
    print(G + "Process finished!")

ngl()


### Coded by 0MeMo07 and Pluz
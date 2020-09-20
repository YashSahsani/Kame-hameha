import PySimpleGUI as sg

sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Oops, looks like your files have been corrupted \nWhat happened to my computer?', font = '20' , text_color = 'white', background_color='maroon' )],
            [sg.Text("Your important files are encrypted. \nMany of the Documnets, photos, videos, databases and other files are no longer \naccesible because they have been encrypted. Maybe you are busy looking for a way to \nrecover your files, but do not waste your time. Nobody can recover your files without our decryption service.")],
            [sg.Text('Can i recover my Files?', font='16', text_color='white', background_color='maroon')],
            [sg.Text("Sure, We guarantee that you can recover all your files safely and easily. But you have \nnot so enough time. \nYou can decrypt some of your files for free. Try now by clicking <Decrypt>. \nBut if you want to decrypt all of your files, you need to pay. \nYou only have 3 days to submit the payment. After that the price will be doubled. \nAlso, if you dont pay in 7 days, you wont be able to recover your files forever. \nWe will have free events for users who are so poor that they couldn't pay in 6 months.")],
            [sg.Text('How do i Pay?', font='16', text_color='white', background_color='maroon')],
            [sg.Text('Below is the address where you can pay with bitcoins')],
            [sg.Text('Bitcoin Address: 151amaAjamfafa2665aaJoafaFjpajfnaifaJFNajf ', font='14', text_color='white', background_color='maroon')],
            [sg.Button('Check Payment'), sg.Button('Decrypt')] ]

# Create the Window
window = sg.Window('Kamehameha', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
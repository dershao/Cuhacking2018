import result, time, datetime, webbrowser
from plyer import notification

def sendNotification(result):
    result[0] = 'afraid' if result[0] == 'fear' else result[0]
    result[0] = 'surprised' if result[0] == 'surprise' else result[0]

    chat = 'https://feelsgoodchat.herokuapp.com/chat/'

    notification.notify(
        title = 'feelsgood',
        message = 'You look ' + result[0] + '.You should check out this link: ' + result[1],
        app_name = 'feelsgood'
    )

    time.sleep(5)

    webbrowser.open(result[1])

    notification.notify(
        title = 'feelsgood',
        message = 'You can join the private chat room at ' + chat + ' to share your thoughts',
        app_name = 'feelsgood',
    )

currtime = time.time()
end_hour = datetime.datetime.now().hour + 1 if (datetime.datetime.now().hour + 1) < 24 else 0
scan = True
while(True):
    if scan == True:
        sendNotification(result.getResult())
        scan = False

    if time.time() - currtime > 10:
        scan = True
        end_hour = datetime.datetime.now().hour + 1 if (datetime.datetime.now().hour + 1) < 24 else 0

    currtime = time.time()

    if datetime.datetime.now().minute == end_hour:
        end_hour = datetime.datetime.now().hour + 1 if (datetime.datetime.now().hour + 1) < 24 else 0
        scan = True

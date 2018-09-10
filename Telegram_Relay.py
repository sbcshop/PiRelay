import time, datetime
import PiRelay
import telepot
from telepot.loop import MessageLoop

relay1 = PiRelay.Relay("RELAY1")
relay2 = PiRelay.Relay("RELAY2")
relay3 = PiRelay.Relay("RELAY3")
relay4 = PiRelay.Relay("RELAY4")

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: %s' % command)

    if 'ON' in command:
        message = "Turned ON "
        if 'Relay 1' in command:
            message = message + "Relay 1"
            relay1.on()
        elif 'Relay 2' in command:
            message = message + "Relay 2"
            relay2.on()
        elif 'Relay 3' in command:
            message = message + "Relay 3"
            relay3.on()
        elif 'Relay 4' in command:
            message = message + "green "
            relay4.on()
        elif 'all' in command:
            message = message + "all Relay's"
            relay1.on()
            relay2.on()
            relay3.on()
            relay4.on() 
        telegram_bot.sendMessage (chat_id, message)

    if 'OFF' in command:
        message = "Turned OFF "
        if 'Relay 1' in command:
            message = message + "Relay 1"
            relay1.off()
        if 'Relay 2' in command:
            message = message + "Relay 2"
            relay2.off()
        if 'Relay 3' in command:
            message = message + "Relay 3"
            relay3.off()
        if 'Relay 4' in command:
            message = message + "Relay 4"
            relay4.off()
        if 'all' in command:
            message = message + "all Relay's "
            relay1.off()
            relay2.off()
            relay3.off()
            relay4.off()
        telegram_bot.sendMessage (chat_id, message)

telegram_bot = telepot.Bot('Enter your API Key')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Running....')

while 1:
    time.sleep(10)

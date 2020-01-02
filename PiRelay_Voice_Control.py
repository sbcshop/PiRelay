import speech_recognition as sr
import time, datetime
import PiRelay
import re

relay1 = PiRelay.Relay("RELAY1")
relay2 = PiRelay.Relay("RELAY2")
relay3 = PiRelay.Relay("RELAY3")
relay4 = PiRelay.Relay("RELAY4")

sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()

device_id = 0
mic_list = sr.Microphone.list_microphone_names()
for mic in mic_list:
    if mic == 'Yeti Stereo Microphone: USB Audio (hw:0,0)':
        device_id = mic_list.index(mic)

while True:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                        chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print("you said: " + text)
        if re.search("rel", text):
            if re.search('on', text):
                if re.search("1", text):
                    print("Turn On Relay 1")
                    relay1.on()
                elif re.search("2", text):
                    print("Turn On Relay 2")
                    relay2.on()
                elif re.search("3", text):
                    print("Turn On Relay 3")
                    relay3.on()
                elif re.search("4", text):
                    print("Turn On Relay 4")
                    relay4.on()
                elif re.search("all", text):
                    print("Turn On All Relay")
                    relay1.on()
                    relay2.on()
                    relay3.on()
                    relay4.on()

            if re.search('off', text):
                if re.search("1", text):
                    print("Turn Off Relay 1")
                    relay1.off()
                elif re.search("2", text):
                    print("Turn Off Relay 2")
                    relay2.off()
                elif re.search("3", text):
                    print("Turn Off Relay 3")
                    relay3.off()
                elif re.search("4", text):
                    print("Turn Off Relay 4")
                    relay4.off()
                elif re.search("all", text):
                    print("Turn Off All Relays")
                    relay1.off()
                    relay2.off()
                    relay3.off()
                    relay4.off()


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    except AssertionError:
        print("Problem with Audio Source")
        break
import pywhatkit
import time

# Store all numbers as string
data = open("paste_all_numbers_here.txt", "r").read()
message = open("message_text.txt", "r").read()

numbers = []

x = data.split()
for i in range(len(x)):
    if len(x[i]) != 13:
        print("Wrong number:",x[i])
    else:
        numbers.append(x[i])


for i in range(len(numbers)):
    phonenumber = numbers[i]

    # Send message without image
    #pywhatkit.sendwhatmsg_instantly(phonenumber, message, 9, True, 3)

    # Send message with image
    pywhatkit.sendwhats_image(phonenumber, "img.jpeg", message, 9, True, 3)

    time.sleep(0.01)
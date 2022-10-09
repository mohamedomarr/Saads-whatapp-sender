import pywhatkit
import time

# Store all numbers as string
data = open("paste_all_numbers_here.txt", "r").read()
message = open("message_text.txt", "r").read()

numbers_list = []

x = data.split()
for i in range(len(x)):
    if len(x[i]) != 13:
        print("Wrong number:",x[i])
    else:
        numbers_list.append(x[i])

numbers = list(dict.fromkeys(numbers_list))

for i in range(len(numbers)):
    phonenumber = numbers[i]

    # Send message without image
    #pywhatkit.sendwhatmsg_instantly(phonenumber, message, 9, True, 3)

    # Send message with image
    #pywupdhatkit.sendwhats_image(phonenumber, "img.jpeg", message, 9, True, 3)

    time.sleep(0.01)
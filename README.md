# Saad's Whatsapp bulk sender
A command line python application that sends a specific message to a group of people individually. 

## Prerequisites

 - Make sure you have [Python](https://www.python.org/downloads/) installed
- Make sure your whatsapp account is opened on your browser

## Getting Started
1- First download the package through the green code button => Download Zip => unzip that file
#### or using the command line enter 
```bash
git clone https://github.com/mohamedomarr/Saads-whatapp-sender
```
2- Navigate to that file in the command line using
```bash
cd Saads-whatapp-sender-main
```
3- Create a Python virtual environment and install the dependencies

### - For Mac/Linux
1- Create the virtual environment
```bash
python -m venv env
```
2- Activate the environment
```bash
source env/bin/activate
```
3- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pywhatkit package
```bash
pip install pywhatkit
```

### - For Windows
1- Create the virtual environment
```bash
python -m venv env
```
2- Activate the environment
```bash
env/Scripts/Activate.ps1
```
- Click and 
3- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pywhatkit package
```bash
pip install pywhatkit
```
4- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pywin32 package
```bash
pip install pywin32
```

## Usage
1- Navigate to the code file and activate the environment

2- Add all the numbers from the sheets to the paste_all_numbers_here.txt file
```python
+20###########
+20###########
+20###########
+20###########
```
3- Write the message you want to send in message_text.txt file
```python
Hello here's a message
welcome
```
4- If you need to attach a photo add it to the same file and rename it to img.jpeg

5- If you want to send a message with text only uncomment line 22 in main.py as follwing
```python
for i in range(len(numbers)):
    phonenumber = numbers[i]

    # Send message without image
    pywhatkit.sendwhatmsg_instantly(phonenumber, message, 9, True, 3)

    # Send message with image
    #pywhatkit.sendwhats_image(phonenumber, "img.jpeg", message, 9, True, 3)

    time.sleep(0.01)
```

6- If you want to send a message with text only uncomment line 25 in main.py as following
```python
for i in range(len(numbers)):
    phonenumber = numbers[i]

    # Send message without image
    #pywhatkit.sendwhatmsg_instantly(phonenumber, message, 9, True, 3)

    # Send message with image
    pywhatkit.sendwhats_image(phonenumber, "img.jpeg", message, 9, True, 3)

    time.sleep(0.01)
```


## License
Made with 🖤 by Mohamed omar

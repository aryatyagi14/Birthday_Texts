What is this Project?
    This project was a fun little side project for me to see if I can automate something I usually forget 
to do. I have a terrible memory when it comes to remembering birthdays and I always feel horrible when I 
realize I forgot to wish them a Happy Birthday. This solves that issue. I get to make the person I love feel 
appreciated as well as not have to worry about missing another important date! 

How it works!
    How it works is pretty simple. The SendiMessage.app is what actually connects to iMessage and sends the 
message through your account. The callSendiMessage.py handles all the other logic. It creates a list of 
messages to pick from so its not the same boring message everytime and it also creates a list of birthdays
you want to keep track of. It then loops through all the birthdays in the list and checks to see if the date
today is someones birthday. If it is, it sends a randomly chosen message from the messages list to the 
recipient. This script (callSendiMessage.py) will run once everyday if you set up the Cron Job as described 
below.

Requierements for Use
    1. You need to be running this on a MacOS system and that system must be signed into the iMessage account
you want the message to be sent from. 
    2. To have this run everyday you must set up Cron Job. This is pretty simple and I will walk you through
it step by step here:
        - Run command: which python 
            (output should be something like /usr/bin/python3)
        - Run Command in the folder where callSendiMessage.py is: pwd
            (output should be something like /path/to/your/script.py)
        - Open the Crone for editing. Run this Command in the terminal: crontab -e
        - Add this line to the file 0 0 * * * /usr/bin/python3 /path/to/your/script.py
            (the 0 0 represent the min and hour the script will run respectively, if added as so it will
            run at 12:00 am everyday)
        - Close file and Save

You can test run this project by using this command:
python callSendiMessage.py

from datetime import datetime

# writes 'Hello Name' in log.txt file with current timestamp
import random as rand
names = ['Dhruv','dhruv','DHRUV', 'Dhruv Prajapati', 'DHRUV']
with open('./log.txt', 'a') as f:
    f.write(f"{datetime.now()}: Hello {names[rand.randint(0,3)]}\n")

# from datetime import datetime

# writes 'hello world' in log.txt file with current timestamp
# with open('/tmp/log.txt', 'a') as f:
#     f.write(f"{datetime.now()}: hello world\n")

names = ['Dhruv','dhruv','DHRUV', 'Dhruv Prajapati', 'DHRUV']
import random as rand
print(f"Hello {names[rand.randint(0,3)]}")
from datetime import datetime
import time, random

odds = []
for num in range(1,60):
    if num%2 == 0:
        pass
    else:
        odds.append(num)


for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print(f'This minute {right_this_minute} seems a little odd ')
    else:
        print(f' {right_this_minute} is not an odd minute')
    
    wait_time = random.randint(1,6)
    time.sleep(wait_time)

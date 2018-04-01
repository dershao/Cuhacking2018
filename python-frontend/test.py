import time

while(True):
    currtime = time.time()
    while(time.time() - currtime < 2):
        print(time.time() - currtime)
        print('counting')

    print('2 sec')

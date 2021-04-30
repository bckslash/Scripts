import time, os
from threading import Thread

def clear(): 
	os.system('cls' if os.name == 'nt' else 'clear')

day, hours, minutes, seconds = 0, 0, 0, 0
run = True
pause = 1

def clock():
	global day, hours, minutes, seconds, run, pause

	while run:
		time.sleep(pause)
		seconds += 1
		if seconds == 60:
			minutes += 1
			seconds = 0
			if minutes == 60:
				hours += 1
				minutes = 0
				if hours == 24:
					day += 1
					hours, minutes, seconds = 0, 0, 0
		clear()
		print("Day: {}\n{}:{}:{}".format(day,hours, minutes, seconds))

def main_thread():
    while True:
        x = input("Press a key: \n")
        if x == "q":
        	run = False

if __name__ == '__main__':
    # create another Thread object
    # daemon means that it will stop if the Main Thread stops
    th = Thread(target=clock(), daemon=True)
    th.start()  # start the side Thread
    main_thread()  # start main logic

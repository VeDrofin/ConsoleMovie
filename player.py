import os
import time
import cursor

frame = open('text.txt', 'r')
conf = open('configuration.txt', 'r')

cols, lines = conf.readline().split(' ')
cols, lines = int(cols), int(lines)
fps = int(conf.readline())
amount_frame = int(conf.readline())

os.system("mode con cols={0} lines={1}".format(cols, lines-1))

start = time.time()
cursor.hide()
for i in range(0, amount_frame):
    while(time.time() - start < i*(1/fps)):
        pass
    text = frame.readline()
    print(text[0: cols*lines], end='')
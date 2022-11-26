import cv2
from PrintingToTheConsole import PrintPicture
import os

# chars to load
char = ("/", "-", "\\", "|")

# program operation status output function
def load(number_frame, i, count_frame):
    if(number_frame % i == 0):
        os.system('cls')
        print(' ')
        print('{0} '.format(char[number_frame%4]), end='') # spinner - load
        print('{0}%\t'.format(int(number_frame/count_frame*100)), end = '') # percent
        print('{0}/{1}\t'.format(number_frame, count_frame), end='') # ratio
        print('|{}| '.format('█'*int(20*number_frame/count_frame) + ' '*int(20-int(20*number_frame/count_frame))), end='') # progress bar
        print('{0}\t'.format(char[number_frame%4]), end='') # spinner - load

# recording frames in txt
def MakePNG(name, cols, lines):

    # getting video data
    video_capture = cv2.VideoCapture(name)
    fps = video_capture.get(cv2.CAP_PROP_FPS)  # OpenCV v2.x used "CV_CAP_PROP_FPS"
    count_frame = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = count_frame / fps

    # writing video data / made configuration
    configuration = open("configuration.txt", 'w')
    configuration.write('{0} {1}\n'.format(cols, lines))
    configuration.write('{}\n'.format(int(fps)))
    configuration.write('{}\n'.format(count_frame))
    configuration.write('{}\n'.format(duration))
    configuration.close()

    # writing a frame in the form of characters in a text document
    f = open("text.txt", "w")
    for number_frame in range(0, count_frame):
        ret, frame = video_capture.read()
        load(number_frame, 3, count_frame)
        cv2.imwrite(r'pic.png', frame)
        string = PrintPicture(cols, lines)
        f.write(string)
    f.close()

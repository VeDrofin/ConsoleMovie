from MakerPNG import MakePNG

def interface():
    print("1. Укажите путь к видео.")
    print(r"Например: .\Movies\NeverGonnaGiveYouUp.mp4")
    print(r"C:\Users\Rick\Movies\NeverGonnaGiveYouUp.mp4")
    path = input()
    print("2. Укажите размер консоли (через пробел).")
    size = input()
    cols, lines = size.split(' ')
    MakePNG(path, int(cols), int(lines))
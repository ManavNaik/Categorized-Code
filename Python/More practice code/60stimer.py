import time as t
import playsound as ps

try:
    for i in range (5):
        # t.sleep(1)
        print(i)

    print("Time up")
    ps.playsound('D:\coding\python by herry\Z My Works\MP3.wav')

except:
    print("error occured")
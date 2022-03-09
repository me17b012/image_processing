import subprocess
import ffmpeg
from keep_alive import keep_alive

class FFMScreenshot:

    def take_screenshot(self,input_file,output_file):
        try:
            command='ffmpeg -i ' + input_file+' -ss 00:00:03 -frames:v 1 '+ output_file
            subprocess.check_output(command,shell=True)
        except:
            print('screenshot taking failed')



#ffm=FFMScreenshot()
#ffm.take_screenshot('https://5f4ad95bcff44.streamlock.net:444/mtrosecam/mtrosecam.stream/chunklist_w799315300.m3u8','D:\Enhancement_code\Enhancements\screenshots\\foobar.jpeg')
import time

i=0
keep_alive()
while(True):
    ffm=FFMScreenshot()
    ffm.take_screenshot('https://5f4ad95bcff44.streamlock.net:444/mtrosecam/mtrosecam.stream/chunklist_w799315300.m3u8','D:\Enhancement_code\Enhancements\screenshots\\foobar_'+str(i)+'.jpeg')

    print(i)
    time.sleep(300)
    i=i+1

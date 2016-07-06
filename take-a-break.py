import time
import webbrowser
break_count = 0
total_breaks = 3
print ("This program started on : "+time.ctime())
while break_count < total_breaks:
    time.sleep(5)
    webbrowser.open ("https://www.facebook.com/")
    break_count+=1
    print ("five seconds over : "+time.ctime())

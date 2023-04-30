import os
import calendar
import time
import subprocess
import os
cmd1= 'systemctl --user restart indi-allsky'
cmd2= 'systemctl --user restart indiserver'


ct = 60
image = '/var/www/html/allsky/images/latest.jpg'


f = os.path.getmtime(image)
c = calendar.timegm(time.gmtime())
d = int(c - f)
#print(f)
#print(c)
#print(d)



while True:
    f = os.path.getmtime(image)
    c = calendar.timegm(time.gmtime())
    d = int(c - f)

    if d-ct > 0:
        print("Image too old, " + str(d) + " sec., restart service!")
        os.system(cmd1)
        # os.system(cmd2)
        time.sleep(240)
    else:
        print("Image is " + str(d) + " sec. old - ok.")
    time.sleep(30)


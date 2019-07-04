# take screenshot with python, linux only (X-server)
# https://pythonbasics.org
import os,sys,subprocess,pwd

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

user = get_username()
commandline = 'DISPLAY=:0 su %s -c "scrot /tmp/image.png"' % user
myprocess = subprocess.Popen(commandline,shell=True)
myprocess.wait()

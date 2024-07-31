import subprocess
import threading
import re

def getClipboardData():
    p = subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data.decode("utf-8")

clip = getClipboardData()
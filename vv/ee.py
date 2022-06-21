import os
import sys
print("sss")

def restart():
    import sys
    os.execl(sys.executable, sys.executable, *sys.argv)

restart()

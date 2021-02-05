from subprocess import Popen

while True:
    print("Starting...")
    p = Popen("python main.py", shell=True)
    p.wait()

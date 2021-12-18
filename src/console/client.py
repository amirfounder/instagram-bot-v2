import subprocess

def run_client():
    subprocess.Popen('npm --prefix src/console/client run start', shell=True)

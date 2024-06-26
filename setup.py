import os

missingLibrary = False
print("Verifying required libraries...")
try:
  import art
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U art")
  print("Done!")


try:
  import alive_progress
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("pip install -U alive-progress")
  print("Done!")


try:
  from bluetooth import *
  
except ModuleNotFoundError:
  missingLibrary = True
  print("Could not find a required library. Installing...")
  os.system("git clone https://github.com/pybluez/pybluez.git")
  os.system("python3 pybluez/setup.py install")
  os.sytsem("sudo rm -rf pybluez/")
  print("Done!")

print("Adding BlueDos to path")
os.system("mkdir /usr/lib/BlueDos")
os.system("cp -r * /usr/lib/BlueDos")
os.system("cp -r bin/BlueDos /usr/bin/")
os.system("chmod +x /usr/bin/BlueDos")

if missingLibrary:
  print("Restarting to refresh content...")
  import main
  exit()




# Fetch Installer
# Will detect your system, and run the command appropriotely.

import platform

system = platform.system().lower()

print("Detected OS: {}".format(system))

if system == "windows":
  os.system("powershell install.ps1")
elif system == "macos":
  os.system("bash install.bash")
elif system == "linux":
  os.system("bash install.bash")
else:
  os.system("Not supported, please use manual installation.")

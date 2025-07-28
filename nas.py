import subprocess
import getpass

user = input("enter user: ")
userPassword = getpass.getpass("enter password: ")
ipAdress = input("ip adress: ")


options = f"username={user},password={userPassword},noperm"

cmd = [
    "sudo",
    "mount",
    "-t",
    "cifs",
    f"//{ipAdress}/Public",
    "/home/pi/Partage",
    "-o",
    options,
]

res = subprocess.run(cmd, text=True, capture_output=True)

if res.returncode != 0:
    print("Erreur :", res.stderr.strip())
else:
    print("Monté !")

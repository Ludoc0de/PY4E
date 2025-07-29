import subprocess
import getpass

answer = input("Do you need to connect the nas: ").lower()
if answer == "yes" or answer == "oui":
    user = input("enter user: ")
    userPassword = getpass.getpass("enter password: ")
    ip = input("enter the NAS ip adress: ")

    options = f"username={user},password={userPassword},noperm"

    cmd = [
        "sudo",
        "mount",
        "-t",
        "cifs",
        f"//{ip}/Public",
        "/home/pi/Partage",
        "-o",
        options,
    ]

    res = subprocess.run(cmd, text=True, capture_output=True)

    if res.returncode != 0:
        print("Erreur :", res.stderr.strip())
    else:
        print("Connected !")

elif answer == "disconected" or answer == "d":
    cmd = [
        "sudo",
        "umount",
        "/home/pi/Partage",
    ]

    res = subprocess.run(cmd, text=True, capture_output=True)

    if res.returncode != 0:
        print("Erreur :", res.stderr.strip())
    else:
        print("Disconnected !")

else:
    print("Your answer its incorrect!")

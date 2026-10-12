import datetime
import os
import subprocess

# import termcolor

while True:
    # if datetime.datetime.now().minute == 0 or datetime.datetime.now().second == 0:
    #     # termcolor.cprint(
    #     #     datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    #     #     color="white",
    #     #     on_color="on_black",
    #     # )
    # else:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if os.name == "nt":
        # os.system("cls")
        subprocess.run("cls", check=True)
    else:
        # os.system("clear")
        subprocess.run("clear", check=True)

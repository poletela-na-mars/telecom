import os
import subprocess


def require_think_dsp():
    if not os.path.exists('thinkdsp.py'):
        # if on Windows, we use local executable of wget
        if os.name == 'nt':
            wget_path = os.path.abspath("../../util/wget.exe")
        else:
            wget_path = "wget"

        subprocess.call([
            wget_path,
            f"-P {os.path.abspath('')}",
            "https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py"
        ])
        print("thinkdsp.py successfully download")
    else:
        print("thinkdsp.py found")
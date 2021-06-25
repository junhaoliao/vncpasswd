from .vncpasswd import *


if __name__ == "__main__":
    import os
    from pathlib import Path

    default_vnc_path = str(Path.home()) + "/.vnc/"
    os.makedirs(default_vnc_path, exist_ok=True)

    default_passwd_path = default_vnc_path + "passwd"
    vncpasswd(default_passwd_path)

    # print(vncpasswd2plain(default_passwd_path))
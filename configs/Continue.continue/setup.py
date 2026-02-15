import os
import shutil

CONFIG_DIR = os.path.dirname(__file__)
DEST_DIR = os.path.join(os.path.expanduser("~"), ".continue")


def install() -> None:
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copy2(os.path.join(CONFIG_DIR, "config.yaml"), DEST_DIR)


def uninstall() -> None:
    dest = os.path.join(DEST_DIR, "config.yaml")
    if os.path.exists(dest):
        os.remove(dest)

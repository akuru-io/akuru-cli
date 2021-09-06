import sys

def install_font():
    platform = sys.platform
    if platform == 'darwin': #mac_os
        # download the font
        print("downloading font files")
        font_source = "https://github.com/mooniak/abhaya-libre-font/raw/master/fonts/ttf/AbhayaLibre-Regular.ttf"
        
        print("font installed", platform)
    elif platform == 'win32' or platform == 'cygwin':
        print("font installed", platform)
    
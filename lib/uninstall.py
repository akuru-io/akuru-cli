from send2trash import send2trash
import json
import os
import requests

def uninstall_font(font_name):
    print('> Uninstalling font')
    req = requests.get('https://github.com/akuru-io/font-lib-temp/raw/master/font_directory.json')
    data = req.json()
    fonts = data["fonts"]
    font_styles = get_font_styles(fonts, font_name)

    if font_styles is None:
        print("> Uninstall aborted: Unable to locate font styles for \"" + font_name + "\"")
        return

    os_font_dir = os.path.expanduser('~/Library/Fonts')
    for font_style in font_styles:
        font_name = font_style['fontUrl'].rsplit('/', 1)[1]
        uninstall_path = os.path.join(os_font_dir, font_name)
        if os.path.exists(uninstall_path):
            send2trash(uninstall_path)
            print('> Uninstalled ' + font_name)
        else:
            print('> Could not uninstall \"' + font_name + '\". Font not found in the system')
        

    print('> Uninstall complete')

def get_font_styles(font_data, font_name):
    print("> Searching for font \"" + font_name + "\"")
    try:
        f = next(font for font in font_data if font['familyName'] == font_name)
        return f['fontStyles']
    except:
        return None

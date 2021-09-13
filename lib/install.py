import sys
import requests
import json
import os

def install_font(font_name):
    tmp_folder_name = 'font_lib_tmp'
    platform = sys.platform
    if platform == 'darwin': #mac_os
        # download the font
        print("> Downloading font library data")
        req = requests.get('https://github.com/akuru-io/font-lib-temp/raw/master/font_directory.json')
        if req.status_code != 200:
            return

        json_data = req.json()
        fonts = json_data["fonts"]
        font_styles = get_font_styles(fonts, font_name)
        
        if font_styles is None:
            print("> Install aborted: Unable to locate font styles for \"" + font_name + "\"")
            return

        create_tmp_folder(tmp_folder_name)

        downloaded_fonts = []
        # download the font files
        for fontStyle in font_styles:
            font_req = requests.get(fontStyle['fontUrl'], allow_redirects=True)
            if font_req.status_code != 200:
                print('> Unable to locate '+ fontStyle['fontUrl'])
                continue

            fileName = fontStyle['fontUrl'].rsplit('/', 1)[1]
            filePath = os.path.join(tmp_folder_name, fileName)
            open(filePath, 'wb').write(font_req.content)
            downloaded_fonts.append(fileName)
            print('> Downloaded: ' + fileName)

        # install the fonts
        if len(downloaded_fonts) == 0:
            remove_tmp_folder(tmp_folder_name)
            print('> No font files downloaded. Aborting font installation')
            return
        
        os_font_dir = os.path.expanduser('~/Library/Fonts')
        for df in downloaded_fonts:
            install_path = os.path.join(os_font_dir, df)
            os.rename(tmp_folder_name+ '/' +df, install_path)
            print('> Installed: ' + df)
        
        # cleanup the temp folder
        remove_tmp_folder(tmp_folder_name)
        print("> Font installation completed")
    elif platform == 'win32' or platform == 'cygwin':
        print("> You are on Windows. This feature isn't implemented yet.", platform)
        return

def create_tmp_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def remove_tmp_folder(name):
    if os.path.exists(name):
        os.rmdir(name)

def get_font_styles(font_data, font_name):
    print("> Searching for font \"" + font_name + "\"")
    try:
        f = next(font for font in font_data if font['familyName'] == font_name)
        return f['fontStyles']
    except:
        return None
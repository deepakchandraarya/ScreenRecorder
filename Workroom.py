# Keyboard module in Python
from PIL import ImageGrab
import keyboard
import docx
docname = 'addImage.docx'
doc = docx.Document()
m = 0
while True:
    try:
        if keyboard.is_pressed('p'):
            image = ImageGrab.grab()
            m = m + 1
            pic = "axbcmxjk.png"
            image.save(pic)
            doc.add_picture(pic, width=docx.shared.Inches(07.0))
        elif keyboard.is_pressed('esc'):
            break

    except:
        break
doc.save(docname)
print(f'Total {m} screenshot are added in {docname}')
exit()

# press a to print rk
# keyboard.add_hotkey('a', lambda: keyboard.write('Geek'))

keyboard.add_hotkey('ctrl + shift + a', print, args=('you entered', 'hotkey'))

keyboard.wait('esc')

exit()
# Keyboard module in Python
import keyboard

# It records all the keys until escape is pressed
rk = keyboard.record(until='Esc')

# It replay back the all keys
keyboard.play(rk, speed_factor=1)
exit()

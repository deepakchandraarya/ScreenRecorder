# Keyboard module in Python
from PIL import ImageGrab
import keyboard
import docx
#docname = 'addImage.docx'
docname = input("Please Give word Document name :-  ")
doc = docx.Document()
m = 0
while True:
    try:
        if keyboard.is_pressed('ctrl + p'):
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
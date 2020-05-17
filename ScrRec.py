# Keyboard module in Python
from PIL import ImageGrab
import keyboard
import docx

class ScrRec:
    def __init__(self, basePath):
        self.basePath = basePath

    def recodSrc(self):
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
        doc.save(self.basePath)
        return

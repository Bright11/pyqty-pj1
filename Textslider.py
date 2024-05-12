from PyQt6.QtCore import QTimer

def Slider(slider_label):
    global count, text
    if count >= len(txt):
        count = -1
        text = ""
        slider_label.setText(text)
    else:
        text = text + txt[count]
        slider_label.setText(text)
    count += 1
    QTimer.singleShot(300, lambda: Slider(slider_label))

txt = "Welcome to pj1batteries and tech, contact Bright C Web Developer on 0558602996 ....".upper()
count = 0
text = ""

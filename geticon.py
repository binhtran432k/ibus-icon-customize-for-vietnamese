#!/bin/python
import sys
import os

file_path = os.path.dirname(os.path.abspath(sys.argv[0]))
def main(argv):
    if len(argv) == 0:
        icon_path = os.path.join(file_path, "themes/default")
        copy_icon(icon_path, "us.svg")
        copy_icon(icon_path, "vi.svg")
    elif len(argv) == 1:
        if argv[0] == "default":
            icon_path = os.path.join(file_path, "themes/default")
        elif argv[0] == "flag":
            icon_path = os.path.join(file_path, "themes/flag")
        elif argv[0] == "flag-circle":
            icon_path = os.path.join(file_path, "themes/flag-circle")
        else:
            print("python geticon.py [default,flag,flag-circle,text,color] [0x000000-0xffffff]")
            exit(1)
        copy_icon(icon_path, "us.svg")
        copy_icon(icon_path, "vi.svg")
    elif len(argv) == 2 and argv[1].startswith("0x"):
        if argv[0] == "text":
            icon_path = os.path.join(file_path, "themes/text")
        elif argv[0] == "color":
            icon_path = os.path.join(file_path, "themes/color")
        else:
            print("python geticon.py [default,flag,flag-circle,text,color] [0x000000-0xffffff]")
            exit(1)
        try:
            color = int(argv[1][2:],16)
        except:
            print("Color must be in hex!")
            exit(1)
        if color > 16**6:
            print("Color must be less than 0xffffff!")
            exit(1)
        copy_icon_with_color(icon_path, "us.svg", color)
        copy_icon_with_color(icon_path, "vi.svg", color)
    else:
        print("python geticon.py [default,flag,flag-circle,text,color] [0x000000-0xffffff]")
        exit(1)

def copy_icon_with_color(icon_path, icon_name, color):
    f = open(os.path.join(icon_path, icon_name), 'r')
    s = f.read()
    f.close()
    begin = s.find("#00ffff")
    end = begin + 7
    change = "#%0.6X" % color
    s = s[:begin]+change+s[end:]
    f = open(os.path.join(file_path, icon_name), 'w')
    f.write(s)
    f.close()

def copy_icon(icon_path, icon_name):
    f = open(os.path.join(icon_path, icon_name), 'r')
    s = f.read()
    f.close()
    f = open(os.path.join(file_path, icon_name), 'w')
    f.write(s)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])

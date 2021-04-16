import os
import sys
import errno
from datetime import datetime

ibus_component_path = '/usr/share/ibus/component'
ibus_icon_path = os.path.dirname(os.path.abspath(sys.argv[0]))
backup_path = os.path.join(
        os.getcwd()+"/backup", 
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

def main(argv):
    customize_bamboo()
    customize_simple()

def customize_bamboo():
    filename = ibus_component_path + '/bamboo.xml'
    f = open(filename, 'r')
    s = f.read()
    f.close()
    backup_component(s, "bamboo.xml")
    begini = s.find('<icon>')
    while begini != -1:
        begini += 6
        endi = s.find('</icon>', begini)
        new_change = ibus_icon_path + '/vi.svg'
        s = s[:begini] + new_change + s[endi:]
        begini = s.find('<icon>', begini+1)
    f = open(filename, 'w')
    f.write(s)
    f.close()

def customize_simple():
    filename = ibus_component_path + '/simple.xml'
    f = open(filename, 'r')
    s = f.read()
    f.close()
    backup_component(s, "simple.xml")
    enpos = s.find('<language>en</language>')
    begini = s.find('<icon>', enpos) + 6
    endi = s.find('</icon>', begini)
    new_change = ibus_icon_path + '/us.svg'
    s = s[:begini] + new_change + s[endi:]
    f = open(filename, 'w')
    f.write(s)
    f.close()

def backup_component(content, filename):
    try:
        os.makedirs(backup_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open(os.path.join(backup_path, filename), 'w') as fw:
        fw.write(content)

if __name__ == "__main__":
    main(sys.argv[1:])

import pyautogui
import clipboard
import time
import keyboard

print('Type 1 for cheque day close and 2 for return dayclose')
dayclose_type = input(':')
# dayclose_type = '1'
print(dayclose_type + ' ' + 'selected!!!')

def trim_special_char(txt):
    return txt.replace('\r','').replace('\n','').replace(',','').replace('-','')

def extract_cheque_no(txt):
    if '11001022-' in txt:
        txt=txt[txt.find('11001022-')+9:]
        cheque_no=txt[0:txt.find(' ')]
        return cheque_no
    else:
        cheque_no = ''
        for aa in txt:
            if aa.isdigit():
                cheque_no = cheque_no + aa
        return cheque_no

def single_alt_tab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    
def double_alt_tab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def bold():
    pyautogui.keyDown('ctrl')
    pyautogui.press('b')
    pyautogui.keyUp('ctrl')
    
def paste():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

while True:
    double_alt_tab()
    for i in range(4):
        pyautogui.press('tab')
            
    copy()
    double_alt_tab()
    clipboard.copy(extract_cheque_no(clipboard.paste()))
    paste()
    clipboard.copy('check condition')
    pyautogui.press('tab')
    pyautogui.press('esc')
    pyautogui.press('esc')
    time.sleep(0.4)
    copy()
    if 'check condition' not in clipboard.paste():
        input('Check number does not match !!!!.\n Continue after manual correction>>>')
        continue
    single_alt_tab()    
    bold()

    if dayclose_type == '1':
        pyautogui.press('tab')
        pyautogui.press('tab')
    elif dayclose_type == '2':
        pyautogui.press('tab')

    copy()
    single_alt_tab()
    pyautogui.typewrite(trim_special_char(clipboard.paste()))
    
    clipboard.copy('check condition')
    pyautogui.press('tab')
    pyautogui.press('esc')
    pyautogui.press('esc')
#     time.sleep(0.5)
    copy()
    if 'check condition' not in clipboard.paste():
        input('Amount does not match !!!!.\n Continue after manual correction>>>')
        continue
    
    single_alt_tab()
    pyautogui.press('esc')
    pyautogui.press('enter')
    single_alt_tab()
    double_alt_tab()
    
    if keyboard.is_pressed('shift'):
        input('PAUSED...... Press enter to continue >>')
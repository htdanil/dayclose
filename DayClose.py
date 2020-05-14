import pyautogui
import clipboard
import time
import keyboard
import pandas as pd

sec = input('Enter seconds to pause. For example, in order to pause operation for 4 seconds enter 4. >>>')
if sec == '' or float(sec) < 0.9:
	sec = 0.9
else:
	sec = float(sec)

print('''
Developed by :- 
Anil Shrestha, Chief Treasury Comptroller, District Treasury Comptroller Office, Makawanpur
email:- official.mail@anilz.net
============================================================================================
Enter 1 for return dayclose and 2 for payment dayclose.
Copy the excel data range without header and press enter.

Note:- The first column of the range should have cheque/voucher no information.
The second column of the range should have deposited amount.
The third column of the range should have payment amount.
============================================================================================
''')

dayclose_type = input(':')
# print(dayclose_type + ' ' + 'selected!!!')

def trim_special_char(txt):
	return txt.replace('\r','').replace('\n','').replace(',','').replace('-','')

def extract_cheque_no(txt):
	if '-' in txt:
		txt=txt[txt.find('-')+1:]
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
	
def copy():
	pyautogui.keyDown('ctrl')
	pyautogui.press('c')
	pyautogui.keyUp('ctrl')
  
def paste():
	pyautogui.keyDown('ctrl')
	pyautogui.press('v')
	pyautogui.keyUp('ctrl')

do_alt_tab = True

while True:
	df = pd.read_clipboard(header=None)
	pyautogui.alert('{} records to enter!!!'.format(df.shape[0]))
	
	for i in range(df.shape[0]):

		if do_alt_tab == True:
			do_alt_tab = False
			single_alt_tab()

		cheque_no = extract_cheque_no(str(df.iat[i,0]))
		clipboard.copy(cheque_no)

		if keyboard.is_pressed('shift'):
			pyautogui.alert('PAUSED...... Press OK to continue >>')
		paste()

		# clipboard.copy('check condition')
		pyautogui.press('tab')
		# time.sleep(0.2)
		# pyautogui.press('esc')
		# time.sleep(0.2)
		# pyautogui.press('esc')
		# time.sleep(0.2)
		# copy()

		# if 'check condition' not in clipboard.paste():
		# 	input('Check number {} does not match !!!!. Continue after manual correction>>>'.format(cheque_no))
		# 	do_alt_tab = True
		# 	continue

		amount = trim_special_char(str(df.iat[i,int(dayclose_type)]))

		if float(amount) == 0:
			continue

		if keyboard.is_pressed('shift'):
			pyautogui.alert(text='PAUSED...... Press OK to continue >>')

		if str(dayclose_type) == '1':
			amount = '-{}'.format(str(amount))

		clipboard.copy(amount)
		paste()
		
		clipboard.copy('check condition')
		pyautogui.press('tab')
		time.sleep(sec - 0.6)
		pyautogui.press('esc')
		time.sleep(0.3)
		pyautogui.press('esc')
		time.sleep(0.3)
		copy()
		if 'check condition' not in clipboard.paste():
			single_alt_tab()
			cc = input(f'\n => Amount of {df.iat[i,int(dayclose_type)]} does not match for cheque number {cheque_no} !!!!.\nContinue after manual correction \n OR type restart to restart the process again>>>')
			if cc == 'restart':
				break

			do_alt_tab = True
			continue
		
		if keyboard.is_pressed('shift'):
			pyautogui.alert('PAUSED...... Press enter to continue >>')


	single_alt_tab()
	input('End of the record.!!! Please copy another excel range for entering data or close the program to exit.')
	do_alt_tab = True
from colorama import init
from colorama import Fore, Back, Style
from time import sleep
import os

init()

def update():
	os.system("./upt")

def blue_text(text = str()):
	print(Fore.BLUE + text)

def red_text(text2 = str()):
	print(Fore.RED + text2)	

def white_text(text3 = str()):
	print(Fore.WHITE + text3)

def green_text(text4 = str()):
	print(Fore.GREEN + text4)

def yellow_text(text5 = str()):
	print(Fore.YELLOW + text5)			

def cyan_text(text6 = str()):
	print(Fore.CYAN + text6)	

def magenta_text(text7 = str()):
	print(Fore.MAGENTA + text7)	

def black_text(text8 = str()):
	print(Fore.BLACK + text8)

def blue_back(text9 = str()):
	print(Back.BLUE + text9)

def red_back(text10 = str()):
	print(Back.RED + text10)

def white_back(text11 = str()):
	print(Back.WHITE + text11)

def green_back(text12 = str()):
	print(Back.GREEN + text12)	

def yellow_back(text13 = str()):
	print(Back.YELLOW + text13)	

def cyan_back(text14 = str()):
	print(Back.CYAN + text14)	

def magenta_back(text15 = str()):
	print(Back.MAGENTA + text15)

def black_back(text16 = str()):
	print(Back.BLACK + text16)

def dim(text17 = str()):
	print(Style.DIM + text17)	

def normal(text18 = str()):
	print(Style.NORMAL + text18)

def bright(text19 = str()):
	print(Style.BRIGHT + text19)

def reset_all(text20 = str()):
	print(Style.RESET_ALL + text20)	

def blue_pixel(text21 = str()):
	print(Fore.BLUE + 
		Back.BLUE + 
		text21)

def red_pixel(text22 = str()):
	print(Fore.RED +
		Back.RED +
		text22)	

def white_pixel(text23 = str()):
	print(Fore.WHITE +
		Back.WHITE +
		text23)

def green_pixel(text24 = str()):
	print(Fore.GREEN +
		Back.GREEN +
		text24)

def yellow_pixel(text25 = str()):
	print(Fore.YELLOW +
		Back.YELLOW +
		text25)	

def cyan_pixel(text26 = str()):
	print(Fore.CYAN +
		Back.CYAN +
		text26)	

def magenta_pixel(text27 = str()):
	print(Fore.MAGENTA +
		Back.MAGENTA +
		text27)

def black_pixel(text28 = str()):
	print(Fore.BLACK +
		Back.BLACK +
		text28)

def print_vert(print_vert = str(), sec = int()):

	for i in print_vert:
		sleep(sec)
		print(i)

def print_hor(print_hor = str(), sec2 = int()):

	for j in print_hor:
		sleep(sec2) 
		print(j, end = "", flush = True )
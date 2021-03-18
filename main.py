import os, shutil, colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

user = os.getlogin()
PATHC, PATHD = (f"C:\\Users\\{user}\\Documents\\ShareX\\Screenshots", f"D:\\Users\\{user}\\Documents\\ShareX\\Screenshots")

if os.path.exists(PATHC):	
	screenshot_path = os.path.join(PATHC)
	shutil.rmtree(screenshot_path, ignore_errors=True)
	print(f"{Fore.GREEN}Wiped")
elif os.path.exists(PATHD):
	screenshot_path = os.path.join(PATHD)
	shutil.rmtree(screenshot_path, ignore_errors=True)
	print(f"{Fore.GREEN}Wiped")
else:
	print(f"{Fore.RED}Screenshot folder not found")

print("laptop repo")
import os
import shutil


COLOR_DEFAULT = '\x1b[0m'
COLOR_RED = '\x1b[31;31m'
COLOR_GREEN = '\x1b[31;32m'

def create_directory(name: str) -> None:
	if not os.path.exists(name):
		os.makedirs(name)

def copy_file(name: str) -> None:
	if not os.path.exists(name):
		shutil.copyfile(os.path.join(os.path.dirname(__file__), name), name)
		print(f'Copy "{name}"... {COLOR_GREEN}success{COLOR_DEFAULT}')
	else:
		print(f'Copy "{name}"... {COLOR_RED}fail{COLOR_DEFAULT}')

def main():
	create_directory('src')
	copy_file('run')
	copy_file('.env')
	copy_file('.coveragerc')
	copy_file('Dockerfile')
	copy_file('requirements.txt')
	print('If you want to initialize those file, remove them and execute this command again.')

if __name__ == '__main__':
	main()

import os
import shutil


def copy_non_existent_directory(name: str) -> None:
	if not os.path.exists(name):
		os.makedirs(name)

def copy_non_existent_file(name: str) -> None:
	if not os.path.exists(name):
		shutil.copyfile(f'py-run/{name}', name)

def main():
	shutil.copyfile('py-run/run', 'run')
	copy_non_existent_directory('src')
	copy_non_existent_file('.env')
	copy_non_existent_file('.coveragerc')
	copy_non_existent_file('Dockerfile')
	copy_non_existent_file('requirements.txt')

if __name__ == '__main__':
	main()

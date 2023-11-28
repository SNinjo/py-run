import pathlib
from setuptools import setup, find_packages
 

HERE = pathlib.Path(__file__).parent.resolve()
requirements = (HERE / 'py-run' / 'requirements.txt').read_text(encoding='utf8')

setup(
    name='py-run',
    version='1.0.3',
    description='',
    long_description=(HERE / 'README.md').read_text(encoding='utf8'),
    long_description_content_type='text/markdown',

    license='Apache',
    author='SNinjo',
    author_email='SNinjo657@gmail.com',
    url='https://github.com/SNinjo/py-run',
    download_url='https://pypi.org/project/py-run/',

    python_requires='>=3.8',
    install_requires= [s.strip() for s in requirements.split("\n")],
    packages=find_packages(),
    classifiers=[f'Programming Language :: Python :: 3.{str(v)}' for v in range(8, 12)],

	package_data={
		'py-run': [
			'*',
			'.*',
		],
	},
)
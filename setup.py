from setuptools import setup, find_packages

version = "1.0.2"

setup(
	name='templatebot',
	version=version,
	packages=find_packages(),
	url='https://github.com/vcokltfre/template-bot-v2',
	license='MIT',
	author='vcokltfre',
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=[open("requirements.txt").read().split("\n")],
	description='A template Discord bot',
	python_requires='>=3.6',
)
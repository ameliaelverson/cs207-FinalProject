import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "autodiff32",
	version = "0.1.0",
	author = "Amelia Elverson, Aaron Jacobson, Eric Moreira, Lin Zhu",
	author_email = "aelverson@mba2020.hbs.edu",
	description = "Automatic Differentiator",
	url = "https://github.com/ELAA207/cs207-FinalProject",
	packages = setuptools.find_packages(),
	install_requires=[
		'numpy'],
	long_description = long_description,
	long_description_content_type = "text/markdown",
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	],
	python_requires='>=3.6',
)

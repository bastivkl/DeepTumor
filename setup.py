import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DeepTumor-bastivkl", 
    version="0.0.1",
    author="Sebastian Völkl",
    author_email="bastivoelkl@gmail.com",
    description="Detecting brain tumors in MRI data based on a deep learning model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bastivkl/DeepTumor",
    project_urls={
        "Bug Tracker": "https://github.com/bastivkl/DeepTumor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
from setuptools import setup, find_packages

setup(
    name='json2yolo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python>=4.1.2",
        "pandas",
        "Pillow",
        "pyYAML",
        "requests",
        "tqdm"
    ]
)

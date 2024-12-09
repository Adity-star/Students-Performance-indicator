from setuptools import find_packages, setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return a list of requirements needed for the project.'''
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

            if hypen_e_dot in requirements:
                requirements.remove(hypen_e_dot)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return requirements

setup(
    name="MLprojects",
    version='0.0.1',
    author="Aditya",
    author_email='aakuskar.980@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

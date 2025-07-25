from setuptools import find_packages,setup
from typing import List

# HYPEN_E_DOT = '-e .' # It is a second method to install packages.

def get_requirements(file_path:str)->list[str]:   # This function will return the list of requirements.
    
     requirements = []
     
     with open(file_path) as file_obj:
         requirements = file_obj.readlines()
         requirements = [req.replace('\n', '') for req in requirements]
         
    
         
         # if HYPEN_E_DOT in requirements:   # It is a second method to install packages.
             # requirements.remove(HYPEN_E_DOT) 
             
     return requirements
         
        

setup(
    name= 'Datascience Project',
    version = '0.01',
    author= 'Kumaraswami',
    author_email='kumaraswamy2686@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
     
    
)
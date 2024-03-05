# Find all the packages in the entire machine learning application directory that we created
from setuptools import find_packages, setup 
from typing import List 

HYPEN_E_DOT = '-e .'

# To automatically download all the packages listed
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read each line inside requirements.txt
        requirements = file_obj.readlines()
        # Replacing '\n' added after every line with ' '
        requirements = [req.replace("\n","") for req in requirements]

        # -e . should not come when we are actually running requiremnets.txt its just to connect setup.py and requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Metadata imformation about the entire project
setup(
    name    = 'mlproject',
    version = '0.0.1',
    author  = 'Ritika',
    author_email = 'ritikag5533@gmail.com',
    # find_packages() will see in how many folders we have __init__.py file
    packages = find_packages(),
    # Mention all the package requirements
    install_requires = get_requirements('requirements.txt')
)
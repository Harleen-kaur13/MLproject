from setuptools import find_packages,setup
from typing import List

e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this fn will return the list of requirements
    '''
    req=[]
    with open(file_path)as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","")for r in req]
        if e_dot in req:
            req.remove(e_dot)
    return req

setup(
    name='MLproject',
    version='0.0.1',
    author='Harleen',
    author_email='harleen1302@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)
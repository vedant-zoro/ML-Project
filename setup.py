from setuptools import find_packages,setup 
from typing import List


HE_DOT = '-e .'

def get_requirments(file_path:str)-> list[str]:

    requirments = []
    with open (file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments =[req.replace ("\n","") for req in requirments ]

        if HE_DOT in requirments:
            requirments.remove(HE_DOT)

    return requirments

setup(
name="MLProject",
version='0.0.1',
author='vedant',
author_email='vedantkadam996@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirment.txt')

)
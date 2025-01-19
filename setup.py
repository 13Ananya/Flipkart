from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    
    #This function will return list of requierments from requirements.txt file
    requirement_list:List[str] = []
    #Read the requirements.txt file and append it to requirement_list variable
    return requirement_list

setup(
    name="flipkart",
    version="0.0.1",
    author="Ananya",
    author_email="shettyananya130603@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
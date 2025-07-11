from setuptools import find_packages, setup
from typing import List

HYPEN = "-e."


def get_requirement(file_path: str) -> List[str]:
    """"""

    """"""
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]
        if HYPEN in requirement:
            requirement.remove(HYPEN)
    return requirement


setup(
    name="mlproject",
    version="0.0.1",
    author="saroja",
    author_email="sarojapatra2021@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirement.txt"),
)

from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='congestion',
      version="0.0.0",
      description="Le Wagon Project",
      license="MIT",
      author="Mayank Soni",
      author_email="mayank.soni101@gmail.com",
      url="https://github.com/mayank-soni/congestion",
      install_requires=requirements,
      packages=find_packages(),
    #   test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
    #   include_package_data=True,
    zip_safe=False
    )

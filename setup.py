from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='matsutil',
    url='https://github.com/aventadoro-ish/matsutil',
    author='Matvey',
    # author_email='jladan@uwaterloo.ca',
    # Needed to actually package something
    packages=['TextMenu', 'Table', 'Utility'],
    # Needed for dependencies
    # install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1.4',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read()
)
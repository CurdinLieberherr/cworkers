from setuptools import setup 
  
setup( 
    name='cworkers', 
    version='0.1', 
    description='Simply simulation of workers who work or take vacation.', 
    author='Curdin Lieberherr', 
    author_email='curdin.lieberherr@bdo.ch', 
    packages=['cworkers'], 
    install_requires=[ 
        'numpy', 
        'pandas', 
        'simpy'
    ], 
) 

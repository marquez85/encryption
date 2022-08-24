from setuptools import setup

setup(
   name='encryption',
   version='1.0',
   description='essencial py files to run to connect plaxis',
   author='PLAXIS_FM',
   author_email='fpvsm85@gmail.com',
   py_modules=['example'],
   entry_points={
       'console_script':[
           'encryption=encryption',
           ],
       },
)
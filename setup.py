from distutils.core import setup
setup(
  name = 'database_pandas',         
  packages = ['database_pandas'],  
  version = '0.1.3',      
  license='MIT',        
  description = 'Package for working with databases in Python, based on pandas and sqlalchemy.',  
  author = 'Daniil Yefimov',                  
  author_email = 'daniil.yefimov92@gmail.com',     
  url = 'https://github.com/danilyef/database_pandas',   
  download_url = 'https://github.com/danilyef/database_pandas/archive/refs/tags/v.0.1.3.tar.gz',    
  keywords = ['Database', 'MySQL', 'Python','pandas'],   
  install_requires=[            
          'numpy',
          'pandas',
          'sqlalchemy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

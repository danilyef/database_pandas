from distutils.core import setup
setup(
  name = 'database_pandas',         
  packages = ['database_pandas'],  
  version = '1.0.3',      
  license='MIT',        
  description = 'Package for working with databases in Python, based on pandas and sqlalchemy.',  
  author = 'Daniil Yefimov',                  
  author_email = 'daniil.yefimov92@gmail.com',     
  url = 'https://github.com/danilyef/database_pandas',   
  download_url = 'https://github.com/danilyef/database_pandas/archive/refs/tags/v.1.0.3.tar.gz',    
  keywords = ['Database', 'MySQL', 'Python','pandas'],   
  install_requires=[            
          'numpy==1.21.6',
          'pandas==1.3.5',
          'sqlalchemy==1.4.39',
          'mysql-connector-python==8.0.30'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',     
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)

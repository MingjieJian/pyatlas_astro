import subprocess
import os
import setuptools

if os.environ.get('READTHEDOCS') != 'True':
    # Define pyatlas_astro_path. This path will store the code of pyatlas_astro and any other temporary files in the calculation.
    pyatlas_astro_path = os.getenv('PYATLAS_PATH')
    if pyatlas_astro_path is None:
      pyatlas_astro_path = '{}/.pyatlas_astro/'.format(os.environ['HOME'])
    elif pyatlas_astro_path[-1] != '/':
      pyatlas_astro_path += '/'
    
    file_list = {'atlas/src/atlas9/':{'atlas9mem.for':'http://wwwuser.oats.inaf.it/castelli/sources/atlas9g/atlas9mem.for', 
                                     'atlas9v.for':'http://wwwuser.oats.inaf.it/castelli/sources/atlas9g/atlas9v.for'}, 
                 'atlas/src/atlas12/':{'atlas12.for':'http://wwwuser.oats.inaf.it/castelli/sources/atlas12/atlas12.for', 
                                      'diatomicspack.for':'http://wwwuser.oats.inaf.it/castelli/sources/atlas12/diatomicspack.for', 
                                      'nltelinesasctobin.for':'http://wwwuser.oats.inaf.it/castelli/sources/atlas12/nltelinesasctobin.for'}, 
                 'atlas/src/dfsynthe/':{
                                      #  'xnfdf.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/xnfdf.for',
                                      #  'dfsynthe.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/dfsynthe.for',
                                      #  'dfsortp.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/dfsynthe.for',
                                      #  'separatedf.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/separatedf.for',
                                      #  'repacklow.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repacklow.for',
                                      #  'repackhi.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repackhigh.for',
                                      #  'repackdi.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repackdi.for',
                                      #  'repacktio.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repacktio.for',
                                      #  'repackh2o.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repacktio.for',
                                      #  'repacknlte.for':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/repacknlte.for'
                                       }, 
                 'atlas/src/kappa9/':{'kappa9.for':'http://wwwuser.oats.inaf.it/castelli/sources/kappa9/kappa9.for', 
                                     'kapreadts.for':'http://wwwuser.oats.inaf.it/castelli/sources/kappa9/kapreadts.for'}, 
                 'atlas/dist/atlas9/':{}, 
                 'atlas/dist/atlas12/':{}, 
                 'atlas/dist/dfsynthe/':{}, 
                 'atlas/dist/kappa9/':{}, 
                 'atlas/assets/common/':{'fclowlines.bin':'http://kurucz.harvard.edu/linelists/linescd/fclowlines.bin', 
                                         'fchilines.bin':'http://kurucz.harvard.edu/linelists/linescd/fchighlines.bin',
                                         'tioschwenke.bin':'http://kurucz.harvard.edu/molecules/tio/tioschwenke.bin', 
                                         'h2ofastfix.bin':'http://kurucz.harvard.edu/molecules/h2o/h2ofastfix.bin', 
                                         'nltelines.asc':'http://kurucz.harvard.edu/linelists/linescd/nltelines.asc',
                                         'molecules.dat':'http://wwwuser.oats.inaf.it/castelli/sources/atlas9/molecules.dat'},
                 'atlas/assets/atlas9/':{},
                 'atlas/assets/atlas12/':{'diatomics.asc':'http://kurucz.harvard.edu/molecules/oldandnew/diatomics.asc'},
                                         # 'nltelines.asc':''}, 
                 'atlas/assets/dfsynthe/':{
                                          # 'lowlines.bin':'http://kurucz.harvard.edu/LINELISTS/LINESCD/lowlines.bin',
                                          # 'highlines.bin':'http://kurucz.harvard.edu/LINELISTS/LINESCD/highlines.bin', 
                                          # 'fclowlines.bin':'', 
                                          # 'fchighlines.bin':'', 
                                          # 'diatomicsiwl.bin':'http://wwwuser.oats.inaf.it/castelli/linelists/diatomicsiwl.bin', 
                                          # 'continua.dat':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/continua.dat', 
                                          # 'pifron.dat':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/pfiron.dat', 
                                          # 'molecules.dat':'http://wwwuser.oats.inaf.it/castelli/sources/dfsynthe/molecules.dat',
                                          # 'tioschwenke.bin':'http://kurucz.harvard.edu/MOLECULES/TiO/tioschwenke.bin', 
                                          # 'h2ofastfix.bin':'http://kurucz.harvard.edu/MOLECULES/H2O/h2ofastfix.bin', 
                                          # 'nltelines.asc':'http://kurucz.harvard.edu/LINELISTS/LINESCD/nltelines.asc'
                                          },
                 'atlas/assets/common/kappa/':{}, 
                 'atlas/assets/common/odf/':{}}
    folders = list(file_list.keys())
    
    # Create the folder according to pyatlas_astro_path
    for folder in folders:
      md_status = subprocess.run(['mkdir', '-p', pyatlas_astro_path + folder], stdout=subprocess.PIPE)
    
    # Download code and supplementary files and arrange them to correct place.
    for folder in folders:
        files = list(file_list[folder].keys())
        # for single_file in files:
        #     print("Download file {} to {}".format(file_list[folder][single_file], pyatlas_astro_path+folder))
        #     wget_status = subprocess.run(['wget', '-cN', file_list[folder][single_file], '-P', pyatlas_astro_path+folder])
    
    # Compile files.
    # Copy the make files into folders.
    copy_status = subprocess.run(['cp', 'pyatlas_astro/files/makefile/Makefile_overall', pyatlas_astro_path+'atlas/Makefile'])
    copy_status = subprocess.run(['cp', 'pyatlas_astro/files/makefile/Makefile_src_atlas', pyatlas_astro_path+'atlas/src/atlas9/Makefile'])
    copy_status = subprocess.run(['cp', 'pyatlas_astro/files/makefile/Makefile_src_atlas', pyatlas_astro_path+'atlas/src/atlas12/Makefile'])
    copy_status = subprocess.run(['cp', 'pyatlas_astro/files/makefile/Makefile_assets_atlas12', pyatlas_astro_path+'atlas/assets/atlas12/Makefile'])
    copy_status = subprocess.run(['cp', 'pyatlas_astro/files/makefile/Makefile_assets_common', pyatlas_astro_path+'atlas/assets/common/Makefile'])
    
    # Make
    copy_status = subprocess.run(['make', '-C', pyatlas_astro_path+'atlas/'])
    
    
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='pyatlas_astro',
      version='0.0.1',
      description='The python3 wrapper to run LTE stellar atmosphere model generation code ATLAS and others.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/MingjieJian/pyatlas_astro',
      author='Mingjie Jian',
      author_email='ssaajianmingjie@gmail.com',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: IPython",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Scientific/Engineering :: Astronomy"
      ],
      python_requires=">=3.5",
      packages=setuptools.find_packages(),
      install_requires=[
          'numpy >= 1.18.0',
          'pandas >= 1.0.0',
          'matplotlib >= 3.1.0',
          'mendeleev >= 0.6.0',
          'scipy >= 1.4.0',
          'astropy >= 4.0',
          'pymoog'
      ],
      include_package_data=True,  
    #   package_data={'': ['moog_nosm/moog_nosm_FEB2017/']},
      zip_safe=False)
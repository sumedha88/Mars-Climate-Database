# Mars-Climate-Database

Instructions on how to install and use MCD on macOS (with mcd-python GitHub repo instead of python3 instructions provided with the distribution). Check which version you are running, accordingly file names and directories will change. These instructions are for MCD v6.1.

* Download MCD source files from http://www-mars.lmd.jussieu.fr (v6.1) and save it on local machine ~/MCD6.1/MCD6.1
* Download additional scenarios and save in data folder of downloaded distribution, ~/MCD6.1/MCD6.1/data
* Download gitHub repo mcd-python from https://github.com/aymeric-spiga/mcd-python (Test codes are in python2 and don’t work directly with python3 - not needed), saved in ~/MCD6.1/mcd-python  
* Download Homebrew, and use brew install netcdf to install netCDF libraries (have to switch to admin for permission, su guptaad), or install using MacPorts.
* In /mcd-python/compile_fmcd.sh, define paths of netcdf and MCD source files - 
    - NETCDF=/opt/local/        
    - wheremcd=~/MCD6.1/MCD6.1/
* In bash-profile, define python paths 
    - export PYTHONPATH=$PYTHONPATH:~/opt/anaconda3/bin
    - export PYTHONPATH=$PYTHONPATH:~/MCD6.1/MCD6.1/mcd
    - export PYTHONPATH=$PYTHONPATH:~/MCD6.1/MCD6.1/mcd/interfaces/python
    - export PYTHONPATH=$PYTHONPATH:~/MCD6.1/mcd-python
    - export PATH=$PATH:/opt/local (netcdf path)
    - Remove the path of the version that you are not using
* Link MCD data to working directory ~/MCD6.1/mcd-python/ 
    - ln -s ~/MCD6.1/MCD6.1/data MCD_DATA
* Compile and create python interface, sh compile_fmcd.sh 
    - This should create .so .log .pyf files, otherwise something is wrong (in the same folder mcd-python)
* Test from fmcd import mcd, then mcd.call_mcd to execute. There should be no error.
* To use MCD with python3, use the following imports and paths in any code, 
    - path_dir = '~/MCD6.1/mcd-python/'
    - sys.path.append(path_dir)
    - from fmcd import mcd
    - dset = '~/MCD6.1/MCD6.1/data/' # default to 'MCD_DATA'
    - Follow the variable declarations and usage as given in ~/MCD6.1/mcd-python/test_mcd/test_mcd_light.py




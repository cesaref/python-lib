import os

os.system ("rm -rf install")
os.system ("git clone https://github.com/python/cpython.git")
os.chdir ("cpython")
os.system ("git checkout v3.13.5")
os.system ("MACOSX_DEPLOYMENT_TARGET=14.0 ./configure --prefix=$PWD/../install")
os.system ("MACOSX_DEPLOYMENT_TARGET=14.0 make -j8")
os.system ("make install")

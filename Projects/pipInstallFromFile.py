#! python3

# importing sys, and either version of pip
import sys

try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

# calls install on string
def install(package):
    pipmain(['install', package])

# when running this code with one parameter, 
# it installs all packages contained the supplied file name,
if __name__ == '__main__':
    if len(sys.argv) == 3:
        pipFile = open(sys.argv[2], 'r')
        packages = pipFile.readlines()
        for package in packages:
            install(str(package))
        pipFile.close()
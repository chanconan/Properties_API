# Properties_API
In order to run this simple API endpoint script, there are a few packages that are necessary. 
Following the steps provided by the following will get started with having Python3 installed on MacOS
https://docs.python-guide.org/starting/install3/osx/

1. Install GCC on MacOS
First, install Xcode to obtain GCC on MacOS. 
2. Once Xcode has been installed, install Homebrew
It is possible to install Homebrew using the following command from the terminal
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
3. Once Homebrew has been installed, install Python 3
https://www.python.org/downloads/
4. Check to see if Python 3 has been installed
python3 --version
5. Once Python 3 has been installed, you will need to install Flask Restful and Pandas in order to run the script. 
pip3 install flask-restful pandas
6. After installing the packages, run the application
python3 api_endpoints
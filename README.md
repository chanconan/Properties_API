# Properties API
In order to run this simple API endpoint script, there are a few packages that are necessary. 
Following the steps provided by the following will get started with having Python3 installed on MacOS
https://docs.python-guide.org/starting/install3/osx/

1. Install GCC on MacOS
First, install Xcode to obtain GCC on MacOS. 
2. Once Xcode has been installed, install Homebrew
It is possible to install Homebrew using the following command from the terminal
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
3. Once Homebrew has been installed, install Python 3
```
https://www.python.org/downloads/
```
4. Check to see if Python 3 has been installed
```
python3 --version
```
5. Once Python 3 has been installed, you will need to install Flask Restful and Pandas in order to run the script. 
```
pip3 install flask flask-restful pandas
```
6. After installing the packages, run the application
```
python3 api_endpoints
```

For Testing, I used Postman and the browser for quick testing purposes
https://www.postman.com/
There are three main endpoints for functionality
```
/properties
/properties/<int: id>
/properties/vote/<int: id>
```
1. The ```GET request /properties``` will return an dictionary object with all the properties sorted from newest to oldest listing
2. By providing a JSON payload in the ```POST request /properties```, it is possible to update the column of which the sort will occur. 
```
{
    "sortBy": "net",
    "ascending": "false"
}
```
The sortBy field values can be ```price, bedrooms, net, total``` depending on what column to sort by.

3. The ```GET request /properties/<int: id>``` will return a dictionary object for a single property with all the columns provided by the CSV. 
4. Lastly, the ```POST request /properties/vote/<int: id>``` takes in a JSON payload for either ```upvote``` the property or ```downvote```.
```
{
    "vote": "downvote"
}
```

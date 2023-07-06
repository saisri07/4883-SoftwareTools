## Assignment 7   Web - Scrapping

## Sai Teja Sripathi

## Description:-

This application renders a web page using Selenium, and then parses the HTML using BeautifulSoup. The parsed HTML is then printed to the console. Creating a gui to retrieve values for the characteristics day, month, year, ariport, and filter (only daily) using PySimpleGui. Utilize Selenium to dynamically retrieve data from Wunderground and display it in a table on the GUI.




## FILES
|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | [airports-better.json](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/airports-better.json)| file that holds airport code ,city and country |
|   2   |    [gui.py](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/gui.py)           |this file contain gui and driver code|
|   3   |    [Example 1a.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%201a.png)  |Example query 1
|   4   |    [Example 1b.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%201b.png)   |Example query 1 ouput
|   5   |    [Example 2a.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%202a.png)   |Example query 2
|   6   |    [Example 2b.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%202b.png)   |Example query 2 ouput
|   7   |    [Example 3a.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%203a.png)   |Example query 3
|   8   |    [Example 3b.png](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/Example%203b.png)   |Example query 3 ouput
|   9   |  [get_weather.py](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/get_weather.py)     | this file contain code to scrape and render data using beautsoup and selenium    |
|   10  | [requirements.txt](https://github.com/saisri07/4883-software-tools-sripathi/blob/main/Assignments/A07/requirements.txt)    | this file has list of dependencies for this project |


# Requirements:

* Python 3.x
* PySimpleGUI
* Selenium
* BeautifulSoup4


# Instructions:

* Install the required libraries by running pip3 install -r requirements.txt in your command line or terminal.
* Run the gui.py script to start the program.
* In the program's user interface, select the filter (currently only "daily" is available), an airport code, and a specific date.
* Click the "Submit" button.
* weather data will be displayed in a table format.




# Output:


# Example-1



<img width="516" alt="Example 1a" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/deb9af2d-9076-439a-bbbf-d74d529dfd4f">



<img width="808" alt="Example 1b" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/bffb982d-7927-4016-870f-82bd413e4f43">


# Example-2

<img width="492" alt="Example 2a" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/46bafad9-1497-4791-93d8-4162a19458fa">



<img width="809" alt="Example 2b" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/8aae7e86-12aa-4f05-b01f-52b29210e1f5">

# Example-3


<img width="516" alt="Example 3a" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/4936f70c-7e49-414c-a8fc-bb722d3e2a35">




<img width="843" alt="Example 3b" src="https://github.com/saisri07/4883-software-tools-sripathi/assets/36495909/bac48796-5b6d-4335-903f-aab7922400dc">







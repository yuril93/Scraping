#Title
README file for Kwame_Johnson_selenium.py python scritp.

##Description 
Scrip automaticaly login in to https://fjdefile.phila.gov/ site and scraping points below in a headless mode for "Case ID" which is manually given as a input:
In case if you are running the script for that day at the firs time it will create .csv file with date at front.
In case if you are rnnning the script for that day more then 1 time it will update existing .csv file with "Case ID" data.

*	Case ID
*	Case Caption
*	Court
*	Filling Date
*	Case Type
*	Case Status
*	Plaintiff
*	Defendant 1
*	Defendant 1 Address Line 1
*	Defendant 2
*	Defendant 2 Address Line 1
*	Defendant 3
*	Defendant 3 Address Line 1
*	Judgement Amount ($)

## Installation
1.	Install Python 3.6+
2.	Install Selenium "VERSION 3.141.0" or above
3.	Download webdriver for your browser (Google Chrome 12+,Internet Explorer 7,8,9,10,Safari 5.1+,Opera 11.5,Firefox 3+)
4. 	Copy Kwame_Johnson_selenium.py file in your path.

6.	Update following line in Kwame_Johnson_selenium.py file:
    Line 8:		csvPath
	Line 29:	executable_path for webdriver

## Usage
run Kwame_Johnson_selenium.py file.
	ex: python Kwame_Johnson_selenium.py , or just double click to Kwame_Johnson_selenium.py file
input "Case ID" number
	ex: 190901053



#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath, isfile
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime
# Import os path function.


#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################

date_list_items = \
['Sun, 15 Oct 2020',
'Mon, 16 Oct 2020',
'Tue, 17 Oct 2020',
'Wed, 18 Oct 2020',
'Thu, 19 Oct 2020',
'Fri, 20 Oct 2020',
'Sat, 21 Oct 2020',
'Latest']
head_template = """<!DOCTYPE html>
<html>

	<head>
	
		<!-- Title for browser window/tab -->
		<title>Daily Mail News Archive</title>
		
		<!-- Overall document style -->
		<style>
			body	{background-color: Linen}
			p		{width: 80%; margin-left: auto; margin-right: auto}
			h1		{width: 80%; margin-left: auto; margin-right: auto}
			h2		{width: 80%; margin-left: auto; margin-right: auto}
			h3		{margin-left: auto; margin-right: auto}
			li		{width: 80%; margin-left: auto; margin-right: auto}
		</style>
	
	</head>
	
	<body>
		
		<!-- Masterhead -->
		<h1>Daily Mail News Archive</h1>
		<!-- Record time -->
		<h2>***archiveDate***</h2>
		<!-- Daily Mail logo from http://i.dailymail.co.uk/i/sitelogos/dm-com-home.png -->
		<p><img src = "http://i.dailymail.co.uk/i/sitelogos/dm-com-home.png" alt = "Daily Mail Logo"</p>
		<p><strong>News source: </strong><a href = "http://www.dailymail.co.uk/articles.rss">http://www.dailymail.co.uk/articles.rss</a></p>
		<p><strong> Archivist: </strong> Danial Baharvand</p>
		<hr width= "80%">
		<ol>
"""

article_template = """
		<!-- A news article -->
		<!-- Headline -->
		<li><h3>***title***</h3></li>
		<!--  image illustrating the story -->
		<p><img src = "***picLink***" alt = "Photo is missing"</p></p>
		<!-- short summary of the story -->
		<p>***descriptions***</p>
		<!-- link to the full version of the story -->
		<p><strong>Full story: </strong><a href = "***fullStory***">***fullStory***</a></p>
		<!-- the date/time the story appeared online -->
		<p><strong> Dateline: </strong>***dateLine***</p>
		<hr width= "80%">
"""
def generate_html(extractedInfo): # Recieves extracted info from extractInfo and creates a html file with correct format
    # Assign values to variables 
    titles=extractedInfo[0]
    descriptions=extractedInfo[1]
    fullStory=extractedInfo[2]
    dateLine=extractedInfo[3]
    picLink=extractedInfo[4]
    archiveDate=dateLine[0]
    # Add header to variable and set archive date
    html_code = head_template.replace('***archiveDate***', date.get())
    # Produce the stories and add them to the code
    for index in range(10):
        articleCache=article_template
        articleCache=articleCache.replace('***title***', titles[index])
        articleCache=articleCache.replace('***picLink***', picLink[index])
        articleCache=articleCache.replace('***descriptions***', descriptions[index])
        articleCache=articleCache.replace('***fullStory***', fullStory[index])
        articleCache=articleCache.replace('***dateLine***', dateLine[index]) 
        html_code = html_code + articleCache
    # Add the finishing tags to the code
    html_code = html_code + """		</ol>
	</body>
    <html>"""
    # Write the HTML code to a file
    html_file = open('extracted.html', 'w')
    html_file.write(html_code)
    html_file.close()

def extractInfo (filePath): # Extracts info from a file at the given file path
    file_contents = open(filePath,'U', encoding='utf8',).read()
    titles = findall("<title>[\s]*([^\n<]+)[\s]*</title>", file_contents)[2:12]
    descriptions= findall("<description>[\s]*([^\n<]+)[\s]*</description>", file_contents)[1:11]
    fullStory= findall("<link>[\s]*([^\n<]+)[\s]*</link>", file_contents)[2:12]
    dateLine= findall("<pubDate>[\s]*([^\n<]+)[\s]*</pubDate>", file_contents)[1:11]
    picLink= findall('<media:content type="image/jpeg" url="([^\"]+)"/>', file_contents)[0:10]
    return titles, descriptions, fullStory, dateLine, picLink
def extractInfoButton():
    if isfile(internet_archive +'/'+ date.get()+'.html'):
        generate_html(extractInfo(internet_archive +'/'+ date.get()+'.html'))
        logEvent('Extracted news from the archive')
    else:
        logEvent('Attempted to extract news from archive but no file was found!')
        new_window = Toplevel()
        new_window.title('error')
        Label(new_window, text='Please download the latest news first').pack()
        Button(new_window, text = 'OK', command = new_window.destroy).pack()
        new_window.mainloop()
        
def openExtractButton():
    if isfile('extracted.html'):
        webopen(normpath(getcwd()+"/extracted.html"))
        logEvent('Extracted news displayed in web browser')
    else:
        logEvent('Attempted to display extracted news in web browser but no file was found!')
        new_window2 = Toplevel()
        new_window2.title('error')
        Label(new_window2, text='Please extract an archive first').pack()
        Button(new_window2, text = 'OK', command = new_window2.destroy).pack()
        new_window2.mainloop()
        
    
def archiveLatestButton():
    new_url = 'http://www.dailymail.co.uk/articles.rss'
    new_web_page = urlopen(new_url)
    new_web_page_contents = new_web_page.read().decode('UTF-8')
    new_html_file = open(internet_archive+'/Latest.html', 'w', encoding = 'UTF-8')
    new_html_file.write(new_web_page_contents)
    new_html_file.close()
    logEvent('Latest news downloaded and stored in archive')
def logEvent(comment):
    global keyNum
    global db_view
    global mydb 
    if log_checked.get() or comment=='Event logging switched off':
        keyNum=keyNum+1
        db_view.execute("""INSERT INTO Event_Log VALUES ('"""+str(keyNum)+"""', '"""+comment+"""')""")
        mydb.commit()
    else:
        pass
def startSql(): 
    if log_checked.get():
        logEvent('Event logging switched on')
    else:
        logEvent('Event logging switched off')
        
    
# Create a window
news_archivist = Tk()
# Give the window a title
news_archivist.title('News Archivist')
# Create a OptionMenu widget to display the choices of dates
date=StringVar(news_archivist)
log_checked = IntVar()
date.set(date_list_items[0]) # default value
dates_list = OptionMenu(news_archivist, date, *date_list_items)

mydb=connect('event_log.db')
db_view = mydb.cursor()

# create buttons
keyNum=0
extract_button = Button(news_archivist, text="Extract news from archive", command=extractInfoButton)
open_button = Button(news_archivist, text="Display news extracted", command=openExtractButton)
archive_latest_button = Button(news_archivist, text="Archive the latest news", command=archiveLatestButton)
daily_mail_image = PhotoImage(file = "logo.gif")
daily_mail_logo = Label(news_archivist, image = daily_mail_image)
log_check_box = Checkbutton(news_archivist, text="Log events", variable=log_checked, command=startSql)
daily_mail_logo.pack()
dates_list.pack()
archive_latest_button.pack()
extract_button.pack()
open_button.pack()
log_check_box.pack()
news_archivist.mainloop()















import webbrowser
url = 'https://epaper.eenadu.net'
print("-"*10,url,'-'*10,'\n') #Print '-' 10 times URL '-'10 times

browser_selection =int(input(" In which browser you want to see? \n\n 1 Google Chrome \n 2 Internet Explorer \n 3 Mozilla Firefox "))
#Take Browser Selction input from user

googlechrome=browser_selection
ie=browser_selection
firefox=browser_selection
if googlechrome == 1:
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #Path of Google Chrome in your system
    webbrowser.get(chrome_path).open(url)
elif ie == 2:
    ie_path = 'C:/Program Files/Internet Explorer/iexplore.exe %s' #Path of IE in your system
    webbrowser.get(ie_path).open(url)
elif firefox==3:
    firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s' #Path of Mozilla Firefox in your system
    webbrowser.get(firefox_path).open(url)
else:
    print("Enter 1 or 2 or 3 Numbers Only\nQUITTING!",sep=" ")

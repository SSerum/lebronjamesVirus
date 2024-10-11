import webbrowser
import time

url = 'http://your-url-here.com'

def open_tab():
    webbrowser.open(url)

while True:
    open_tab()
    print(f"Opened {url} in a new tab.")
    time.sleep(5)  # Wait a few seconds to simulate user closing the tab

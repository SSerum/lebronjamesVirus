import webbrowser
import time

url = 'https://www.youtube.com/shorts/ZeIr0FVJwGs'

def open_tab():
    webbrowser.open(url)

while True:
    open_tab()
    time.sleep(1)  # Wait a few seconds to simulate user closing the tab

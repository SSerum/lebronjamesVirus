import webbrowser
import time

url = 'https://www.youtube.com/shorts/ZeIr0FVJwGs'

def open_tab():
    webbrowser.open(url)

while True:
    open_tab()
    print(f"Opened {url} in a new tab.")
    time.sleep(5)  # Wait a few seconds to simulate user closing the tab

# Solution

```python
import webbrowser
import argparse

parser = argparse.ArgumentParser(description='Open a web page in your default browser.')
parser.add_argument('url', help='the URL of the webpage to open')
parser.add_argument('--new-window', action='store_true', help='open the webpage in a new window')

args = parser.parse_args()

url = args.url
new_window = args.new_window

try:
    if new_window:
        webbrowser.open_new(url)
    else:
        webbrowser.open(url)
except Exception as e:
    print("An error occurred:", e)
```

# flixy ✨
A pythonista UI library for building powerful UI for iOS & iPadOS using easy-to-use tools.
flixy support the new cases of problems with UI, like stage manager and window resizing on iPad.

## Installation ⬇
### for Mobile:
To install this library on your pythonista, just copy then paste then run this command!:
```python
import requests; exec(requests.get("https://bit.ly/flixy-installer").text);
```

Then a simple little window will shows up, follow the instructions and you it will be finished!

<img src="https://user-images.githubusercontent.com/86029286/230713728-41878deb-5714-4a85-a3b5-5225c33729da.png" data-canonical-src="[https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png](https://user-images.githubusercontent.com/86029286/230713728-41878deb-5714-4a85-a3b5-5225c33729da.png)" width="500" />

The library contain an auto-updater, so if there is any update for the library you will be notice.

### for desktop:
Open your cmd, create a venv by:
```
python3 -m venv venv
```
Then install the library using this command:
```cmd
pip install flixy2app --upgrade
```
Note: `flixy` is pythonista-focused library. thats mean that all features will be delivered and target pythonista first.

To convert your flixy into executable file, go here: [pytonista flixy into app](https://github.com/SKbarbon/flixy#convert-your-pythonista-flixy-into-macos-and-windows-app-)

## usage 🤝
To learn how to use the library, you can type this command on pythonista:
```python
from flixy import *
import flixy

flixy.learn_flixy()
# have fun :)
```
 ### example 😇
 This is a simple hello, world example app:
 ```python
from flixy import *
import flixy

def main (page:flixy.Page):
	page.add(Text("Hello, world!", expand_width=True))

flixy.app(target=main)
 ```
 Result:
 
<img src="https://user-images.githubusercontent.com/86029286/230714340-66fa77ee-9789-45d1-af73-79cda70a5550.jpeg" data-canonical-src="[[https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png](https://user-images.githubusercontent.com/86029286/230714340-66fa77ee-9789-45d1-af73-79cda70a5550.jpeg)]([https://user-images.githubusercontent.com/86029286/230713728-41878deb-5714-4a85-a3b5-5225c33729da.png](https://user-images.githubusercontent.com/86029286/230714340-66fa77ee-9789-45d1-af73-79cda70a5550.jpeg))" width="500" />

## Convert your pythonista flixy into macOS and windows app 🪄!!
1- install `flixy2app` using `pip` .

2- Bring your pythonista file.

3- Use this command: `python3 -m flixy2app.generate`. follow the Instructions, then done.

Note: This is BETA! thats mean it may be broken because its on the first releases. To support this project please create an issue if you find one.

## comming soon 🔜
- Support games develop. making `flixy.game` module.

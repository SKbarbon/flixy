# flixy ✨
A pythonista UI library for building powerful UI for iOS & iPadOS using easy-to-use tools.
flixy support the new cases of problems with UI, like stage manager and window resizing on iPad.

## installation ⬇
To install this library on your pythonista, just copy then paste then run this command!:
```python
import requests; exec(requests.get("https://bit.ly/flixy-installer").text);
```

Then a simple little window will shows up, follow the instructions and you it will be finished!

<img src="https://user-images.githubusercontent.com/86029286/230713728-41878deb-5714-4a85-a3b5-5225c33729da.png" data-canonical-src="[https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png](https://user-images.githubusercontent.com/86029286/230713728-41878deb-5714-4a85-a3b5-5225c33729da.png)" width="500" />

## usage 🤝
To learn how to use the library, you can type this command on pythonista:
```python
from flixy import learn
learn()
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
 


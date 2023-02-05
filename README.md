# flixy
A python library for pythonista iOS
This is a UI library based on the built-in pythonista library named ui.
This library provides powerful tools that help developers build graphical interfaces that work differently on all screen sizes but with the same lines of code, so there is no need to waste time working for each screen.

## Current features
- Easy to use.
- Support All screen sizes.
- Support Window resizing.
- Auto position its items using powerful tools.

## Comming soon features
- Support many built-in widgets (For example: Sound Player widget).
- Support macOS for non-pythonista use.


## How to install
### on pythonista
You can install the library using this code:
Put the code on a standalone file, not inside any sub-folders.

`
import requests; exec(requests.get("https://bit.ly/FlixyUI").text)
`

You can also install it from github here and then insert it manually on the `Python modules/site-package-3`

## Demo
This is a simple `Hello, world!` interface:

`

from flixy import *

def Home(view:View):
	view.add(Text("Hello, world!"))

app(target=Home)

`
[![asciicast](https://videos.files.wordpress.com/3EUWRjDy/rpreplay_final1675629474.mp4)

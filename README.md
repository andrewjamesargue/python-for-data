# Python for Data Analysis

## Setup instructions for Python and Virtual Studio Code:

## Download and install VS Code
Follow this link to install the latest version of VS Code:  
https://code.visualstudio.com/download

## Download and install Python 3
Follow this link to download Python version 3.11:  
https://www.python.org/downloads/

## Install Python extension for VS Code
![Extensions in VS Code](extensions-view-filter-menu.png "Search for Python")

## Open a Terminal window
In the menu bar select the following drop-down menus:
```
Terminal > New Terminal 
```

## Check what version of Python you have:
In the terminal type the following command:  

macOS:  
```
python --version
```

Windows:  
```
py --version
```

## Select Python interpreter
In the menu bar select the following drop-down menus:
```
View > Command Palette...
```

1) In the search bar of the command palette type "select interpreter"
2) Click the highlighted row under the search bar that says "Python: Select Interpreter"
3) Select the Python version 3.x.x that you want to use

## Install a python package called "pip"
In the VS Code terminal type:

macOS:  
```
python3 -m ensurepip --upgrade
```
```
python3 -m pip install --upgrade pip
```
  
Windows:
```
py -m pip install --upgrade pip
```

## Create a virtual environment using "venv"

In the VS Code terminal type:
```
python3 -m venv venv
```

## Change VS Code Python interpreter to venv version
Open the "command palette" in VS Code
In the menu bar select the following drop-down menus:
```
View > Command Palette...
```

In the search bar of the command palette type "select interpreter"
Click the highlighted row under the search bar that says "Python: Select Interpreter"
Find the Python version 3.x.x ('venv':venv) ./venv/bin/python

## Activate the virtual environment (Windows only)
In the terminal type:  

macOS:  
```
source venv/bin/activate
```

Windows:  
```
./venv/Scripts/activate
```
## If you need to exit the virtual environment
In the terminal type:  

```
deactivate
```

## Install a package
In the terminal type:

macOS:  
```
python3 -m pip install pandas
```

Windows:
```
py -m pip install pandas
```

## Check what packages are installed
In the terminal type:

macOS:
```
python3 -m pip freeze
```

Windows:
```
py -m pip install pandas
```






## Setup instructions for Python and Virtual Studio Code (macOS):

## Download and install VS Code
Follow this link to install the latest version of VS Code:  
https://code.visualstudio.com/download
****

## Download and install Python 3
Follow this link to download Python version 3.11:  
https://www.python.org/downloads/
****

## Install Python extension for VS Code
![Extensions in VS Code](/images/extensions-view-filter-menu.png "Search for Python")
****

## Open a Terminal window
In the menu bar select the following drop-down menus:  
`
Terminal > New Terminal 
`
****

## Check what version of Python you have:
In the terminal type the following command:
```
python --version
```
****

## Select Python interpreter
1) In the menu bar select the following drop-down menus:  
`
View > Command Palette...
`
2) In the search bar of the command palette type "select interpreter"
3) Click the highlighted row under the search bar that says "Python: Select Interpreter"
4) Select the Python version 3.x.x that you want to use
****

## Install a python package called "pip"
1) In the VS Code terminal type:
```
python3 -m ensurepip --upgrade
```
2) Then type
```
python3 -m pip install --upgrade pip
```
****

## Create a virtual environment using "venv"
In the VS Code terminal type:
```
python3 -m venv venv
```
****

## Change VS Code Python interpreter to venv version
1) Open the "command palette" in VS Code
2) In the menu bar select the following drop-down menus:  
`
View > Command Palette...
`
3) In the search bar of the command palette type "select interpreter"
4) Click the highlighted row under the search bar that says "Python: Select Interpreter"
5) Find the Python version 3.x.x ('venv':venv) ./venv/bin/python
****

## Activate the virtual environment (Windows only)
In the terminal type:  
```
source venv/bin/activate
```
****

## If you need to exit the virtual environment
In the terminal type:  
```
deactivate
```
****

## Install a package
In the terminal type:
```
python3 -m pip install jupyter
```
****

## Check what packages are installed
In the terminal type:
```
python3 -m pip freeze
```
****
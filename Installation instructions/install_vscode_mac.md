# macOS setup instructions for Python and VS Code:

## Download and install VS Code
Follow this link to install the latest version of VS Code:  
https://code.visualstudio.com/download

## Download and install Python 3
Follow this link to download Python version 3.11:  
https://www.python.org/downloads/

## Install Python extension for VS Code
![Extensions in VS Code](/images/extensions-view-filter-menu.png "Search for Python")

## Open a Terminal window
In the menu bar select the following from the drop-down menus:  
`
Terminal > New Terminal 
`

## Check what version of Python you have:
In the terminal type the following command:
```
python --version
```

## Select Python interpreter
1) In the menu bar select the following from the drop-down menus:  
`
View > Command Palette...
`
2) In the search bar of the command palette type "select interpreter"
3) Click the highlighted row under the search bar that says "Python: Select Interpreter"
4) Select the Python version 3.x.x that you want to use  
![Select the Python interpreter](/images/select-interpreter.png "Select the Python interpreter")

## Install a python package called "pip"
1) In the VS Code terminal type:
```
python3 -m ensurepip --upgrade
```
2) Then type
```
python3 -m pip install --upgrade pip
```

## Install a package called Jupyter
In the terminal type:
```
python3 -m pip install jupyter
```

## Check which packages that are installed so far
In the terminal type:
```
python3 -m pip freeze
```
# If you want to set up a virtual environment follow these instructions

## Make sure pip is up-to-date
In the VS Code terminal type:
```
python3 -m ensurepip --upgrade
```
Then type
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

## Activate the virtual environment

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
****
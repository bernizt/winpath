# winpath
Python script to get the path of a Windows file/folder inside the file system of Bash on Ubuntu on Windows

## What is it useful for?
Windows 10 Anniversary update brought a beta of the linux bash to Windows, under the name "Bash on Ubuntu on Windows". When you drag and drop a file or a folder to the bash window, you get the full path to the element in windows format. This is useless in linux as the paths follow a different format.

The host Windows 10 file system is mounted under /mnt/, which means that the Windows folder:
```
C:\Users\john\Albums
```
can be accessed in bash as:
```
/mnt/c/Users/john/Albums
```

## Usage
This Python module also install a global script *wp* which accepts a path in windows format and returns its bash equivalent. The path can be obtained by dragging and dropping a folder or a file into the bash window. For example
```
$ wp C:\\Users\john\Albums
/mnt/c/Users/john/Albums
```
```
$ ls $("wp "C:\Users\john\Albums"")
Please Please Me    A Hard Day's Nigh   Help!
```
**Note:** The windows path must be double-quoted or the backslashes will be stripped (error)

## Installation
Download/clone this repository and go to its directory inside bash. Then, install easy_install and winpath with the following commands:
```
sudo apt-get install python-setuptools
sudo easy_install .
```


# qd - Quick Change Directory

This is a utility that allows you to quickly jump to your favorite directories without having to write out the full path like you would using the standard cd command.

## Setup:
 - Clone this repo and add it to your `PATH`
 - Add the following line to your shell's config file: (*.bash_profile, .bashrc, .zprofile, .zshrc*)
```
alias qd="source qd.sh"
```
 - Open up a new terminal and give it a try using `qd`

![gif of example usage](https://github.com/Macuyler/qd/blob/development/usage.gif)


## Usage:
	- "$qd [path to search for]" normal operation
	- "$qd -ss or --set-shortcut [shortcut key]" set a keyword to a current working directory. Used to quickly cd to dir
	- "$qd -s --shortcut [shortcut key]" go to shortcut set by command above.
    - "qd -ls or --shortcut" list all set shortcuts
    - "qd -rs or --remove-shortcut [shortcut]" remove shortcut

## Notes:
 - Windows is not supported.
 - It seems that python caches the directories. So, the first time you run the command after boot it takes longer then normal operation.

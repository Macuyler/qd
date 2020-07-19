
# qd - Quick Change Directory

This is a utility that allows you to quickly jump to your favorite directories without having to write out the full path like you would using the standard cd command.

## Setup:
 - Clone this repo and add it to your `PATH` *OR* run the following commands:
```
sudo ln -s ./qd/qd.py /usr/local/bin
sudo ln -s ./qd/qd.sh /usr/local/bin
```
 - Add the following line to your shell's config file: (*.bash_profile, .bashrc, .zprofile, .zshrc*)
```
alias qd="source qd.sh"
```
 - Open up a new terminal and give it a try using `qd`

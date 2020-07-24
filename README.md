
# qd - Quick Change Directory

This is a utility that allows you to quickly jump to your favorite directories without having to write out the full path like you would using the standard cd command.

## Setup:
 - Clone this repo and add it to your `PATH`
 - Add the following line to your shell's config file: (*.bash_profile, .bashrc, .zprofile, .zshrc*)
```
alias qd="source qd.sh"
```
 - Open up a new terminal and give it a try using `qd`

## Notes:
 - Windows is not (yet) supported.
 - It seems that python caches the directories. So, the first time you run the command after boot it takes longer then normal operation.

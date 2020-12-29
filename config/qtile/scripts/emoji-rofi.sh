#!/bin/bash

choice=$(cat emoji-unicode | rofi -dmenu -p "Emoji:" | tr '\t' ' ' | cut -d ' ' -f 1)

if [ -n "$choice" ]
then
    echo $choice | xclip -selection clipboard
    notify-send "$(xclip -o -selection clipboard) Copied to clipboard"
fi

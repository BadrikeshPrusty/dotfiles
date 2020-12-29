#!/bin/bash

DMENU="dmenu -h 22 -i -l 20 -nb #191919 -nf #fea63c -sb #fea63c -sf #191919 -fn NotoMonoRegular:bold:pixelsize=14 -p "Fonts:""

choice=$(fc-list | cut -d ":" -f 1 | rev | cut -d '/' -f 1 | rev | $DMENU)

if [ -n "$choice" ]
then
    display "$(fc-list | cut -d ":" -f 1 | grep "$choice")"
fi

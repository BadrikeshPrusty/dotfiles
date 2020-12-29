#!/bin/bash

#function run {
#  if ! pgrep $1 ;
#  then
#    $@&
#  fi
#}

#Some ways to set your wallpaper besides variety or nitrogen
feh --bg-fill /home/badrikesh/Pictures/wallpapers/moon_orbiting_earth-wallpaper-3840x2160.jpg &

#starting utility applications at boot time
nm-applet &
xfce4-power-manager &
#run numlockx on &
#run blueberry-tray &
picom -b --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
#run optimus-manager-qt &

#starting user applications at boot time
#nitrogen --restore &
#run caffeine -a &
#run insync start &
redshift -P -O 3500 &
xinput set-prop "Elan Touchpad" "libinput Tapping Enabled" 1
xinput set-prop "Elan Touchpad" "libinput Natural Scrolling Enabled" 1

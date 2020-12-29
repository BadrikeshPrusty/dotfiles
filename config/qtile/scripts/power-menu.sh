#!/bin/bash

DMENU="dmenu -h 22 -i -nb #191919 -nf #fea63c -sb #fea63c -sf #191919 -fn NotoMonoRegular:bold:pixelsize=14 -p "Power:""
choice=$(echo -e "Lock\nSuspend\nHibernate\nLogout\nReboot\nShutdown\n" | $DMENU)

case "$choice" in
    Logout)
        killall qtile
        ;;
   
    Shutdown)
        systemctl poweroff
        ;;
      
    Reboot)
        systemctl reboot
        ;;
      
    Suspend)
        systemctl suspend
        ;;
      
    Hibernate) 
        systemctl hibernate
        ;;

    Lock)
        xfce4-screensaver-command --lock
        ;;
esac

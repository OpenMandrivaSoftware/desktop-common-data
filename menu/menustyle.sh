#!/bin/sh

if [ "$META_CLASS" = "desktop" ]; then 
	MDV_MENU_STYLE=discovery 
else
	MDV_MENU_STYLE=mandriva
fi

[ -r /etc/sysconfig/menustyle ] && source /etc/sysconfig/menustyle
[ -r $HOME/.menustyle ] && source $HOME/.menustyle

if [ "$MDV_MENU_STYLE" = "discovery" ]; then
	XDG_CONFIG_DIRS=/etc/xdg/discovery:/etc/xdg
	export XDG_CONFIG_DIRS
fi

export MDV_MENU_STYLE

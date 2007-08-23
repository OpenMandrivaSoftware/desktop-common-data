MDV_MENU_STYLE=mandriva

[ -r /etc/sysconfig/menustyle ] && source /etc/sysconfig/menustyle
[ -r $HOME/.menustyle ] && source $HOME/.menustyle

if [ "$MDV_MENU_STYLE" = "discovery" ]; then
	MDV_MENU_STYLE=mandriva
fi

export MDV_MENU_STYLE

#!/bin/csh
if ($META_CLASS == desktop ) then 
	set MDV_MENU_STYLE=discovery 
else
	set MDV_MENU_STYLE=mandriva
endif

foreach file (/etc/sysconfig/menustyle $HOME/.menustyle)
 if ( -f $file ) then
   eval `sed 's|^#.*||' $file | sed 's|\([^=]*\)=\([^=]*\)|set \1=\2|g' | sed 's|$|;|' `
 endif
end

if ($MDV_MENU_STYLE  == discovery && ! ${?XDG_CONFIG_DIRS}) then
	setenv XDG_CONFIG_DIRS /etc/xdg/discovery:/etc/xdg
endif

setenv MDV_MENU_STYLE $MDV_MENU_STYLE

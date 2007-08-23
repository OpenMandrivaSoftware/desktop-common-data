set MDV_MENU_STYLE=mandriva

foreach file (/etc/sysconfig/menustyle $HOME/.menustyle)
 if ( -f $file ) then
   eval `sed 's|^#.*||' $file | sed 's|\([^=]*\)=\([^=]*\)|set \1=\2|g' | sed 's|$|;|' `
 endif
end

if ($MDV_MENU_STYLE  == discovery && ! ${?XDG_CONFIG_DIRS}) then
	set MDV_MENU_STYLE=mandriva
endif

setenv MDV_MENU_STYLE $MDV_MENU_STYLE

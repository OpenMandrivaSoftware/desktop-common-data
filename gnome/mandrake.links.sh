#!/bin/bash

if [ ! -d ~/.gnome-desktop ] ; then
	mkdir -p ~/.gnome-desktop
fi

if [ -e "/usr/share/gnome/distribution-menus/Mandrake/Networking/WWW/Netscape Communicator.desktop" ] ; then
	cp -f "/usr/share/gnome/distribution-menus/Mandrake/Networking/WWW/Netscape Communicator.desktop" $HOME/.gnome-desktop/
elif [ -e "/usr/share/gnome/distribution-menus/Mandrake/Networking/WWW/Netscape Navigator.desktop" ] ; then
	cp -f "/usr/share/gnome/distribution-menus/Mandrake/Networking/WWW/Netscape Navigator.desktop" $HOME/.gnome-desktop/
fi
if [ -e /usr/share/gnome/distribution-menus/Mandrake/Configuration/Other/DrakConf.desktop ] ; then
	cp -f /usr/share/gnome/distribution-menus/Mandrake/Configuration/Other/DrakConf.desktop $HOME/.gnome-desktop/ -f
fi

# Documentation
langg=$(cat /etc/sysconfig/i18n | grep ^LANG= | sed -e 's/LANG=//')
if [ ! -e ~/.gnome/.doc ] ; then
	if [ ! -d ~/.gnome/ ] ; then
		mkdir -p ~/.gnome
	fi
	if [ $langg = de ] && [ -r /usr/share/doc/mandrake/de/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation-de.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
	elif [ $langg = es ] && [ -r /usr/share/doc/mandrake/es/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation-es.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
	elif [ $langg = fr_FR:fr ] || [ $langg = fr ] && [ -r /usr/share/doc/mandrake/fr/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation-fr.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
	elif [ $langg = it ] && [ -r /usr/share/doc/mandrake/it/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation-it.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
elif [ $langg = en ] || [ -z $langg ] && [ -r /usr/share/doc/mandrake/en/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
	elif [ -r /usr/share/doc/mandrake/en/index.html ] ; then
		cp /usr/share/mdk/gnome-desktop/Documentation.desktop ~/.gnome-desktop/Documentation.desktop && touch ~/.gnome/.doc
	fi
fi

# Mandrake Campus
if [ ! -e ~/.gnome/.mdkcampus ] ; then
        cp /usr/share/mdk/gnome-desktop/Mandrake\ Campus.desktop ~/.gnome-desktop && touch ~/.gnome/.mdkcampus
fi


# Mandrake Expert
if [ ! -e ~/.gnome/.mdkexpert ] ; then
        cp /usr/share/mdk/gnome-desktop/Mandrake\ Expert.desktop ~/.gnome-desktop/ && touch ~/.gnome/.mdkexpert
fi

# Control Center
if [ ! -e ~/.gnome/.ccenter ] && [ -x /usr/X11R6/bin/DrakConf ] ; then
        cp /usr/share/mdk/gnome-desktop/Mandrake\ Control\ Center.desktop ~/.gnome-desktop/Mandrake\ Control\ Center.desktop && touch ~/.gnome/.ccenter
fi

        
# Mandrake Update
if [ ! -e ~/.gnome/.mdkupdate ] && [ -x /usr/bin/rpmdrake ] ; then
        cp /usr/share/mdk/gnome-desktop/Software\ Manager.desktop ~/.gnome-desktop/ && touch ~/.gnome/.mdkupdate
fi


# Internet
if [ ! -e ~/.gnome/.internet ] ; then
        if [ -x /usr/sbin/draknet ] ; then
                cp /usr/share/mdk/gnome-desktop/Connection-to-Internet.desktop ~/.gnome-desktop/Internet.desktop && touch ~/.gnome/.internet ;
        fi
fi

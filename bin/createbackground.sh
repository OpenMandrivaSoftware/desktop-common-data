#!/bin/sh

# (c) 2000 - MandrakeSoft - Frederic CROZAT <fcrozat@mandrakesoft.com>

if [ $# != 2 ] ; then
   echo "Usage : $0 <location for backgrounds> < extension for background> ]"
   exit 1
fi

if [ -z $DISPLAY ] ; then
   echo "Must be run in an X session"
   exit 1
fi

backgroundhome=$1
extension=$2

if [ ! -d $backgroundhome ] ; then
    mkdir -p $backgroundhome 
fi

# Set backgrounds
width=$(/usr/X11R6/bin/xdpyinfo | grep dimensions | cut -c 18-26 | sed "s/x.*//")
vertype=$(cat /etc/sysconfig/system | grep META_CLASS | sed "s/META_CLASS=//" | tr A-Z a-z)


if [ -z "$vertype" ] || [ $vertype = "powerpack" ] ; then
    backgroundtype=PP
elif [ $vertype = "desktop" ] ; then
    backgroundtype=DKP 
else backgroundtype=PP
fi

if [ $width ] ; then
    for num in 1 2 3 4 5 6 7 ; do 
        file=/usr/share/pixmaps/backgrounds/linux-mandrake/$backgroundtype$num-$width.$extension
	if [ -s $file ] ; then
	    ln -sf $file $backgroundhome/linux-mandrake-background$num.$extension ;
	else 
	    echo "File $file does not exist or is not readable"
	fi
    done ;
fi

#!/bin/sh
if [ -x /usr/bin/qtcups ]; then
        qtcups $*
else 
        if [ -x /usr/bin/xpp ]; then
                xpp $*
        else 
                lpr $*
        fi
fi

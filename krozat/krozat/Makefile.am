# $Id$
# Makefile.am for kscreensave.
#

AM_CPPFLAGS = -UQT_NO_ASCII_CAST

INCLUDES = $(all_includes) 
LDFLAGS = $(all_libraries) $(KDE_RPATH)
LDADD = $(LIB_KDEUI) -lkscreensaver -lm

bin_PROGRAMS = krozat.kss 

krozat_kss_SOURCES = krozat.cpp

METASOURCES = krozat.moc

noinst_HEADERS = krozat.h

messages:
	$(XGETTEXT) *.cpp *.h -o $(podir)/klock.pot

########## Meta objects ##########

#data_DATA = kscience.png
datadir = $(kde_datadir)/kscreensaver

desktop_DATA = Krozat.desktop 

desktopdir = $(kde_appsdir)/System/ScreenSavers

#EXTRA_DIST = $(desktop_DATA) vm.xpm vm.xbm kscience.png

SUBDIRS = . pics

INCLUDES = $(GTK_CFLAGS) $(CAPPLET_CFLAGS) -DDATADIR=\"$(datadir)/eazel-engine\"

bin_PROGRAMS = eazel-engine-capplet

eazel_engine_capplet_SOURCES =	eazel-engine-capplet.c

eazel_engine_capplet_LDADD = $(GTK_LIBS) $(CAPPLET_LIBS)

EXTRA_DIST = eazel-engine-properties.desktop

sysdir = $(datadir)/control-center/Desktop
sys_DATA = eazel-engine-properties.desktop

menudir = $(datadir)/gnome/apps/Settings/Desktop/
menu_DATA = $(sys_DATA)

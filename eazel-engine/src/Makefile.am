
INCLUDES = $(GTK_CFLAGS) $(GDK_PIXBUF_CFLAGS) -DDATADIR=\"$(datadir)/eazel-engine\"

enginedir = $(libdir)/gtk/themes/engines

engine_LTLIBRARIES = libeazel-engine.la

libeazel_engine_la_SOURCES =	\
	eazel-theme.h		\
	eazel-theme-draw.c	\
	eazel-theme-main.c	\
	eazel-theme-gradient.c	\
	eazel-theme-pixmaps.c	\
	eazel-theme-hacks.c

libeazel_engine_la_LDFLAGS = -module -avoid-version
libeazel_engine_la_LIBADD = $(GTK_LIBS) $(GDK_PIXBUF_LIBS)

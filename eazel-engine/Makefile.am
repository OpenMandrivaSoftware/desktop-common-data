SUBDIRS = src capplet data Crux

INCLUDES = $(GTK_CFLAGS) $(GNOME_CFLAGS) -DDATADIR=\"$(datadir)\"

EXTRA_DIST =			\
	gtkrc.in		\
	make-gtkrc.pl		\
	test.glade		\
	eazel-engine.spec.in	\
	check-data.sh

dist-hook: spec-hook check-data
	
spec-hook : eazel-engine.spec
	cp $^ $(distdir)

check-data : check-data.sh
	$(SHELL) $<

noinst_PROGRAMS = test

test_LDADD = $(GTK_LIBS) $(GNOME_LIBS)

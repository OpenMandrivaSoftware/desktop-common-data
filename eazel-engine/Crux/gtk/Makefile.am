
COLOR = '<".eazel-engine-color">'

themedir = $(datadir)/themes/Crux/gtk
theme_DATA = gtkrc

enginedir = $(libdir)/gtk/themes/engines

MAINTAINERCLEANFILES = gtkrc

gtkrc : $(top_srcdir)/gtkrc.in $(top_srcdir)/make-gtkrc.pl $(top_builddir)/config.status
	perl $(top_srcdir)/make-gtkrc.pl -c $(COLOR) -d "$(enginedir)" < $(top_srcdir)/gtkrc.in > gtkrc

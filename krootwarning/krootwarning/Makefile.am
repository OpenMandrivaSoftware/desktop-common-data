
bin_PROGRAMS = krootwarning
krootwarning_SOURCES = krootwarning.cpp main.cpp
krootwarning_METASOURCES = AUTO
krootwarning_LDADD   =  $(LIB_QT) $(LIB_KDECORE) $(LIB_KDEUI)  $(LIBSOCKET)


EXTRA_DIST = main.cpp krootwarning.cpp krootwarning.h krootwarning.desktop lo32-app-krootwarning.png lo16-app-krootwarning.png 

install-data-local:
	$(mkinstalldirs) $(kde_appsdir)/Applications/
	$(INSTALL_DATA) $(srcdir)/krootwarning.desktop $(kde_appsdir)/Applications/krootwarning.desktop
	$(mkinstalldirs) $(kde_icondir)/locolor/32x32/apps/
	$(INSTALL_DATA) $(srcdir)/lo32-app-krootwarning.png $(kde_icondir)/locolor/32x32/apps/krootwarning.png
	$(mkinstalldirs) $(kde_icondir)/locolor/16x16/apps/
	$(INSTALL_DATA) $(srcdir)/lo16-app-krootwarning.png $(kde_icondir)/locolor/16x16/apps/krootwarning.png

uninstall-local:
	-rm -f $(kde_appsdir)/Applications/krootwarning.desktop
	-rm -f $(kde_icondir)/locolor/32x32/apps/krootwarning.png
	-rm -f $(kde_icondir)/locolor/16x16/apps/krootwarning.png


# set the include path for X, qt and KDE
INCLUDES= $(all_includes)

SUBDIRS = . pics

METASOURCES = AUTO

# the library search path. 
krootwarning_LDFLAGS = $(all_libraries) $(KDE_RPATH)

messages: 
	LIST=`find . -name \*.h -o -name \*.hh -o -name \*.H -o -name \*.hxx -o -name \*.hpp -o -name \*.cpp -o -name \*.cc -o -name \*.cxx -o -name \*.ecpp -o -name \*.C`; \
	if test -n "$$LIST"; then \
	 $(XGETTEXT) $$LIST -o $(podir)/krootwarning.pot; \
	fi


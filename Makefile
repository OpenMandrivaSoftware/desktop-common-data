NAME = mandrake_desk
VERSION = $(shell awk '/define version/ { print $$3 }' $(NAME).spec)
mandir=/usr/share/man

all:
	@echo "Run make install"

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

merge-translations:
	for i in `find kde kdelnk gnome old special -name "*.in"` ; \
	do \
		case "$$i" in \
		*.links.desktop.in) \
			xml-i18n-merge -d po $$i \
			    `dirname $$i`/`basename $$i .desktop.in` ;; \
		*.noext.kdelnk.in) \
			xml-i18n-merge -d po $$i \
			    `dirname $$i`/`basename $$i .noext.kdelnk.in` ;; \
		*.in) \
			xml-i18n-merge -d po $$i \
			    `dirname $$i`/`basename $$i .in` ;; \
	  esac ; \
	done

install: merge-translations
	mkdir -p $(RPM_BUILD_ROOT)/usr/{s,}bin
	mkdir -p $(RPM_BUILD_ROOT)/$(mandir)/man8/
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/{faces,icons,icons/large,icons/mini,pixmaps/backgrounds/mandrake}
	mkdir -p $(RPM_BUILD_ROOT)/etc/X11/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk
	mkdir -p $(RPM_BUILD_ROOT)/etc/skel/Desktop
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/desktop-links
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/Internet
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/System
	install -m644 man/*8 $(RPM_BUILD_ROOT)/$(mandir)/man8/
	install -m755 sbin/* $(RPM_BUILD_ROOT)/usr/sbin/
	install -m755 bin/* $(RPM_BUILD_ROOT)/usr/bin/
	install -m644 icons/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/*.png $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/mini/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/mini
	install -m644 icons/large/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/large
	install -m644 backgrounds/* \
	$(RPM_BUILD_ROOT)/usr/share/pixmaps/backgrounds/mandrake/
	install -m644 default_background.jpg \
	$(RPM_BUILD_ROOT)/usr/share/pixmaps/backgrounds/
	install -m644 default_logo.jpg \
	$(RPM_BUILD_ROOT)/usr/share/icons/

	install -m644 kdelnk/*.kdelnk $(RPM_BUILD_ROOT)/etc/skel/Desktop/
	install -m644 icons/mandrake*.xpm $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk/
	install -m755 gnome/mandrake.links.sh \
		$(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	install -m644 gnome/mandrake.links \
		$(RPM_BUILD_ROOT)/usr/lib/desktop-links
	install -m644 faces/* $(RPM_BUILD_ROOT)/usr/share/faces


dis: 
	rm -rf $(NAME)-$(VERSION) ../$(NAME)-$(VERSION).tar*
	cvs commit
	mkdir -p $(NAME)-$(VERSION)
	find . -not -name "$(NAME)-$(VERSION)"|cpio -pd $(NAME)-$(VERSION)/
	find $(NAME)-$(VERSION) -type d -name CVS -o -name .cvsignore -o -name unused |xargs rm -rf
	tar cf ../$(NAME)-$(VERSION).tar $(NAME)-$(VERSION)
	bzip2 -9f ../$(NAME)-$(VERSION).tar
	rm -rf $(NAME)-$(VERSION)

rpm: dis ../$(NAME)-$(VERSION).tar.bz2 $(RPM)
	cp -f ../$(NAME)-$(VERSION).tar.bz2 $(RPM)/SOURCES
	cp -f special/mandrake-small.xpm $(RPM)/SOURCES/
	cp -f $(NAME).spec $(RPM)/SPECS/
	-rpm -ba --clean --rmsource $(NAME).spec
	rm -f ../$(NAME)-$(VERSION).tar.bz2
	rm -f $(RPM)/SOURCES/mandrake-small.xpm
	rm -f $(RPM)/SPECS/$(NAME).spec

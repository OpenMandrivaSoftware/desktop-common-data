NAME = mandrake_desk
VERSION = 1.0.1

all:
	@echo "Run make install"

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

dis: clean
	rm -rf $(NAME)-$(VERSION) ../$(NAME)-$(VERSION).tar*
	mkdir -p $(NAME)-$(VERSION)
	find . -not -name "$(NAME)-$(VERSION)"|cpio -pd $(NAME)-$(VERSION)/
	find $(NAME)-$(VERSION) -type d -name CVS -o -name .cvsignore -o -name unused |xargs rm -rf
	perl -p -i -e 's|^%define version.*|%define version $(VERSION)|' $(NAME).spec
	tar cf ../$(NAME)-$(VERSION).tar $(NAME)-$(VERSION)
	bzip2 -9f ../$(NAME)-$(VERSION).tar
	rm -rf $(NAME)-$(VERSION)

rpm: dis ../mandrake_desk-$(VERSION).tar.bz2 $(RPM)
	cp -f ../mandrake_desk-$(VERSION).tar.bz2 $(RPM)/SOURCES
	cp -f mandrake_desk.spec $(RPM)/SPECS/
	cp -f special/mandrake-small.xpm $(RPM)/SOURCES/
	-rpm -ba mandrake_desk.spec
	rm -f ../mandrake_desk-$(VERSION).tar.bz2

install:
	mkdir -p $(RPM_BUILD_ROOT)/usr/sbin
	mkdir -p $(RPM_BUILD_ROOT)/usr/man/man8/
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/{icons,icons/large,icons/mini,pixmaps/backgrounds/mandrake}
	mkdir -p $(RPM_BUILD_ROOT)/etc/X11/
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk
	mkdir -p $(RPM_BUILD_ROOT)/etc/skel/Desktop
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	mkdir -p $(RPM_BUILD_ROOT)/usr/lib/desktop-links
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/Internet
	mkdir -p $(RPM_BUILD_ROOT)/usr/share/gnome/apps/System
	install -m644 man/*8 $(RPM_BUILD_ROOT)/usr/man/man8/
	install -m755 sbin/* $(RPM_BUILD_ROOT)/usr/sbin
	install -m644 window-managers $(RPM_BUILD_ROOT)/etc/X11/
	install -m644 icons/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/*.png $(RPM_BUILD_ROOT)/usr/share/icons/
	install -m644 icons/mini/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/mini
	install -m644 icons/large/*.xpm $(RPM_BUILD_ROOT)/usr/share/icons/large
	install -m644 backgrounds/* \
	$(RPM_BUILD_ROOT)/usr/share/pixmaps/backgrounds/mandrake/
	install -m644 kdelnk/* $(RPM_BUILD_ROOT)/etc/skel/Desktop/
	install -m644 icons/mandrake*.xpm $(RPM_BUILD_ROOT)/usr/share/pixmaps/mdk/
	install -m644 gnome/Netscape.desktop \
		$(RPM_BUILD_ROOT)/usr/share/gnome/apps/Internet
	install -m644 gnome/{DrakConf,RpmDrake}.desktop \
		$(RPM_BUILD_ROOT)/usr/share/gnome/apps/System
	install -m755 gnome/mandrake.links.sh \
		$(RPM_BUILD_ROOT)/usr/lib/mc/desktop-scripts
	install -m644 gnome/mandrake.links \
		$(RPM_BUILD_ROOT)/usr/lib/desktop-links
	bzip2 -9f $(RPM_BUILD_ROOT)/usr/man/*/*


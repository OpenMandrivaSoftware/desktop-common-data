PACKAGE = mandrake_desk
NAME = mandrake_desk
VERSION:=$(shell grep 'Version:' $(PACKAGE).spec| cut -f 2)
RELEASE:=$(shell grep 'Release:' $(PACKAGE).spec| cut -f 2)
RPM=$(HOME)/rpm
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

dis: clean
	rm -rf $(NAME)-$(VERSION) ../$(NAME)-$(VERSION).tar*
	mkdir -p $(NAME)-$(VERSION)
	find . -not -name "$(NAME)-$(VERSION)"|cpio -pd $(NAME)-$(VERSION)/
	find $(NAME)-$(VERSION) -type d -name CVS -o -name .cvsignore |xargs rm -rf
	tar cf ../$(NAME)-$(VERSION).tar $(NAME)-$(VERSION)
	bzip2 -9f ../$(NAME)-$(VERSION).tar
	rm -rf $(NAME)-$(VERSION)

rpm: dis ../$(NAME)-$(VERSION).tar.bz2 $(RPM)
	cp -f ../$(NAME)-$(VERSION).tar.bz2 $(RPM)/SOURCES
	cp -f $(NAME).spec $(RPM)/SPECS/
	rpm -ba --clean --rmsource $(NAME).spec
	rm -f ../$(NAME)-$(VERSION).tar.bz2

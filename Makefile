PACKAGE = mandrake_desk
NAME = mandrake_desk
VERSION:=$(shell grep 'Version:' $(PACKAGE).spec| cut -f 2)
RELEASE:=$(shell grep 'Release:' $(PACKAGE).spec| cut -f 2)
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

dis: clean
	rm -rf $(NAME)-$(VERSION) ../$(NAME)-$(VERSION).tar*
	mkdir -p $(NAME)-$(VERSION)
	find . -not -name "$(NAME)-$(VERSION)"|cpio -pd $(NAME)-$(VERSION)/
	find $(NAME)-$(VERSION) -type d -name CVS -o -name .cvsignore |xargs rm -rf
	tar jcf ../$(NAME)-$(VERSION).tar.bz2 $(NAME)-$(VERSION)
	rm -rf $(NAME)-$(VERSION)

rpm: dis
	rpm -ta --clean --rmsource ../$(NAME)-$(VERSION).tar.bz2
	rm -f ../$(NAME)-$(VERSION).tar.bz2

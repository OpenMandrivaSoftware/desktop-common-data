PACKAGE = desktop-common-data
NAME = desktop-common-data
VERSION:=$(shell rpm -q --qf '%{VERSION}\n' --specfile $(PACKAGE).spec | head -1)
RELEASE:=$(shell rpm -q --qf '%{RELEASE}\n' --specfile $(PACKAGE).spec | head -1| sed -e 's/%mkrel \(.*\)/\1mdk/g')
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man
SVNROOT = svn+ssh://svn.mandriva.com/svn/soft/$(PACKAGE)


clean:
	find . -type d -name '.xvpics' -o -name '*~' |xargs rm -rf

# rules to build a test rpm

localrpm: localdist buildrpm

localdist: cleandist dir localcopy tar

cleandist:
	rm -rf $(PACKAGE)-$(VERSION) $(PACKAGE)-$(VERSION).tar.bz2

dir:
	mkdir $(PACKAGE)-$(VERSION)

localcopy:
	find . -not -name "$(PACKAGE)-$(VERSION)"|cpio -pd $(PACKAGE)-$(VERSION)/
	find $(PACKAGE)-$(VERSION) -type d -name CVS -o -name .cvsignore -name '*~' |xargs rm -rf

tar:
	tar cvf $(PACKAGE)-$(VERSION).tar $(PACKAGE)-$(VERSION)
	bzip2 -9vf $(PACKAGE)-$(VERSION).tar
	rm -rf $(PACKAGE)-$(VERSION)

buildrpm:
	rpm -ta $(PACKAGE)-$(VERSION).tar.bz2

# rules to build a distributable rpm

rpm: changelog svntag dist buildrpm

dist: cleandist dir export tar

export:
	svn export $(SVNROOT)/tags/$(TAG) $(PACKAGE)-$(VERSION)

svntag:
	svn copy $(SVNROOT)/trunk $(SVNROOT)/tags/$(TAG) -m "$(TAG)"

changelog: ../common/username
#svn2cl is available in our contrib.
	svn2cl --authors ../common/username.xml --accum
	rm -f ChangeLog.bak
	svn commit -m "Generated by svn2cl the `date '+%c'`" ChangeLog

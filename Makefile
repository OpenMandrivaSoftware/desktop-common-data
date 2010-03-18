PACKAGE = desktop-common-data
NAME = desktop-common-data
TAG := $(shell echo "V$(VERSION)_$(RELEASE)" | tr -- '-.' '__')
mandir=/usr/share/man
SVNROOT = svn+ssh://svn.mandriva.com/svn/soft/$(PACKAGE)

menus: applications.menu kde-applications.menu

menu/validated-menu: menu/applications.menu.in
	xmllint --noout --dtdvalid menu/menu.dtd $?

applications.menu: menu/validated-menu
	@echo -n "generating $@ "
	@sed -e 's,@MAIN_DESKTOP@,GNOME,g' -e 's,@MAIN_TOOLKIT@,GTK,g' -e 's,@ALTERNATIVE_DESKTOP@,KDE,g' -e 's,@ALTERNATIVE_TOOLKIT@,Qt,g' < menu/applications.menu.in > $@
	@xmllint --noout --dtdvalid menu/menu.dtd $@
	@echo " OK"

kde-applications.menu: menu/validated-menu
	@echo -n "generating $@ "
	@sed -e 's,@MAIN_DESKTOP@,KDE,g' -e 's,@MAIN_TOOLKIT@,Qt,g' -e 's,@ALTERNATIVE_DESKTOP@,GNOME,g' -e 's,@ALTERNATIVE_TOOLKIT@,GTK,g' < menu/applications.menu.in > $@
	@xmllint --noout --dtdvalid menu/menu.dtd $@
	@echo " OK"

checktag:
	@if [ -e ".git" ]; then \
         if ! git diff --quiet  ; then \
	   echo not all changes are committed, aborting ; \
	   exit 1 ; \
	 fi ; \
	 if [ -e ".git/svn" ]; then \
	   if ! git diff --quiet HEAD..trunk ; then \
	   echo not all changes were pushed to SVN repository ; \
	   exit 1 ; \
	   fi ; \
	 fi ; \
	fi
	@if [ "x$(VERSION)" == "x" -o "x$(RELEASE)" = "x" ]; then \
 	  echo usage is "make VERSION=version_number RELEASE=release_number dist" ; \
	  exit 1 ; \
	fi

clean:
	find . -type d -name '.xvpics' -o -name '*~' |xargs rm -rf
	rm -f applications.menu kde-applications.menu

# rules to build a distributable rpm

dist: menus checktag clean changelog tag
	rm -rf ../$(NAME)-$(VERSION)*.tar* $(NAME)-$(VERSION)
	@if [ -e ".svn" ]; then \
		$(MAKE) dist-svn; \
	elif [ -e ".git" ]; then \
		$(MAKE) dist-git; \
	else \
		echo "Unknown SCM (not SVN nor GIT)";\
		exit 1; \
	fi;
	$(info $(NAME)-$(VERSION).tar.bz2 is ready)

dist-git: 
	@git archive --prefix=$(NAME)-$(VERSION)/ HEAD | bzip2 -9 -c >../$(NAME)-$(VERSION).tar.bz2;

dist-svn: 
	svn export -q -rBASE . $(NAME)-$(VERSION)
	tar cfj ../$(NAME)-$(VERSION).tar.bz2 $(NAME)-$(VERSION)
	rm -rf $(NAME)-$(VERSION)

tag: checktag
	@if [ -e ".svn" ]; then \
		svn copy $(SVNROOT)/trunk $(SVNROOT)/tags/$(TAG) -m "$(TAG)"; \
	elif [ -e ".git" -a -e ".git/svn" ]; then \
		git svn tag $(TAG); \
	fi;

.PHONY: ChangeLog log changelog

log: ChangeLog

changelog: ChangeLog

#svn2cl is available in our contrib.
ChangeLog: ../common/username.xml
	@if test -d "$$PWD/.git"; then \
	  ../common/gitlog-to-changelog | sed -e '/\tgit-svn-id:.*/d' > $@.tmp \
	  && mv -f $@.tmp $@ \
	  && if [ -e ".git/svn" ]; then \
	    git svn dcommit ; \
	    fi \
	  || (rm -f  $@.tmp; \
	 echo Failed to generate ChangeLog, your ChangeLog may be outdated >&2; \
	 (test -f $@ || echo git-log is required to generate this file >> $@)); \
	else \
	 svn2cl --accum --authors ../../soft/common/username.xml; \
	 rm -f *.bak;  \
	fi;

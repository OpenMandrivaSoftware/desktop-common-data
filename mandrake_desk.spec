%define	release	21mdk
%define name	mandrake_desk
%define version	1.0.3

Summary:	The Desktop configuration files for Linux Mandrake
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	GPL
Group:		System/Configuration/Other
Icon:		mandrake-small.xpm
BuildRoot:	%{_tmppath}/%{name}-buildroot
# get the source from our cvs repository (see
# http://www.linuxmandrake.com/en/cvs.php3)
Source:		mandrake_desk-%{version}.tar.bz2
BuildArchitectures: noarch

%description
This package contains useful icons background and .kdelnk files for
the Mandrake desktop.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%install
make install RPM_BUILD_ROOT=$RPM_BUILD_ROOT
rm -f special/mandrake-small.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TRANSLATORS special/* README.CVS
%config /etc/X11/window-managers
/usr/sbin/*
/usr/bin/*
/usr/share/icons/*.xpm
/usr/share/icons/*.jpg
/usr/share/icons/mini/*.xpm
/usr/share/icons/large/*.xpm
/usr/share/pixmaps/backgrounds/mandrake
/usr/share/pixmaps/backgrounds/default_background.jpg
%config /etc/skel/Desktop/
/usr/share/pixmaps/mdk
#/usr/share/gnome/apps/Internet/*.desktop
/usr/share/gnome/apps/System/*.desktop
/usr/lib/mc/desktop-scripts/mandrake.links.sh
/usr/lib/desktop-links/mandrake.links
/usr/man/*/*

%changelog
* Fri May 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.3-21mdk
- corrected chksession for gnome.

* Fri May 12 2000 dam's <damien@mandrakesoft.com> 1.0.3-20mdk
- added gnome desktop entries.

* Wed May 10 2000 dam's <damien@mandrakesoft.com> 1.0.3-19mdk
- corrected bugy script. 

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-18mdk
- added Netscape on desktop.

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-17mdk
- corrected Netscape and rpmdrake gnome icons

* Tue May  9 2000 dam's <damien@mandrakesoft.com> 1.0.3-16mdk
- removed Netscape and rpmdrake gnome icons

* Sat May  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-15mdk
- sbin/chksession: if icewm is not here by default launch twm.

* Fri May  5 2000 Pixel <pixel@mandrakesoft.com> 1.0.3-14mdk
- fix for kdeDesktopCleanup

* Thu May 04 2000 dam's <damien@mandrakesoft.com> 1.0.3-13mdk
- cleaned gnome desktop.

* Sun Apr 30 2000 dam's <damien@mandrakesoft.com> 1.0.3-12mdk
- re-added XKill in kdelnk. 

* Fri Apr 28 2000 dam's <damien@mandrakesoft.com> 1.0.3-11mdk
- corrected xfce entry in windowmanagers.

* Thu Apr 27 2000 dam's <damien@mandrakesoft.com> 1.0.3-10mdk
- Corrected wmaker path.
- Added Update.kdelnk.

* Fri Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-9mdk
- Adjust wmaker path
- Maker rpmlint happy

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-8mdk
- Update doc icons

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.3-7mdk
- Update doc icons

* Thu Apr 20 2000 François Pons <fpons@mandrakesoft.com> 1.0.3-6mdk
- updated WindowMaker priority again.

* Thu Apr 20 2000 François Pons <fpons@mandrakesoft.com> 1.0.3-5mdk
- moved WindowMaker to a lower priority.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 1.0.3-4mdk
- removed some kdelnk for desktop cleaning.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 1.0.3-3mdk
- removed kdelnk/KAppfinder.kdelnk

* Sun Apr 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-2mdk
- DrakWM: a new greatest hit.

* Tue Apr 11 2000 dam's <damien@mandrakesoft.com> 1.0.3-1mdk
- new icons, new place for default background.

* Wed Apr  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.2-1mdk
- mandrake_desk.spec: adjust groups.
- Makefile: correct dis and rpm target.
- window-managers: fix blakbox with last blackbox package.
- Makefile: don't need to bzip (spec-helper do this job).

* Wed Feb  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-19mdk
- window-managers: Add a sawmill entry (V.Danen).

* Thu Jan 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-18mdk
- backgrounds/mandrake_background_*: add background from helene.
- mandrake_desk.spec: Remove the mandrake_background.xpm

* Mon Jan 10 2000 Pixel <pixel@mandrakesoft.com>
- icons/mini/hd_umount.xpm: renamed in hd_unmount.xpm (for coherence)

* Fri Jan  7 2000 Pixel <pixel@mandrakesoft.com>
- window-managers (NAME): KDE => kde.
- sbin/chksession: look at /etc/sysconfig/desktop to sort

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- icons/*: convert back and from .gif for kfm compliance :-/

* Wed Jan  5 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-13mdk
- Fix gnome links.

* Tue Jan  4 2000 Pixel <pixel@mandrakesoft.com>
- sbin/kdeDesktopCleanup: perl's glob in not " " compliant :(

* Tue Jan 04 2000 David BAUDENS <baudens@mandrakesoft.com>
- Use BBDrake & WMDrake for BlackBox & Window Maker

* Fri Dec 31 1999 Pixel <pixel@mandrakesoft.com>
- Makefile (dis): added a missing \
- kdelnk: Name field changes (dadou)

* Tue Dec 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a manpages for chksession from camille.
- sbin/chksession: no errror when no Session is present.

* Mon Dec 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Various fix and changes (icons & links).
- bin/chkSession check if we are root.

* Fri Dec 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- window-managers: various change from (jerome).
- kdelnk/Kppp.kdlnk: (new).
- icons/user-*: added user icons for kdm (pixel).
- gnome/*: sync with kde desktop. (pablo).

* Tue Dec 23 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included the mandrake.links* files formerly in gmc package

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- sbin/fndSession: new script with the new chksession.
- sbin/chksession: a new greatest hit.
- window-managers: list of current window manager.

* Mon Dec 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Another icons change.

* Mon Dec 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons large and mini.

* Mon Dec 20 1999 Pixel <pixel@mandrakesoft.com>
- added icons/mini and icons/large

* Sun Dec 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add fndSession.
- Use mktemp instead of $$ for fndSession.
- Add a real Makefile and clean-up the .spec.

* Fri Dec 17 1999 Pixel <pixel@mandrakesoft.com>
- add perl script to remove icons pointing to binaries not present

* Thu Dec 16 1999 Pixel <pixel@mandrakesoft.com>
- new icons

* Thu Dec 16 1999 François PONS <fpons@mandrakesoft.com>
- removed Cd-Rom.kdelnk and floppy.kdelnk, since handled by DrakX.

* Mon Dec 13 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- reordered the mess with the *.kdelnk translations
- put old files in a old/ directory (the translations inside them
  can be handy if a similar icon is needed in the future)

* Fri Dec 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove my CVS DIR :\.

* Fri Dec 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove Hwiz.kdelnk
- Add/Remove icons.
- A lots of new icons (heléne).
- Add the doc.

* Mon Dec 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added ca, cs, gl language

* Mon Nov 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add Hwiz.kdelnk to Autostart kde.

* Thu Nov 04 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- changed the type of icons for CD and floppy

* Mon Oct 25 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added da, br, sk, uk translations

* Mon Oct 04 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added lt, ru translations
- added kdelnk/Dos_C.kdelnk icon (will be used as a pattern 
  by initscripts' kdeicons when creating icons for the FAT partitions)
- the horribly big *.xpm backgrounds are now created at %install time
  with 'convert'; that way we avoid the bzip2 taking forever each time
  a new version is done. 

* Fri Sep 28 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added de, is, it, ro translations

* Tue Sep 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Gaeilge (irish gaelic) translations

* Thu Sep 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included translations in several languages (et,hr,hu,id,nl,no)
  Currently covered are: es,et,fr,hr,hu,id,nl,no,wa you are welcome
  to add descriptions for the missing languages, get in touch with me.

* Wed Aug 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Launch kpackage with kdesu.
- Add script to launch this fu***ng linuxconf as kdesu (i love to do awfull
  thing :-(( ).

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix another typo :-((.

* Fri Aug 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move floppy.kdelnk to FLOPPY.kdelnk for backward compatibilities.

* Fri Aug 20 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included norwegian nad indonesian texts for icons

* Wed Aug 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild with defattr(root,root). (Thanks to Michael Irving <laric@laric.com>)

* Wed Aug 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Reinsert {FLOPPY,CDROM} and remove from kdesupport.

* Tue Aug 03 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove {FLOPPY,CDROM} (already in kdesupport).

* Mon Aug 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- desktop-links/* for gmc are installed through gmc package
- put an icon for the rpm

* Wed Jul 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added some stuff for Gnome

* Wed Jul 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Relifting of kde link.
- Add link for gnome.

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons.

* Mon Jul 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add mandrake backgrounds xpm.

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix background to backgrounds.
- Add mandrake background images.

* Sat May 22 1999 Gaël Duval <gael@linux-mandrake.com>
- fixed bad owner/group files
- added PRINTER.kdelnk

* Wed May 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix url of kde links.

* Sat May 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add new icons.

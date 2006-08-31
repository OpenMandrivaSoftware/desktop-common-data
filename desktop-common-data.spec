# EDIT IN CVS NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

Summary:	Desktop common files 
Name:		desktop-common-data
Version:	2007
Release: 	%mkrel 10
License:	GPL
URL:		http://www.mandrivalinux.com/
Group:		System/Configuration/Other

# get the source from our cvs repository (http://cvs.mandriva.com/cgi-bin/viewvc.cgi/soft/mandrake_desk)
# (see http://qa.mandriva.com/twiki/bin/view/Main/CvsHowto)
# no extra source or patch are allowed here.
Source:		%{name}-%{version}.tar.bz2

BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	intltool
BuildRequires:  mdk-menu-messages
BuildRequires:  gettext
BuildArch:	noarch
Requires:	mandriva-theme
Obsoletes:	mandrake_desk
Provides:	mandrake_desk
Conflicts:	kdebase-kdm-config-file < 1:3.2-62mdk
Obsoletes:	menu
Obsoletes:	menu-xdg
Provides:	menu-xdg
Provides:	menu = 2.1.24
Requires:	xinitrc >= 2.4.12
Requires:	mdk-menu-messages >= 10.2-7mdk
Conflicts:      kdelibs-common < 30000000:3.5

%description
This package contains useful icons, menu structure and others goodies for the
Mandriva Linux desktop.

%prep



%setup -q
find . -type 'd' -name 'CVS' | xargs rm -fr



%install
rm -rf %buildroot

## Install backgrounds
# User & root's backgrounds
install -d -m 0755 %buildroot/%_datadir/mdk/backgrounds/
install -m 0644 backgrounds/flower.jpg %buildroot/%_datadir/mdk/backgrounds/
install -m 0644 backgrounds/nature.jpg %buildroot/%_datadir/mdk/backgrounds/

# XFdrake test card
install -d -m 0755 %buildroot/%_datadir/mdk/xfdrake/
install -m 0644 backgrounds/xfdrake-test-card.png %buildroot/%_datadir/mdk/xfdrake/xfdrake-test-card.png



## Install scripts
# /usr/bin/
install -d -m 0755 %buildroot/%_bindir/
for i in bin/*.sh ; do install -m 0755 $i %buildroot/%_bindir/ ; done
install -m 0755 bin/www-browser %buildroot/%_bindir/
install -m 0755 bin/xvt %buildroot/%_bindir/

# /usr/sbin/
install -d -m 0755 %buildroot/%_sbindir/
for i in sbin/* ; do install -m 0755 $i %buildroot/%_sbindir/ ; done

# /etc/X11/xinit.d/
install -d -m 0755 %buildroot/%_sysconfdir/X11/xinit.d/
for i in xinit.d/* ; do install -m 0755 $i %buildroot/%_sysconfdir/X11/xinit.d/ ; done


## Install faces
install -d -m 0755 %buildroot/%_datadir/mdk/faces/
install -d -m 0755 %buildroot/%_datadir/faces/
for i in faces/*.png ; do install -m 0644 $i %buildroot/%_datadir/mdk/faces/ ; done
		
# David - 9.0-5mdk - For KDE
install -m 0644 faces/default.png %buildroot/%_datadir/faces/default.png

# David - 9.0-5mdk - For GDM
install -m 0644 faces/default.png %buildroot/%_datadir/faces/user-default-mdk.png



## KDE
# kdm
install -d -m 0755 %buildroot/%_datadir/apps/kdm/pics/
install -m 0644 kde/kdm-mdk-logo.png %buildroot/%_datadir/apps/kdm/pics/



## icons
install -d -m 0755 %buildroot/%_miconsdir %buildroot/%_liconsdir
install -m 0644 menu/icons/*.png %buildroot/%_iconsdir
install -m 0644 menu/icons/large/*.png %buildroot/%_liconsdir
install -m 0644 menu/icons/mini/*.png %buildroot/%_miconsdir

# XDG menus
install -d -m 0755 %buildroot/%_sysconfdir/xdg/menus/applications-merged  %buildroot/%_sysconfdir/xdg/discovery/menus/applications-merged
install -d -m 0755 %buildroot/%_sysconfdir/menu.d %buildroot/%_sysconfdir/profile.d
install -m 0644 menu/applications-mdk.menu %buildroot/%_sysconfdir/xdg/menus/applications.menu
install -m 0644 menu/applications-discovery.menu %buildroot/%_sysconfdir/xdg/discovery/menus/applications.menu
install -m 0755 menu/xdg_menu %buildroot/%_bindir
install -m 0755 menu/update-menus %buildroot/%_bindir/update-menus
install -m 0755 menu/menustyle.sh menu/menustyle.csh %buildroot/%_sysconfdir/profile.d

install -d -m 0755 %buildroot/%_datadir/desktop-directories
mkdir tmp-l10n
for i in %_datadir/locale/*/LC_MESSAGES/menu-messages.mo ; do
 msgunfmt $i > tmp-l10n/`echo $i | sed -e 's|%{_datadir}/locale/||' -e 's|/LC.*||'`.po
done
 
for i in menu/desktop-directories/*.in ; do
 %{_bindir}/intltool-merge --desktop-style -c tmp-l10n/cache tmp-l10n $i %buildroot/%_datadir/desktop-directories/`basename $i .in` 
done


#install theme for GDM/KDM
install -d -m 0755 %buildroot/%_datadir/mdk/dm
for i in dm/*.png dm/*.desktop dm/*.xml ; do 
  install -m 0644 $i %buildroot/%_datadir/mdk/dm/
done


%post
if [ -f %_sysconfdir/X11/window-managers.rpmsave ];then
	%_sbindir/convertsession -f %_sysconfdir/X11/window-managers.rpmsave || :
fi
# Create a link to allow users to access to Mandrakelinux's backgrounds from KDE
[ ! -d %_datadir/wallpapers ] && install -d -m 0755 %_datadir/wallpapers
[ ! -e %_datadir/wallpapers/mandrake-linux ] && ln -s %_datadir/mdk/backgrounds/ %_datadir/wallpapers/mandrake-linux
%update_menus

%make_session

%postun
# Remove link created to allow users to access to Mandrakelinux's backgrounds from KDE
[ -e %_datadir/wallpapers ] && rm -f %_datadir/wallpapers/mandrake-linux
[ $(ls %_datadir/wallpapers/ | wc -l) -eq 0 ] && rm -fr %_datadir/wallpapers/
%clean_menus

%clean
rm -fr %buildroot



%files
%defattr(-,root,root,-)
%_bindir/*
#
%_sbindir/*

%_sysconfdir/X11/xinit.d/*
%_sysconfdir/profile.d/*
%dir %_sysconfdir/menu.d
%dir %_sysconfdir/xdg
%dir %_sysconfdir/xdg/menus
%dir %_sysconfdir/xdg/menus/applications-merged
%dir %_sysconfdir/xdg/discovery/menus
%dir %_sysconfdir/xdg/discovery/menus/applications-merged
%config(noreplace) %_sysconfdir/xdg/menus/*.menu
%config(noreplace) %_sysconfdir/xdg/discovery/menus/*.menu

#
%dir %_datadir/faces/
%dir %_datadir/mdk/
%dir %_datadir/mdk/faces/
%_datadir/faces/*
%_datadir/mdk/faces/*
#
%dir %_datadir/mdk/backgrounds/
%_datadir/mdk/backgrounds/*.jpg
#
%dir %_datadir/apps/kdm/pics/
%_datadir/apps/kdm/pics/*
#
%dir %_datadir/mdk/xfdrake/
%_datadir/mdk/xfdrake/*.png
#

%_datadir/mdk/dm
#
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png

%_datadir/desktop-directories/*.directory


%changelog
* Thu Aug 31 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-10mdv2007.0
- Fix upgrade from 2006
- Fix discovery menu (merge kmenuedit.menu when it created by kmenuedit, fix 
 kfmclient error)

* Wed Aug 30 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-9mdv2007.0
- update-menus doesn't do anything if DURING_INSTALL is set to 1

* Wed Aug 30 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-8mdv2007.0
- Add missing directory file for adventure (Mdv bug #24829)
- Add empty menu nodes for KDE in discovery menu
- Remove old X-MandrakeLinux* categories for main menu, all entries
  must now use X-MandrivaLinux
- fix default directories creation if translation contains spaces (Mdv bug #24677)

* Thu Aug 17 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-7mdv2007.0
- Add discovery menu and script to support MDV_MENU_STYLE

* Thu Aug 17 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-6
- Change requires to mandriva-theme

* Wed Aug 09 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-5
- Fix oowriter menu entry

* Mon Aug 07 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-4
- Fix applications-mdk.menu to merge kmenuedit.menu files (fix mdk bug #24103)

* Thu Jul 20 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-3mdv2007.0
- Ignore "Development" keyword, it is too broad atm (Mdv bug #23826)
- Add .directory for Archiving/Other (Mdv bug #23845)

* Thu Jul 20 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-2mdv2007.0
- Fix some typo (Andrej) (Mdk bug #23842)

* Mon Jul 17 2006 Frederic Crozat <fcrozat@mandriva.com> 2007-1mdv2007.0
- Drop old menu system completely

* Tue Jul 11 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-12mdv2007.0
- Add missing .directory (Mdv bug #23614)
- fix translations for some .directories (Mdv bug #23641)

* Fri Jul 07 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-11mdv2007.0
- add missing .directory
- rebuild with fixed intltool
- fix generating icewm menu from XDG (pixel)

* Mon Jun 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-10mdv2007.0
- Add missing .directory files and fix videoconference one

* Thu Jun 15 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-9mdv2007.0
- Switch to X-MandrivaLinux

* Mon May 29 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-8mdv2007.0
- Add legacy directories and default merge directory

* Wed May 17 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-7mdk
- ship our own .directory files now
- use kde .directory files when possible
- add more upstream categories

* Fri May 12 2006 Laurent MONTEL <lmontel@mandriva.com> 2006-6
- Update for missing kcontrol entry

* Thu May 11 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-5mdk
- Update menu file with new filename for kde

* Wed May 10 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-4mdk
- Add missing catergories in menu file (laurent)

* Thu May 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-3mdk
- Add applications-mdk.menu file for XDG menu system
- Add xdg_menu script from SUSE to support old WM
- Don't ship defaultlayout.menu anymore, it is merged into main menu
- Fix typo in old menu file

* Mon Sep 26 2005 Frederic Crozat <fcrozat@mandriva.com> 2006-2mdk 
- Fix desktop-directory script (UTF encoded URL, hidden .directory file)
  Mdk bug #18853

* Fri Sep 23 2005 Frederic Lepied <flepied@mandriva.com> 2006-1mdk
- Mandriva
- fixed simplified menu

* Mon Sep 19 2005 Laurent MONTEL <lmontel@mandriva.com> 10.3.1-9mdk
- Fix menu order

* Mon Sep 19 2005 Frederic Crozat <fcrozat@mandriva.com> 10.3.1-8mdk 
- Fix loop in www-browser (based on patch from Andrey Borzenkov)

* Mon Sep 12 2005 Frederic Crozat <fcrozat@mandriva.com> 10.3.1-7mdk 
- Fix package name and command for gimp in simplified menu (Mdk bug #17627)

* Thu Sep 08 2005 Laurent MONTEL <lmontel@mandriva.com> 10.3.1-6mdk
- Add separator in simplified menu

* Mon Aug 29 2005 Frederic Crozat <fcrozat@mandriva.com> 10.3.1-5mdk 
- Fix default directories script when no translation is available

* Fri Aug 26 2005 Frederic Crozat <fcrozat@mandriva.com> 10.3.1-4mdk 
- New scheme for default directories

* Wed Aug 24 2005 Frederic Crozat <fcrozat@mandriva.com> 10.3.1-3mdk 
- Add default directories xinit.d script

* Tue Aug 23 2005 Laurent MONTEL <lmontel@mandriva.com> 10.3.1-2mdk
- Mandrake->Mandriva

* Mon Jun  6 2005 Frederic Lepied <flepied@mandriva.com> 10.3.1-1mdk
- rebuild to have the correct fndSession (bug #16255)

* Mon May 30 2005 Frederic Lepied <flepied@mandriva.com> 10.3-1mdk
- fndSession: use the new generic framework

* Fri May 13 2005 Frederic Crozat <fcrozat@mandriva.com> 10.2-5mdk 
- change package name
- xvt : fix typo (bug #15836)
- fix typo in translation-map
- remove screensaver images, moved in theme package

* Tue Mar 29 2005 Frederic Lepied <flepied@mandrakesoft.com> 10.2-4mdk
- www-browser: test if the $BROWSER variable is set to something valid (bug #14903).

* Wed Mar 23 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 10.2-3mdk 
- don't use .desktop files for order directive

* Wed Mar 09 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 10.2-2mdk 
- change www-browser to use BROWSER variable if set or use running environment
  settings if set.
- xvt script to replace alternative : choose programs to start based on
  running environment

* Mon Mar 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 10.2-1mdk
- Fix error into menu

* Wed Mar 02 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-19mdk
- Fix order for simplified menu

* Tue Mar 01 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-18mdk
- Fix Filename order with menu id

* Tue Mar 01 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-17mdk
- Update menu order

* Mon Feb 28 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 10.1-16mdk 
- Install shared Mdk theme for GDM/KDM

* Tue Jan 25 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 10.1-15mdk 
- Fix small errors in default layout menu files

* Tue Dec 14 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 10.1-14mdk 
- Move mdk menu data from menu to mandrake_desk package

* Wed Sep 29 2004 David Baudens <baudens@mandrakesoft.com> 10.1-13mdk
- Fix task oriented menu to allow translations of "Listen to Music Files" menu
  entry (Laurent Montel)

* Wed Sep 29 2004 David Baudens <baudens@mandrakesoft.com> 10.1-12mdk
- Add missing menu entry for french Mandrakelinux documentation

* Wed Sep 29 2004 David Baudens <baudens@mandrakesoft.com> 10.1-11mdk
- Fix Import and Sort Your Photos menu entry

* Fri Sep 10 2004 David Baudens <baudens@mandrakesoft.com> 10.1-10mdk
- Add documentation to task oriented menu

* Thu Sep 09 2004 David Baudens <baudens@mandrakesoft.com> 10.1-9mdk
- Remove all longtitle

* Thu Sep 09 2004 David Baudens <baudens@mandrakesoft.com> 10.1-8mdk
- Fix task oriented menu (kphone)

* Wed Sep 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-7mdk
- Fix capitalization in simplified menu

* Tue Aug 31 2004 Frederic Lepied <flepied@mandrakesoft.com> 10.1-6mdk
- added the script www-browser

* Fri Aug 27 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 10.1-5mdk
- Fix typo in gnome-cd entry

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-4mdk
- Fix "Play Games" menu entry

* Wed Aug 11 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 10.1-3mdk
- Add GNOME version of task oriented menu
- Fix capitalisations in task oriented menu

* Thu Aug 05 2004 David Baudens <baudens@mandrakesoft.com> 10.1-2mdk
- Add "Make a phone call" to task oriented menu

* Thu Aug 05 2004 David Baudens <baudens@mandrakesoft.com> 10.1-1mdk
- Update task oriented menu

* Wed Aug  4 2004 Pixel <pixel@mandrakesoft.com> 10.0-11mdk
- add "chksession -L" used by DrakX to configure ~/.dmrc
- fix descriptions (use Mandrakelinux instead of simply Mandrake)

* Tue Mar  2 2004 Frederic Lepied <flepied@mandrakesoft.com> 10.0-10mdk
- in KDE session only pass the session name

* Fri Feb 27 2004 Frederic Lepied <flepied@mandrakesoft.com> 10.0-9mdk
- fixed KDM sessions

* Fri Feb 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-8mdk
- Fix typo reported by Per Øyvind Karlsen

* Tue Feb 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-7mdk
- Fix kontact icons

* Thu Feb 05 2004 David Baudens <baudens@mandrakesoft.com> 10.0-6mdk
- Fix simplified menu

* Thu Feb 05 2004 David Baudens <baudens@mandrakesoft.com> 10.0-5mdk
- Fix typos in simplified menu

* Thu Jan 29 2004 David Baudens <baudens@mandrakesoft.com> 10.0-4mdk
- Remove old files

* Mon Jan 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-3mdk
- Add "kontact" entry

* Tue Jan 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-2mdk
- Fix drakbackup menu entry

* Tue Jan 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-1mdk
- Fix requires with good menu
- Create simplified menu for MDK 10.0

* Wed Sep 10 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 9.2-8mdk
- xfdrake-test-card needs to be in .png format since we don't
  have have the jpeg pixbug loader during install

* Fri Sep 05 2003 David Baudens <baudens@mandrakesoft.com> 9.2-7mdk
- Update simplified menu

* Mon Sep 01 2003 David Baudens <baudens@mandrakesoft.com> 9.2-6mdk
- Remove "Record sound" in simplified menu

* Thu Aug 28 2003 David Baudens <baudens@mandrakesoft.com> 9.2-5mdk
- Update simplified menu

* Wed Aug 27 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 9.2-4mdk
- Fix fndSession to look for new gdm session path (fix bug #4572)

* Tue Aug 26 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 9.2-3mdk
- New background infrastructure (dadou)
- Rewritten chksession program and manpage, thanks to Bernard Lang
- Fixed chksession to generate a default session for gdm (fc)

* Fri Aug 22 2003 David Baudens <baudens@mandrakesoft.com> 9.2-2mdk
- Update

* Wed Jul 30 2003 David Baudens <baudens@mandrakesoft.com> 9.2-1mdk
- Fix %post (thanks to Pixel)

* Fri Jun 13 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 9.1-6mdk
- gdm session format has changed, fix chksession

* Wed Jun 04 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-5mdk
- Create a link to allow users to access to Mandrake's backgrounds from KDE

* Thu Mar 13 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-4mdk
- Add icons to applications which miss one
- Remove some broken applications
- Add OpenOffice.org entries

* Wed Mar 12 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-3mdk
- Update icons and screensavers images

* Fri Feb 14 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-1mdk
- Update default backgrounds

* Thu Feb 13 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-1mdk
- New backgrounds

* Fri Sep 06 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-20mdk
- Add mandrake-club icon

* Mon Sep 02 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-19mdk
- Fix drakconf menu entry

* Thu Aug 29 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-18mdk
- Enhance tux family images (Hélène)

* Thu Aug 29 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-17mdk
- Update screensavers

* Thu Aug 29 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-16mdk
- Tux family is back

* Tue Aug 27 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-15mdk
- Fix mail screensaver image

* Fri Aug 23 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-14mdk
- Fix mail screensaver image

* Fri Aug 23 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-13mdk
- New XFdrake image

* Thu Aug 22 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-12mdk
- New XFdrake image

* Thu Aug 22 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-11mdk
- New images for screensavers

* Fri Aug 02 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-10mdk
- Move faces in /usr/share/mdk/faces/

* Thu Aug 01 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-9mdk
- Add screensavers images

* Thu Aug 01 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-8mdk
- Re-add gnome.xpm & kde.xpm icons for Lord Pixel

* Wed Jul 31 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-7mdk
- Add kdm logo
- Re-add update-menus (and lost menu entries)

* Wed Jul 31 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-6mdk
- Add two new backgrounds
- Don't run update-menus

* Wed Jul 31 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-5mdk
- Remove eazel-mdk-engine, krozat, krootwarnig (moved in their own modules/packages)
- Add new icons
- Rewrite spec

* Wed Jul 31 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 9.0-4mdk
- Fix GNOME entry for Crux theme applet
- Fix menu entries for simplified menu

* Tue Jul 30 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-3mdk
- New default user image

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-2mdk
- Fix Requires
- Add Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> changes :
	- As usual, search for qt/kde libraries in the right directories

* Thu Jul 18 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-1mdk
- Remove old users images. Add new images. Feedback welcome using cooker@linux-mandrake.com.

* Fri Mar 15 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-13mdk
- Fix text color in progress bar in Mandrake GTK theme 

* Thu Mar  7 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-12mdk
- No longer create icon for root
- Modify Mandrake GTK theme - Frederic Crozat
- Change name of Mandrake Control Center to Control Center in GNOME desktop
  (Thanks to Mattias Dahlberg) - Frederic Crozat

* Tue Feb 26 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-11mdk
- Add/remove some icons
- Don't allow spec to skip a build or install step without stop
- Remove DrakWM

* Mon Feb 25 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-10mdk
- Fix mdk-eazel-engine text color (Thanks to Brice Figureau)
- Update po files

* Wed Feb 20 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-9mdk
- Oops, fix location of capplet for mdk-eazel-engine

* Wed Feb 20 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-8mdk
- Fix building of package
- Fix english title for "What to do?" menu (Thanks to Till and Phil Lavigna)

* Mon Feb 18 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-7mdk
- Various fixes for simplified menu

* Tue Feb 12 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-6mdk
- Clean simplified menu

* Tue Jan 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-5mdk
- Add link to Crux configuration applet
- Fix menu entries for simplified menu

* Mon Jan 28 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-4mdk
- New icons for GNOME desktop

* Sun Jan 27 2002 Stefan van der Eijk <stefan@eijk.nu> 8.2-3mdk
- BuildRequires

* Thu Jan 24 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-2mdk
- Fix path used for images in krozat

* Fri Jan 11 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 8.2-1mdk
- Move screensaver images to mandrake_desk package
- Configure default desktop for nautilus

* Mon Dec 24 2001 Stefan van der Eijk <stefan@eijk.nu> 8.1-22mdk
- BuildRequires

* Thu Oct 18 2001 Stefan van der Eijk <stefan@eijk.nu> 8.1-21mdk
- BuildRequires: arts

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-20mdk
- Fix GMC URL (Frederic Crozat)

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-19mdk
- Fix GMC script

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-18mdk
- Fix my mistake with default user icon for GDM

* Wed Sep 19 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-17mdk
- Add simplified menu file
- Gnome: don't put special icons on root desktop
- Gnome: fix Internet icon
- Gnome: fix URL (Fred CROZAT)
- mv man.png aman.png
- Remove some obsolete faces (LN)
- put mdk-eazel-engine capplet to separate package

* Sat Sep 16 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-16mdk
- Update gnome desktop

* Fri Sep 14 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-15mdk
- Update ga translations

* Tue Sep 13 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-14mdk
- Re-add mandrakeexpert and mandrakecampus icons

* Tue Sep 04 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-13mdk
- Remove old icons and nearly all old images
- Move eazel-engine-capplet in mdk-eazel-engine
- Use man.png as default image for users

* Tue Sep 04 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-12mdk
- Make Monseigneur Pascal Rigaux, Prince de DrakX, Marquis de Pixel, happy (aka,
  move eazel-engine in a separate package)

* Mon Sep 03 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 8.1-11mdk
- An other fix for krootwarning

* Sat Sep 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 8.1-10mdk
- Autostart krootwarning

* Thu Aug 30 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-9mdk
- Bazoocate /etc/gtkrc to the moon request

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-8mdk
- Build without rpath

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-7mdk
- Add menu entry for krozat

* Mon Aug 27 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-6mdk
- Fix %%defattr

* Sat Aug 25 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-5mdk
- Split package

* Fri Aug 24 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-4mdk
- Add krozat (our Chef ;)

* Tue Aug 08 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-3mdk
- Add krootwarning

* Tue Aug 07 2001 Vincent Saugey <vince@mandrakesoft.com> 8.1-2mdk
- Move faces png to /usr/share/mdk/faces

* Tue Jul 31 2001 Frederic Lepied <flepied@mandrakesoft.com> 8.1-1mdk
- reworked Makefile and spec
- resync with cvs
- generate the kdm sessions with the right path to Xsession.

* Tue Jun 12 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-12mdk
- Fix patch0 with authors comments

* Mon Jun 11 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-11mdk
- Add control-center-devel, db1-devel, gdk-pixbuf-devel and libglade-devel to
  BuildRequires (thanks to Stefan van der Eijk)

* Fri Jun  8 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-10mdk
- Patch0: fix eazel engine for gfloppy and xcdroast

* Fri Jun  8 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 8.0-9mdk
- Update eazel-engine to latest CVS snapshot (correct bug in Gimp)

* Wed Apr 18 2001 David BAUDENS <baudens@mandrakesot.com> 8.0-8mdk
- Fix some bugs in theme
- Update gnome-desktop

* Sat Apr 15 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-7mdk
- chksession: fix Window Managers list for GDM
- Update gnome-desktop

* Thu Apr 12 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-6mdk
- Remove KDE stuff
- Remove patch #1
- Add icons for Mandrake Campus and Mandrake Expert
- Add print-cups.sh script - Frederic CROZAT

* Wed Apr 4 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-5mdk
- fix zip mount point typo

* Thu Mar 29 2001 David BAUDENS <baudens@mandrakesoft.com> - 8.0-4mdk
- Add new GTK theme

* Tue Mar 20 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-3mdk
- remove Drakconf workaround patch

* Tue Mar 20 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-2mdk
- better workaround for DrakConf, waiting for Holy Traktopel to show me the way to fix. 

* Wed Mar 14 2001 Daouda Lo <daouda@mandrakesoft.com> 8.0-1mdk
- workaround to DrakConf crash (ugly) 
- update version number to 8.0 

* Mon Oct 09 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-18mdk
- Fix bugs 750, 732, 625, 623

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-17mdk
- Fix META_CLASS detection
- Redraw some icons (for FPons)

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-16mdk
- Fix faces for userdrake

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-15mdk
- Fix a typo

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-14mdk
- Fix icon for DrakConf

* Fri Oct 06 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-12mdk
- Fix bug # 639

* Thu Oct 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-11mdk
- Add icons for Pixel

* Wed Oct 04 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-10mdk
- Really create destdir when not present

* Wed Oct 04 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-9mdk
- More background & create destdir when not present (createbackground.sh)

* Tue Oct 02 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-8mdk
- Change default background names in createbackground.sh

* Mon Oct 02 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-7mdk
- Add createbackground.sh from Frederic CROZAT
- Remove old default background

* Fri Sep 22 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-6mdk
- New PATH for Linux-Mandrake backgrounds
- Put/remove backgrounds

* Wed Sep 20 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-5mdk
- Add new image for XFdrake
- Remove Templates and Autostart from /etc/skel/Desktop

* Tue Sep 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-4mdk
- Add KDM pixmap

* Fri Sep 01 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-3mdk
- Add some icons in faces (aka make Pixel happy)

* Fri Sep 01 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-2mdk
- Fix CD-ROM & Co links (KDE)

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 7.2-1mdk
- KDE 2 compliant

* Thu Aug 31 2000 David BAUDENS <baudens@mandrakesoft.com> 7.1-1mdk
- Add new Chmouel chksession
- Update description

* Thu Aug 24 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-9mdk
- Add a link "root" to make GDM happy
- Remove old links

* Wed Aug 23 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-8mdk
- Add links default.png and root.png to make KDM happy

* Wed Aug 23 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-7mdk
- Convert /usr/share/faces/*.xpm to /usr/share/faces/*.png to make KDM happy

* Tue Aug 22 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.4-6mdk
- Move user icons in /usr/share/faces

* Sat Jul 22 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-5mdk
- Oups forgot the BM.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-4mdk
- sbin/chksession: Set support for KDE2 by default when generating
  session.

* Tue Jul 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-3mdk
- Remove /etc/X11/window-managers
- bin/DrakWM: 
  	* Add -i options to launch with xinit.
	* Add -a option to provide alias for bash.
 
* Mon Jul 17 2000 dam's <damien@mandrakesoft.com> 1.0.4-2mdk
- replaced sawmill by sawfish

* Tue Jul 11 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-1mdk
- Add convertsession
- Make window-managers file dynamic and set them in /etc/X11/wmsession.d/.

* Mon May 29 2000 dam's <damien@mandrakesoft.com> 1.0.3-22mdk
- corrected doc url on gnome-desktop

* Fri May 12 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.3-21mdk
- corrected chksession for gnome.

* Fri May 12 2000 dam's <damien@mandrakesoft.com> 1.0.3-20mdk
- added gnome desktop entries.

* Wed May 10 2000 dam's <damien@mandrakesoft.com> 1.0.3-19mdk
- corrected buggy script. 

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
- the horribly big *.xpm backgrounds are now created at %%install time
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

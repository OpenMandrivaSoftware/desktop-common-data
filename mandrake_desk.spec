Summary:	The Desktop configuration files for Mandrake Linux
Name:		mandrake_desk
Version:	8.2
Release:	10mdk
License:	GPL
URL:		http://www.mandrakelinux.com/
Group:		System/Configuration/Other

# get the source from our cvs repository (see
# http://www.linuxmandrake.com/en/cvs.php3)
# no extra source or patch are allowed here.
Source:		mandrake_desk-%{version}.tar.bz2

BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:   menu
BuildRequires:	kdelibs-devel libcapplet-devel gdk-pixbuf-devel
BuildRequires:	XFree86-static-libs
BuildRequires:	arts
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	control-center-devel
BuildRequires:	freetype2
BuildRequires:	gcc-c++
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext
BuildRequires:	kdelibs-devel
BuildRequires:	texinfo

%description
This package contains useful icons, backgrounds and others goodies for the
Mandrake desktop.

%package -n mdk-eazel-engine
Summary:	Default GTK theme used in Mandrake Linux distribution
Group:		Graphical desktop/Other
Requires:	libgtk+1.2

%description -n mdk-eazel-engine
This package contains the default GTK theme used in Mandrake Linux 
distribution.

%package -n mdk-eazel-engine-capplet
Summary:	Configuration applet for Default GTK theme used in Mandrake Linux distribution
Group:		Graphical desktop/GNOME
Requires:	mdk-eazel-engine

%description -n mdk-eazel-engine-capplet
This package contains the configuration applet for Default GTK theme 
used in Mandrake Linux distribution


%package -n krootwarning
Summary:	Warning box for root user
Group:		Graphical desktop/KDE
Requires:	kdebase

%description -n krootwarning
This package contains a warning box displayed when you are using KDE with
system administrator permissions.

%package -n krozat
Summary:	Default Mandrake Linux screensaver for KDE
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs-devel
Requires:	kdebase
Requires:   mandrake_desk >= 8.2

%description -n krozat
This package contains the default Mandrake Linux screensaver for KDE.

%prep

%setup -q
find . -type 'd' -name 'CVS' | xargs rm -fr

%build
(
cd eazel-engine
%configure
%make
)

(
cd krootwarning
make -f admin/Makefile.common
./configure --prefix=%_prefix --enable-final --disable-debug --with-xinerama --disable-rpath
%make
)

(
cd krozat
make -f admin/Makefile.common
./configure --prefix=%_prefix --enable-final --disable-debug --with-xinerama --disable-rpath
%make
)

%install
rm -rf %buildroot

(
cd eazel-engine
%makeinstall_std
)
mkdir -p $RPM_BUILD_ROOT{%{_menudir},%{_datadir}/control-center/capplets/Advanced}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/mdk-eazel-engine-capplet
?package(mdk-eazel-engine-capplet):command="%{_bindir}/eazel-engine-capplet" \
needs="gnome" section="Configuration/Gnome/Advanced" title="Crux GTK+ Theme" \
longtitle="Configuration applet for Crux GTK+ theme"
EOF
cp -f $RPM_BUILD_ROOT%_datadir/gnome/apps/Settings/Desktop/eazel-engine-properties.desktop $RPM_BUILD_ROOT%{_datadir}/control-center/capplets/Advanced
(
cd krootwarning
%makeinstall_std
)

(
cd krozat
%makeinstall_std
)

mkdir -p %buildroot/%_datadir/themes/Mandrake/gtk
install -m644 gtkrc %buildroot/%_datadir/themes/Mandrake/gtk

make install RPM_BUILD_ROOT=%buildroot mandir=%{_mandir}

mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/X11/wmsession.d/

rm -f special/mandrake-small.xpm

install -d %buildroot/%_datadir/faces/
cp %buildroot/%_datadir/mdk/faces/user-hat-mdk.png %buildroot/%_datadir/faces/root.png
cp %buildroot/%_datadir/faces/root.png %buildroot/%_datadir/faces/root
cp %buildroot/%_datadir/mdk/faces/aman.png %buildroot/%_datadir/faces/default.png
cp %buildroot/%_datadir/mdk/faces/aman.png %buildroot/%_datadir/mdk/faces/default.png
# Dadou - 18mdk - This is needed for GDM
cp %buildroot/%_datadir/mdk/faces/aman.png %buildroot/%_datadir/mdk/faces/user-default-mdk.png

install -d %buildroot/%_datadir/mdk/gnome-desktop/
for l in de en fr it; do
	install -m644 gnome/gnome-Documentation-$l.desktop %buildroot/%_datadir/mdk/gnome-desktop/Documentation-$l.desktop
done

mkdir -p $RPM_BUILD_ROOT%_libdir/mc/desktop-scripts
cp gnome/mandrake.links.sh $RPM_BUILD_ROOT%_libdir/mc/desktop-scripts/mandrake.links.sh
chmod 0755 $RPM_BUILD_ROOT%_libdir/mc/desktop-scripts/mandrake.links.sh
install -m644 gnome/gnome-mandrake-control-center.desktop %buildroot/%_datadir/mdk/gnome-desktop
install -m644 gnome/gnome-mandrake-expert.desktop %buildroot/%_datadir/mdk/gnome-desktop
install -m644 gnome/gnome-mandrake-news.desktop %buildroot/%_datadir/mdk/gnome-desktop
install -m644 gnome/gnome-mandrake-store.desktop %buildroot/%_datadir/mdk/gnome-desktop
install -m644 gnome/gnome-Internet.desktop %buildroot/%_datadir/mdk/gnome-desktop

mkdir -p $RPM_BUILD_ROOT%_datadir/nautilus/default-desktop
install -m644 gnome/gnome-mandrake-control-center.desktop %buildroot/%_datadir/nautilus/default-desktop
install -m644 gnome/gnome-mandrake-expert.desktop %buildroot/%_datadir/nautilus/default-desktop
install -m644 gnome/gnome-mandrake-news.desktop %buildroot/%_datadir/nautilus/default-desktop
install -m644 gnome/gnome-mandrake-store.desktop %buildroot/%_datadir/nautilus/default-desktop
install -m644 gnome/gnome-Internet.desktop %buildroot/%_datadir/nautilus/default-desktop


install -d %buildroot/%_datadir/pixmaps
install -m644 gnome/*.png %buildroot/%_datadir/pixmaps

install -m755 gnome/gnomedesktop-network %buildroot/%_bindir

install -d %buildroot/%_menudir
kdedesktop2mdkmenu.pl krozat .hidden/ScreenSavers %buildroot/%_datadir/applnk/System/ScreenSavers/Krozat.desktop %buildroot/%_menudir/krozat kde

install -d %buildroot/%_menudir/simplified/
install -m644 menu/mandrake_desk %buildroot/%_menudir/simplified/



%post
if [ -f %_sysconfdir/X11/window-managers.rpmsave ];then
	%_prefix/sbin/convertsession -f %_sysconfdir/X11/window-managers.rpmsave || :
fi
%update_menus

%postun
%clean_menus

%post -n krozat
%update_menus

%postun -n krozat
%clean_menus

%post -n mdk-eazel-engine-capplet
%update_menus

%postun -n mdk-eazel-engine-capplet
%clean_menus



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc TRANSLATORS
#
#
%_bindir/DrakWM
%_bindir/createbackground.sh
%_bindir/gnomedesktop-network
%_bindir/print-cups.sh
#
#
%dir %_sysconfdir/X11/wmsession.d/
#
#
%dir %_libdir/mc/desktop-scripts/
%_libdir/mc/desktop-scripts/*
#
#
%_sbindir/*
#
#
%dir %_datadir/faces/
%_datadir/faces/*.png
%_datadir/faces/root
#
#
%_iconsdir/*.xpm
%_miconsdir/*
%_liconsdir/*
#
#
%_mandir/*/*
#
#
%dir %_datadir/mdk/
%dir %_datadir/mdk/faces/
%_datadir/mdk/faces/*
%_datadir/mdk/screensaver
#
%dir %_datadir/mdk/gnome-desktop/
%_datadir/mdk/gnome-desktop/*

%_datadir/nautilus/default-desktop
#
#
%dir %_datadir/pixmaps/backgrounds/
%dir %_datadir/pixmaps/backgrounds/linux-mandrake/
%_datadir/pixmaps/backgrounds/linux-mandrake/*
#

%dir %_datadir/pixmaps/mdk/
%_datadir/pixmaps/mdk/*
%_datadir/pixmaps/*.png
#
%_menudir/simplified/mandrake_desk


%files -n mdk-eazel-engine
%defattr(-,root,root,-)

%_datadir/eazel-engine

#
#
%dir %_libdir/gtk/
%dir %_libdir/gtk/themes/
%dir %_libdir/gtk/themes/engines/
%_libdir/gtk/themes/engines/*

%dir %_datadir/themes
%_datadir/themes/Crux
%_datadir/themes/Mandrake


%files -n mdk-eazel-engine-capplet
%defattr(-,root,root,-)
%_bindir/eazel-engine-capplet
%dir %_datadir/gnome/
%dir %_datadir/gnome/apps/
%dir %_datadir/gnome/apps/Settings/
%dir %_datadir/gnome/apps/Settings/Desktop/
%_datadir/gnome/apps/Settings/Desktop/*.desktop
%{_menudir}/mdk-eazel-engine-capplet
%{_datadir}/control-center/capplets/Advanced/*

%files -n krootwarning
%defattr(-,root,root,-)
%_bindir/krootwarning
#
#
%dir %_datadir/apps/krootwarning/
%dir %_datadir/apps/krootwarning/pics/
%_datadir/apps/krootwarning/pics/*.png
#
#
%dir %_datadir/applnk/Applications/
%_datadir/applnk/Applications/krootwarning.desktop

%dir %_datadir/autostart/
%_datadir/autostart/krootwarning.desktop

%config(noreplace) %_datadir/config/krootwarningrc

%files -n krozat
%defattr(-,root,root,-)
%_bindir/krozat.kss
#
#
%dir %_datadir/applnk/System/
%dir %_datadir/applnk/System/ScreenSavers/
%_datadir/applnk/System/ScreenSavers/*.desktop
#
#
%dir %_iconsdir/locolor/
%dir %_iconsdir/locolor/16x16/
%dir %_iconsdir/locolor/16x16/apps/
%_iconsdir/locolor/16x16/apps/krootwarning.png
#
%dir %_iconsdir/locolor/32x32/
%dir %_iconsdir/locolor/32x32/apps
%_iconsdir/locolor/32x32/apps/krootwarning.png
#
#
%_menudir/krozat

%changelog
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

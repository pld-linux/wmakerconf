Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	2.0
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	http://www-info2.informatik.uni-wuerzburg.de/staff/ulli/wmakerconf/%{name}-%{version}.tar.bz2
Source1:	wmakerconf.wmconfig
Source2:	wmakerconf.pl.po
Source3:	wmakerconf-data.pl.po
Patch0:		wmakerconf-pl.patch
Patch1:		wmakerconf-data-pl.patch
Icon:		wmakerconf.xpm
BuildPrereq:	libPropList-devel >= 0.8.3
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libungif-devel
BuildPrereq:	WindowMaker-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	zlib-devel
BuildPrereq:	autoconf
BuildPrereq:	automake
Requires:	WindowMaker
Requires:	wmakerconf-data
BuildRoot:	/tmp/%{name}-%{version}-root

%description
wmakerconf is a GTK+ based configuration tool for the window manager
WindowMaker.
Support of all WindowMaker attributes: Font selection browser, pixmap
preview browser, color selection dialog, shortcut dialog, file selection
dialog, etc. 
Tooltips with short description of every attribute.
New attributes can be simply integrated by changing the wmakerconf proplist

%description -l pl
wmakerconf jest opartym na GTK+ narzêdziem konfiguracyjnym dla WindowMakera.
Umo¿liwia zmianê czcionek, ikon, kolorów i pozosta³ych atrybutów przy
pomocy prostych narzêdzi dialogowych. 

%package data
Version:	0.53.0p2
Summary:	Data files for GTK-based configuration tool for Window Maker
Summary(pl):	Pliki danych dla opartego na GTK konfiguratora WindowMakera
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Requires:	WindowMaker = 0.53.0

%description data
Data files containing information relating to the latest version of
WindowMaker for use by wmakerconf, the WindowMaker configuration
tool

%description -l pl
Pakiet zawiera pliki danych dotycz±ce najnowszej wersji WindowMakera,
u¿ywane przez program wmakerconf -- narzêdzie konfiguracyjne tego
zarz±dcy okien.

%prep
%setup -q  
%patch0 -p0
%patch1 -p0

cp %{SOURCE2} po/pl.po
cp %{SOURCE3} data/po/pl.po

%build
%GNUconfigure -- --prefix=/usr/X11R6 --with-wmakerdataprefix=/usr/X11R6/share --with-wmakeretcprefix=/etc/X11 

make

cd data
./configure \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/X11R6/share/pixmaps,etc/X11/wmconfig}

make install DESTDIR=$RPM_BUILD_ROOT
make -C data prefix=$RPM_BUILD_ROOT/usr/X11R6 install

install $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmakerconf

strip $RPM_BUILD_ROOT/usr/X11R6/bin/*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%config /etc/X11/wmconfig/wmakerconf

%lang(ca)    /usr/X11R6/share/locale/ca/LC_MESSAGES/wmakerconf.mo
%lang(da)    /usr/X11R6/share/locale/da/LC_MESSAGES/wmakerconf.mo
%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/wmakerconf.mo
%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/wmakerconf.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/wmakerconf.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/wmakerconf.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/wmakerconf.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/wmakerconf.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/wmakerconf.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/wmakerconf.mo
%lang(pl)    /usr/X11R6/share/locale/pl/LC_MESSAGES/wmakerconf.mo
%lang(pt_BR) /usr/X11R6/share/locale/pt_BR/LC_MESSAGES/wmakerconf.mo
%lang(ru)    /usr/X11R6/share/locale/ru/LC_MESSAGES/wmakerconf.mo
%lang(sv)    /usr/X11R6/share/locale/sv/LC_MESSAGES/wmakerconf.mo

%attr(755,root,root) /usr/X11R6/bin/*
%dir /usr/X11R6/share/wmakerconf
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.sh
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.pl
/usr/X11R6/share/wmakerconf/*.xpm
/usr/X11R6/share/wmakerconf/*.jpg
/usr/X11R6/share/wmakerconf/MANUAL
/usr/X11R6/share/pixmaps/wmakerconf.xpm

%files data
%defattr(644,root,root,755)
/usr/X11R6/share/wmakerconf/WMWmakerconf
/usr/X11R6/share/wmakerconf/wmaker-version

%lang(ca)    /usr/X11R6/share/locale/ca/LC_MESSAGES/wmakerconf-data.mo
%lang(cz)    /usr/X11R6/share/locale/cz/LC_MESSAGES/wmakerconf-data.mo
%lang(da)    /usr/X11R6/share/locale/da/LC_MESSAGES/wmakerconf-data.mo
%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/wmakerconf-data.mo
%lang(el)    /usr/X11R6/share/locale/el/LC_MESSAGES/wmakerconf-data.mo
%lang(es)    /usr/X11R6/share/locale/es/LC_MESSAGES/wmakerconf-data.mo
%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/wmakerconf-data.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/wmakerconf-data.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/wmakerconf-data.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/wmakerconf-data.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/wmakerconf-data.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/wmakerconf-data.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/wmakerconf-data.mo
%lang(pl)    /usr/X11R6/share/locale/pl/LC_MESSAGES/wmakerconf-data.mo
%lang(pt_BR) /usr/X11R6/share/locale/pt_BR/LC_MESSAGES/wmakerconf-data.mo
%lang(ro)    /usr/X11R6/share/locale/ro/LC_MESSAGES/wmakerconf-data.mo
%lang(ru)    /usr/X11R6/share/locale/ru/LC_MESSAGES/wmakerconf-data.mo
%lang(sv)    /usr/X11R6/share/locale/sv/LC_MESSAGES/wmakerconf-data.mo
%lang(tr)    /usr/X11R6/share/locale/tr/LC_MESSAGES/wmakerconf-data.mo

%changelog
* Sat May  8 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.0-1]
- updated to 2.0,
- added wmakerconf-data subpackage,
- added "Requires: wmakerconf-data",
- removed wmakerconf-config.patch (no longer needed),
- added using %GNUconfigure macro and fixed configure options,
- added using DESTDIR to make install,
- added stripping binaries,
- fixed %config description,
- added pl locales for wmakerconf and wmakerconf-data.

* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.99.2-1]
- recompiles on new rpm.

* Sun Apr 11 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.99.0-1]
- upgraded to 1.99.0,
- removed --disable-gtktest and --disable-imlibtest
  from configure options by Artur Frysiak <wiget@pld.org.pl>,
- fixed passing $RPM_OPT_FLAGS during compile,
- added '%dir /usr/X11R6/share/wmakerconf' in %files,
- cosmetic changes for common l&f.

* Thu Mar 18 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.8.3-1]
- upgraded to 1.8.3.

* Wed Mar 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.8-1]
- upgraded to 1.8,
- added more requirements,
- added wmakerconf-config.patch,
- added --with-wmakersysdir=/etc/X11/WindowMaker and
  --with-wmakerprefix=/usr/X11R6 to configure options,
- removed --with-wmakerdir=DIR from configure options (no longer in use),
- added wmakerconf.wmconfig file,
- added more locales,
- minor changes in all sections.

* Tue Mar  2 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.7-1]
- upgraded to 1.7,
- updated data files for WindowMaker >= 0.51,
- added Polish summary, group and description,
- added --disable-imlibtest,
- added gzipping doc files,
- rewritten %files section,
- added %lang macro for /usr/X11R6/share/locale/*/LC_MESSAGES/*,
- major changes.

* Fri Nov  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.2-1d]
- added -q %setup parameter,
- removed Source1 (wmakerconf-libPropList.tar.gz) this is now in separated
  package,
- changed install prefix to /usr/X11R6,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added full %attr description in %files,
- changed install prefix to /usr/X11R6.

* Fri Sep 18 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2 to be used with WindowMaker

Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	2.1
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
Patch2:		wmakerconf-subdir.patch
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
BuildPrereq:	gettext
Requires:	WindowMaker
Requires:	wmakerconf-data
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix         /usr/X11R6
%define _sysconfdir     /etc/X11

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
%patch2 -p0

cp %{SOURCE2} po/pl.po
cp %{SOURCE3} data/po/pl.po

%build
%{GNUconfigure} --prefix=%{_prefix} \
	--with-wmakerdataprefix=%{_datadir} \
	--with-wmakeretcprefix=%{_sysconfdir} \
	--enable-themes-org

make

cd data
./configure \
	--prefix=%{_prefix}

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_datadir}/pixmaps,%{_sysconfdir}/wmconfig}

make install DESTDIR=$RPM_BUILD_ROOT
make -C data prefix=$RPM_BUILD_ROOT%{_prefix} install

install $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/wmconfig/%{name}

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%{_sysconfdir}/wmconfig/%{name}

%lang(ca)    %{_datadir}/locale/ca/LC_MESSAGES/%{name}.mo
%lang(da)    %{_datadir}/locale/da/LC_MESSAGES/%{name}.mo
%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%lang(fi)    %{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
%lang(fr)    %{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%lang(hu)    %{_datadir}/locale/hu/LC_MESSAGES/%{name}.mo
%lang(it)    %{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
%lang(ja)    %{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo
%lang(ko)    %{_datadir}/locale/ko/LC_MESSAGES/%{name}.mo
%lang(no)    %{_datadir}/locale/no/LC_MESSAGES/%{name}.mo
%lang(pl)    %{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
%lang(ru)    %{_datadir}/locale/ru/LC_MESSAGES/%{name}.mo
%lang(sv)    %{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo

%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.jpg
%{_datadir}/%{name}/MANUAL
%{_datadir}/pixmaps/%{name}.xpm

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}/WMWmakerconf
%{_datadir}/%{name}/wmaker-version

%lang(ca)    %{_datadir}/locale/ca/LC_MESSAGES/%{name}-data.mo
%lang(cz)    %{_datadir}/locale/cz/LC_MESSAGES/%{name}-data.mo
%lang(da)    %{_datadir}/locale/da/LC_MESSAGES/%{name}-data.mo
%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/%{name}-data.mo
%lang(el)    %{_datadir}/locale/el/LC_MESSAGES/%{name}-data.mo
%lang(es)    %{_datadir}/locale/es/LC_MESSAGES/%{name}-data.mo
%lang(fi)    %{_datadir}/locale/fi/LC_MESSAGES/%{name}-data.mo
%lang(fr)    %{_datadir}/locale/fr/LC_MESSAGES/%{name}-data.mo
%lang(hu)    %{_datadir}/locale/hu/LC_MESSAGES/%{name}-data.mo
%lang(it)    %{_datadir}/locale/it/LC_MESSAGES/%{name}-data.mo
%lang(ja)    %{_datadir}/locale/ja/LC_MESSAGES/%{name}-data.mo
%lang(ko)    %{_datadir}/locale/ko/LC_MESSAGES/%{name}-data.mo
%lang(no)    %{_datadir}/locale/no/LC_MESSAGES/%{name}-data.mo
%lang(pl)    %{_datadir}/locale/pl/LC_MESSAGES/%{name}-data.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}-data.mo
%lang(ro)    %{_datadir}/locale/ro/LC_MESSAGES/%{name}-data.mo
%lang(ru)    %{_datadir}/locale/ru/LC_MESSAGES/%{name}-data.mo
%lang(sv)    %{_datadir}/locale/sv/LC_MESSAGES/%{name}-data.mo
%lang(tr)    %{_datadir}/locale/tr/LC_MESSAGES/%{name}-data.mo

%changelog
* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.1-1]
- updated to 2.1,
- added wmakerconf-subdir.patch,
- added using more rpm macros,
- minor changes.

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

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
* Thu May 20 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [2.1-1]
- package is FHS 2.0 compliant,
- spec file based on RH version; rewritten for PLD use by me
  and Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>.

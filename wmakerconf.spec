Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	2.1
Release:	2
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	http://www-info2.informatik.uni-wuerzburg.de/staff/ulli/wmakerconf/%{name}-%{version}.tar.bz2
Source1:	wmakerconf.desktop
Source2:	wmakerconf.pl.po
Source3:	wmakerconf-data.pl.po
Patch0:		wmakerconf-pl.patch
Patch1:		wmakerconf-data-pl.patch
Patch2:		wmakerconf-subdir.patch
Icon:		wmakerconf.xpm
BuildRequires:	libPropList-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	WindowMaker-devel
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libwmfun
Requires:	WindowMaker
Requires:	wmakerconf-data
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

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
Requires:	WindowMaker >= 0.53.0

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
automake
aclocal
autoconf
%configure \
	--prefix=%{_prefix} \
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
install -d $RPM_BUILD_ROOT/{%{_datadir}/pixmaps,%{_sysconfdir}/applnk/Utilities}

make install DESTDIR=$RPM_BUILD_ROOT
make -C data prefix=$RPM_BUILD_ROOT%{_prefix} install

install $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/applnk/Utilities

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}
%find_lang %{name}-data

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%{_sysconfdir}/applnk/Utilities/wmakerconf.desktop

%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.jpg
%{_datadir}/%{name}/MANUAL
%{_datadir}/pixmaps/%{name}.xpm

%files data -f %{name}-data.lang
%defattr(644,root,root,755)
%{_datadir}/%{name}/WMWmakerconf
%{_datadir}/%{name}/wmaker-version

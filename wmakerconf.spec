Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	2.5
Release:	8
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://members.linuxstart.com/~ulli/wmakerconf/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.pl.po
Source3:	%{name}-data.pl.po
Patch0:		%{name}-data-locale.patch
Patch1:		%{name}-subdir.patch
Patch2:		%{name}-DESTDIR.patch
Icon:		wmakerconf.xpm
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	WindowMaker-devel >= 0.51.0
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libwmfun-devel >= 0.0.2
BuildRequires:	imlib-devel
Requires:	WindowMaker >= 0.62.1
Requires:	wmakerconf-data >= 0.62.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
wmakerconf is a GTK+ based configuration tool for the window manager
WindowMaker. Support of all WindowMaker attributes: Font selection
browser, pixmap preview browser, color selection dialog, shortcut
dialog, file selection dialog, etc. Tooltips with short description of
every attribute. New attributes can be simply integrated by changing
the wmakerconf proplist

%description -l pl
wmakerconf jest opartym na GTK+ narzêdziem konfiguracyjnym dla
WindowMakera. Umo¿liwia zmianê czcionek, ikon, kolorów i pozosta³ych
atrybutów przy pomocy prostych narzêdzi dialogowych.

%package data
Version:	0.62.1
Summary:	Data files for GTK-based configuration tool for Window Maker
Summary(pl):	Pliki danych dla opartego na GTK konfiguratora WindowMakera
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Requires:	WindowMaker = 0.62.1

%description data
Data files containing information relating to the latest version of
WindowMaker for use by wmakerconf, the WindowMaker configuration tool

%description -l pl
Pakiet zawiera pliki danych dotycz±ce najnowszej wersji WindowMakera,
u¿ywane przez program wmakerconf -- narzêdzie konfiguracyjne tego
zarz±dcy okien.

%prep
%setup -q 
%patch0 -p1
%patch1 -p0
%patch2 -p1

cp -f %{SOURCE2} po/pl.po
cp %{SOURCE3} data/po/pl.po

%build
gettextize --copy --force
automake; (cd data; automake)
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-wmakerdataprefix=%{_datadir} \
	--with-wmakeretcprefix=%{_sysconfdir} \
	--enable-themes-org
%{__make}

cd data
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_datadir}/pixmaps,%{_applnkdir}/Utilities}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} -C data DESTDIR=$RPM_BUILD_ROOT install

install $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}
%find_lang %{name}-data

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%{_applnkdir}/Utilities/wmakerconf.desktop

%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/MANUAL
%{_datadir}/pixmaps/%{name}.xpm

%files data -f %{name}-data.lang
%defattr(644,root,root,755)
%{_datadir}/%{name}/WMWmakerconf
%{_datadir}/%{name}/wmaker-version

Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	1.7
Release:	1
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Copyright:	GPL
Source:		http://www-info2.informatik.uni-wuerzburg.de/staff/ulli/wmakerconf/%{name}-%{version}.tar.gz
Icon:		wmakerconf.xpm
Requires:	WindowMaker >= 0.51
Requires:	libPropList
Requires:       perl
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

%prep
%setup -q  

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--with-wmakerdir=/usr/X11R6/share/WindowMaker \
	--disable-gtktest \
	--disable-imlibtest
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6

gzip -9nf AUTHORS ChangeLog NEWS README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz TODO.gz

%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.sh
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.pl
/usr/X11R6/share/wmakerconf/*.xpm
/usr/X11R6/share/wmakerconf/*.jpg
/usr/X11R6/share/wmakerconf/MANUAL
/usr/X11R6/share/wmakerconf/WM*
/usr/X11R6/share/wmakerconf/wmaker-version

%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/*

%changelog
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

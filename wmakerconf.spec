Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Name:		wmakerconf
Version:	1.8
Release:	1
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Copyright:	GPL
Source0:	http://www-info2.informatik.uni-wuerzburg.de/staff/ulli/wmakerconf/%{name}-%{version}.tar.bz2
Source1:	wmakerconf.wmconfig
Patch0:		wmakerconf-config.patch
Icon:		wmakerconf.xpm
Requires:	WindowMaker >= 0.51.2
Requires:	libPropList
Requires:	gtk+ 
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
%patch0 -p1

%build
autoconf
./configure \
	--prefix=/usr/X11R6 \
	--with-wmakerprefix=/usr/X11R6 \
	--with-wmakersysdir=/etc/X11/WindowMaker \
	--disable-gtktest \
	--disable-imlibtest

make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6
install -d $RPM_BUILD_ROOT/{usr/X11R6/share/pixmaps,etc/X11/wmconfig}
install $RPM_SOURCE_DIR/wmakerconf.xpm $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmakerconf

gzip -9nf AUTHORS ChangeLog NEWS README TODO MANUAL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz TODO.gz
%config(missingok) /etc/X11/wmconfig/wmakerconf

%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.sh
%attr(755,root,root) /usr/X11R6/share/wmakerconf/*.pl
/usr/X11R6/share/wmakerconf/*.xpm
/usr/X11R6/share/wmakerconf/*.jpg
/usr/X11R6/share/wmakerconf/MANUAL
/usr/X11R6/share/wmakerconf/WMWmakerconf
/usr/X11R6/share/wmakerconf/wmaker-version
/usr/X11R6/share/pixmaps/wmakerconf.xpm

%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/*
%lang(cz) /usr/X11R6/share/locale/cz/LC_MESSAGES/*
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/*
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/*
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/*
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/*
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/*
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/*
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/*
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/*
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/*
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/*
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/*
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/*
%lang(tr) /usr/X11R6/share/locale/tr/LC_MESSAGES/*

%changelog
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

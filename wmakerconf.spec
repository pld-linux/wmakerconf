Summary:	This is a GTK-based configuration tool for WindowMaker
Name:		wmakerconf
Version:	1.1.2
Release:	1
Group:		X11/Window Managers
Copyright:	GPL
Source0:	http://www-info2.informatik.uni-wuerzburg.de/staff/ulli/wmakerconf/%{name}-%{version}.tar.gz
Requires:	WindowMaker
Requires:	perl
BuildRoot:	/tmp/%{name}-%{version}-root

%description
wmakerconf is a GTK+ based configuration tool for the window manager
WindowMaker.

Support of all WindowMaker attributes: Font selection browser, pixmap
preview browser, color selection dialog, shortcut dialog, file selection
dialog, ... 

Tooltips with short description of every attribute. 

New attributes can be simply integrated by changing the wmakerconf proplist

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--with-wmakerdir=/usr/X11R6/share/WindowMaker \
	--disable-gtktest
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/X11R6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README TODO
/usr/X11R6/bin/*
/usr/Z11R6/share/wmakerconf

%changelog
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

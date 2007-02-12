Summary:	This is a GTK+-based configuration tool for WindowMaker
Summary(es.UTF-8):   Herramienta de configuración basada en GTK+ para WindowMaker
Summary(pl.UTF-8):   Oparty na GTK+ konfigurator dla WindowMakera
Summary(pt_BR.UTF-8):   Ferramenta de configuração baseada no GTK+ para o WindowMaker
Name:		wmakerconf
Version:	2.9
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.windowmaker.org/pub/contrib/source/wmakerconf/%{name}-%{version}.tar.bz2
# Source0-md5:	da02991fc9e8e09c99c1d159f45afe1e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-subdir.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-charset.patch
Patch3:		%{name}-misc.patch
Patch4:		%{name}-ia64+mkstemp.patch
#URL:		http://ulli.on.openave.net/wmakerconf/
BuildRequires:	WindowMaker-devel >= 0.51.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
# BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
Requires:	WindowMaker >= 0.62.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	wmakerconf-data

%define		_sysconfdir	/etc/X11

%description
wmakerconf is a GTK+ based configuration tool for the window manager
WindowMaker. Support of all WindowMaker attributes: Font selection
browser, pixmap preview browser, color selection dialog, shortcut
dialog, file selection dialog, etc. Tooltips with short description of
every attribute. New attributes can be simply integrated by changing
the wmakerconf proplist

%description -l es.UTF-8
Herramienta de configuración basada en GTK+ para el administrador de
ventanas Window Maker. Soporta todos los atributos del Window Maker:
navegador para selección de fuentes, navegador para visualizar
pixmaps, caja de diálogo para selección de colores, caja de diálogo
para accesos directos, caja de diálogo para selección de archivos,...
Trucos en todos los atributos. Nuevos atributos se pueden integrar de
forma sencilla, cambiando la lista de propiedades del wmakerconf.

%description -l pl.UTF-8
wmakerconf jest opartym na GTK+ narzędziem konfiguracyjnym dla
WindowMakera. Umożliwia zmianę czcionek, ikon, kolorów i pozostałych
atrybutów przy pomocy prostych narzędzi dialogowych.

%description -l pt_BR.UTF-8
Ferramenta de configuração baseada em GTK+ para o gerenciador de
janelas Window Maker. Suporta todos os atributos do Window Maker:
navegador para seleção de fontes, navegador para visualização de
pixmaps, caixa de diálogo para seleção de cores, caixa de diálogo para
atalhos, caixa de diálogo para seleção de arquivos, ... Dicas em todos
os atributos. Novos atributos podem ser integrados de forma simples,
mudando a lista de propriedades do wmakerconf.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
(cd data
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake})
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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Settings/WindowMaker}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} install -C data DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/WindowMaker
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.sh
%attr(755,root,root) %{_datadir}/%{name}/*.pl
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/MANUAL
%{_datadir}/%{name}/WMWmakerconf
%{_datadir}/%{name}/wmaker-version
%{_applnkdir}/Settings/WindowMaker/wmakerconf.desktop
%{_pixmapsdir}/*

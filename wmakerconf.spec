Summary:	This is a GTK-based configuration tool for WindowMaker
Summary(es):	Herramienta de configuraci�n basada en GTK para WindowMaker
Summary(pl):	Oparty na GTK konfigurator dla WindowMakera
Summary(pt_BR):	Ferramenta de configura��o baseada no GTK para o WindowMaker
Name:		wmakerconf
Version:	2.8.1
Release:	7
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://ulli.on.openave.net/wmakerconf/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-subdir.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-charset.patch
Patch3:		%{name}-misc.patch
Patch4:		%{name}-ia64+mkstemp.patch
Icon:		wmakerconf.xpm
URL:		http://ulli.on.openave.net/wmakerconf/
BuildRequires:	WindowMaker-devel >= 0.51.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libPropList-devel >= 0.8.3
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
Requires:	WindowMaker >= 0.62.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	wmakerconf-data

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
wmakerconf is a GTK+ based configuration tool for the window manager
WindowMaker. Support of all WindowMaker attributes: Font selection
browser, pixmap preview browser, color selection dialog, shortcut
dialog, file selection dialog, etc. Tooltips with short description of
every attribute. New attributes can be simply integrated by changing
the wmakerconf proplist

%description -l es
Herramienta de configuraci�n basada en GTK+ para el administrador de
ventanas Window Maker. Soporta todos los atributos del Window Maker:
navegador para selecci�n de fuentes, navegador para visualizar
pixmaps, caja de di�logo para selecci�n de colores, caja de di�logo
para accesos directos, caja de di�logo para selecci�n de archivos,...
Trucos en todos los atributos. Nuevos atributos se pueden integrar de
forma sencilla, cambiando la lista de propiedades del wmakerconf.

%description -l pl
wmakerconf jest opartym na GTK+ narz�dziem konfiguracyjnym dla
WindowMakera. Umo�liwia zmian� czcionek, ikon, kolor�w i pozosta�ych
atrybut�w przy pomocy prostych narz�dzi dialogowych.

%description -l pt_BR
Ferramenta de configura��o baseada em GTK+ para o gerenciador de
janelas Window Maker. Suporta todos os atributos do Window Maker:
navegador para sele��o de fontes, navegador para visualiza��o de
pixmaps, caixa de di�logo para sele��o de cores, caixa de di�logo para
atalhos, caixa de di�logo para sele��o de arquivos, ... Dicas em todos
os atributos. Novos atributos podem ser integrados de forma simples,
mudando a lista de propriedades do wmakerconf.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
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
install -d $RPM_BUILD_ROOT/{%{_pixmapsdir},%{_applnkdir}/Settings/WindowMaker}

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

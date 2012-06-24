Summary:	amaroc - ncurses frontend for Amarok
Summary(de):	amaroc - ncurses Frontend f�r Amarok
Summary(pl):	amaroc - frontend ncurses dla Amaroka
Name:		amaroc
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/amaroc/%{name}-%{version}.tar.bz2
# Source0-md5:	38308e04b2bd0f7df94d19f2455b70df
Patch0:		%{name}-curses.patch
Requires:	amarok
Requires:	python
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amaroc is an ncurses frontend for Amarok. It uses DCOP calls and its
purpose is to ease control of Amarok over a network.

%description -l de
Amaroc ist ein ncurses Frontend f�r Amarok. Es benutzt DCOP Aufruffe
und es vereinfacht die Nutzung von Amarok �bers Netzwerk.

%description -l pl
Amaroc jest frontendem ncurses dla Amaroka. U�ywa wezwa� DCOPu i
u�atwia u�ywanie Amaroka przez sie�.

%prep
%setup -q
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install amaroc.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/amaroc.py

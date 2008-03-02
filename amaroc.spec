Summary:	amaroc - ncurses frontend for Amarok
Summary(de.UTF-8):	amaroc - ncurses Frontend für Amarok
Summary(pl.UTF-8):	amaroc - frontend ncurses dla Amaroka
Name:		amaroc
Version:	0.3
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/amaroc/%{name}-%{version}.tar.bz2
# Source0-md5:	38308e04b2bd0f7df94d19f2455b70df
Patch0:		%{name}-curses.patch
URL:		http://sourceforge.net/projects/amaroc/
BuildRequires:	sed >= 4.0
Requires:	amarok
Requires:	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amaroc is an ncurses frontend for Amarok. It uses DCOP calls and its
purpose is to ease control of Amarok over a network.

%description -l de.UTF-8
Amaroc ist ein ncurses Frontend für Amarok. Es benutzt DCOP Aufrufe
und es vereinfacht die Nutzung von Amarok übers Netzwerk.

%description -l pl.UTF-8
Amaroc jest frontendem ncurses dla Amaroka. Używa wywołan DCOP i
ułatwia używanie Amaroka przez sieć.

%prep
%setup -q
%patch0 -p0
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' amaroc.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install amaroc.py $RPM_BUILD_ROOT%{_bindir}/amaroc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/amaroc

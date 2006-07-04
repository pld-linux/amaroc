Summary:	amaroc - ncurses frontend for Amarok
Summary(de):	amaroc - ncurses Frontend für Amarok
Summary(pl):	amaroc - frontend ncurses dla Amaroka
Name:		amaroc
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/amaroc/%{name}-%{version}.tar.bz2
# Source0-md5:	7191b83e2b66d161a7cd8f463f5181d7
Requires:	amarok
Requires:	ncurses
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amaroc is an ncurses frontend for Amarok. It uses DCOP calls and its
purpose is to ease control of Amarok over a network.

%description -l de
Amaroc ist ein ncurses Frontend für Amarok. Es benutzt DCOP Aufruffe
und es vereinfacht die Nutzung von Amarok übers Netzwerk.

%description -l pl
Amaroc jest frontendem ncurses dla Amaroka. U¿ywa wezwañ DCOPu i
u³atwia u¿ywanie Amaroka poprzez sieæ.

%prep
%setup -q

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

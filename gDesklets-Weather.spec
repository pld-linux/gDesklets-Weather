%define	pname	Weather
Summary:	A sensor and display for displaying the current weather information
Summary(pl):	Czujnik i wy¶wietlacz do pokazywania aktualnej informacji pogodowej
Name:		gDesklets-%{pname}
Version:	0.24
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/weather-desklet-%{version}.tar.bz2
# Source0-md5:	f10d7cdb043b9f461a52e5d1226ddbdf
URL:		http://gdesklets.gnomedesktop.org/
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
Provides:	gDesklets-display
Provides:	gDesklets-sensor
Conflicts:	gDesklets-StarterKit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define _displaysdir	%{_datadir}/gdesklets/Displays

%description
A sensor and display for displaying the current weather information.
It can retrieve information for many countries of the world.

%description -l pl
Czujnik i wy¶wietlacz do pokazywania aktualnej informacji pogodowej.
Mo¿e zbieraæ informacje dla wielu krajów ¶wiata.

%prep
%setup -q -n weather-desklet-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

rm -rf $RPM_BUILD_ROOT%{_sensorsdir}/%{pname}/{.*~,icons/.xvpics,po}
find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sensorsdir}/%{pname}
%dir %{_sensorsdir}/%{pname}/locale
%{_sensorsdir}/%{pname}/icons
%{_sensorsdir}/%{pname}/*.py[co]
%{_sensorsdir}/%{pname}/ChangeLog
%{_displaysdir}/*

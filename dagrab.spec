%define name dagrab
%define version 0.3.5
%define release %mkrel 10

Name: %{name}  
Summary: A CD ripper
Version: %{version} 
Release: %{release}
Source: %{name}-%{version}.tar.bz2
UrL: http://web.tiscalinet.it:/marcellou/dagrab.html
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL

%description
Dagrab is a digital audio grabber designed to rip sound tracks from an audio 
cd to wave files.

%prep

%setup -q 

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 dagrab $RPM_BUILD_ROOT%{_bindir}/
install -m 755 -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 dagrab.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*


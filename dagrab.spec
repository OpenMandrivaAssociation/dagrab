%define name dagrab
%define version 0.3.5
%define release %mkrel 12

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-12mdv2011.0
+ Revision: 617514
- the mass rebuild of 2010.0 packages

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.5-11mdv2010.0
+ Revision: 449510
- rebuild for missing binaries

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.3.5-10mdv2010.0
+ Revision: 426818
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.5-9mdv2009.0
+ Revision: 243887
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 7mdv2008.1-current
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import dagrab


* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 0.3.5-7mdv2007.0
- rebuild

* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 0.3.5-6mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-5mdk
- rebuild

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-4mdk
- rebuild

* Wed Aug 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-3mdk
- rebuild

* Mon Jun 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-2mdk
- rebuild

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.5-1mdk 
- updated to 0.3.5
- add url

* Mon Jul 31 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3.3-5mdk
- BM
- add some doc
- spec cleaning

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.3.3-4mdk
- fix group
- spec helper fixes

* Wed Dec 22 1999 Lenny Cartier <lenny@mandrakesoft.com>
- fix location of files

* Tue Nov 02 1999 Lenny Cartier <lenny@mandrakesoft.com>
- First specfile for Mandrake / New contrib

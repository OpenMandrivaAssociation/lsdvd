Name:		lsdvd
Summary:	Reads and prints the contents of a dvd in plain English
Version:	0.17
Release:	1
Source:		https://sourceforge.net/projects/lsdvd/files/lsdvd/lsdvd-%{version}.tar.gz
URL:		https://untrepid.com/lsdvd/
License:	GPLv2
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libdvdread-devel >= 0.9.4

%description
Lsdvd reads and prints the contents of a dvd to your terminal in plain, but
very parsable, English. Lsdvd in turn uses libdvdread, the most popular dvd
reading library for *nix.

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16-9mdv2011.0
+ Revision: 612772
- the mass rebuild of 2010.1 packages

* Fri Apr 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.16-8mdv2010.1
+ Revision: 530780
- add patch to fix string format (spotted by Matthew Dawkins)
- fix license
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.16-6mdv2009.0
+ Revision: 278254
- rebuild for new libdvdread

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.16-5mdv2009.0
+ Revision: 251494
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.16-3mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.16-3mdv2007.0
+ Revision: 111085
- forgot to add - fix #25190 :(

* Sat Jan 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.16-2mdv2007.1
+ Revision: 110992
- Import lsdvd


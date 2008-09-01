%define name	lsdvd
%define version	0.16
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Reads and prints the contents of a dvd in plain English
Version: 	%{version}
Release: 	%{release}
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.16-configure.patch
Patch1:		%{name}-0.16-include-order.patch
Patch2:		%{name}-0.16-ocode.patch
URL:		http://untrepid.com/lsdvd/
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libdvdread-devel >= 0.9.4

%description
Lsdvd reads and prints the contents of a dvd to your terminal in plain, but
very parsable, English. Lsdvd in turn uses libdvdread, the most popular dvd
reading library for *nix.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%configure2_5x

%make
										
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*



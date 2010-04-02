Name:		lsdvd
Summary:	Reads and prints the contents of a dvd in plain English
Version:	0.16
Release:	%mkrel 8
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.16-configure.patch
Patch1:		%{name}-0.16-include-order.patch
Patch2:		%{name}-0.16-ocode.patch
Patch3:		%{name}-0.16-fix-string-format.patch
URL:		http://untrepid.com/lsdvd/
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
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

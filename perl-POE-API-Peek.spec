%define upstream_name    POE-API-Peek
%define upstream_version 2.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Epoch:		1

Summary:	Peek into the internals of a running POE environment
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-API-Peek-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Size)
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
POE::API::Peek extends the POE::Kernel interface to provide clean access to 
Kernel internals in a cross-version compatible manner. Other calculated 
data is also available.

%prep
%setup -q -n POE-API-Peek-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/POE
%{_mandir}/man3/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.170.0-1mdv2011.0
+ Revision: 684784
- update to new version 2.17

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.160.0-1mdv2011.0
+ Revision: 596008
- update to new version 2.16

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.340.0-1mdv2010.0
+ Revision: 406180
- rebuild using %%perl_convert_version

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.34-1mdv2010.0
+ Revision: 372166
- update to new version 1.34

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.32-1mdv2009.0
+ Revision: 270394
- update to new version 1.32

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:1.30-2mdv2009.0
+ Revision: 268699
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.30-1mdv2009.0
+ Revision: 210843
- set epoch...
- new version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0802-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0802-1mdv2008.0
+ Revision: 25176
- 1.0802


* Mon Jan 30 2006 Michael Scherer <misc@mandriva.org> 1.06-2mdk
- BuildRequires

* Tue Jan 24 2006 Michael Scherer <misc@mandriva.org> 1.06-1mdk
- First Mandriva package



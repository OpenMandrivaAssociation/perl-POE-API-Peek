%define realname   POE-API-Peek

Name:		perl-%{realname}
Version:    1.0802
Release:    %mkrel 1
License:	Artistic
Group:		Development/Perl
Summary:    Peek into the internals of a running POE environment
Source0:    http://search.cpan.org/CPAN/authors/id/S/SU/SUNGO/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel perl-Devel-Size perl-POE
BuildArch: noarch

%description
POE::API::Peek extends the POE::Kernel interface to provide clean access to 
Kernel internals in a cross-version compatible manner. Other calculated 
data is also available.

%prep
%setup -q -n POE-API-Peek-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/POE
%{_mandir}/man3/*


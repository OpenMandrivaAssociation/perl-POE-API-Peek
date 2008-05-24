%define module   POE-API-Peek

Name:		perl-%{module}
Version:    1.30
Release:    %mkrel 1
License:	Artistic
Group:		Development/Perl
Summary:    Peek into the internals of a running POE environment
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.gz
BuildRequires:	perl(Devel::Size)
BuildRequires:	perl(POE)
BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/POE
%{_mandir}/man3/*


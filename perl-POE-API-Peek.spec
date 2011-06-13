%define upstream_name    POE-API-Peek
%define upstream_version 2.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Peek into the internals of a running POE environment
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Devel::Size)
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::NoWarnings)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
POE::API::Peek extends the POE::Kernel interface to provide clean access to 
Kernel internals in a cross-version compatible manner. Other calculated 
data is also available.

%prep
%setup -q -n POE-API-Peek-%{upstream_version}

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

%define	pdir	File
%define	pnam	CounterFile
%include	/usr/lib/rpm/macros.perl
Summary:	File-CounterFile perl module
Summary(pl):	Modu� perla File-CounterFile
Name:		perl-File-CounterFile
Version:	0.12
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-CounterFile - Persistent counter class.

%description -l pl
Modu� perla File-CounterFile.

%prep
%setup -q -n File-CounterFile-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/CounterFile.pm
%{_mandir}/man3/*

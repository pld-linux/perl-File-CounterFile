#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	CounterFile
Summary:	File::CounterFile Perl module
Summary(cs):	Modul File::CounterFile pro Perl
Summary(da):	Perlmodul File::CounterFile
Summary(de):	File::CounterFile Perl Modul
Summary(es):	Módulo de Perl File::CounterFile
Summary(fr):	Module Perl File::CounterFile
Summary(it):	Modulo di Perl File::CounterFile
Summary(ja):	File::CounterFile Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	File::CounterFile ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul File::CounterFile
Summary(pl):	Modu³ Perla File::CounterFile
Summary(pt):	Módulo de Perl File::CounterFile
Summary(pt_BR):	Módulo Perl File::CounterFile
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl File::CounterFile
Summary(sv):	File::CounterFile Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl File::CounterFile
Summary(zh_CN):	File::CounterFile Perl Ä£¿é
Name:		perl-File-CounterFile
Version:	1.00
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::CounterFile - Persistent counter class.

%description -l pl
Modu³ perla File::CounterFile.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/File/CounterFile.pm
%{_mandir}/man3/*

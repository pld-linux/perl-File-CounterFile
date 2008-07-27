#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	CounterFile
Summary:	File::CounterFile - persistent counter class
Summary(pl.UTF-8):	File::CounterFile - klasa trwałych liczników
Name:		perl-File-CounterFile
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df77e2dbc80aa3ec9647a570bb5e0cf8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::CounterFile Perl module implements a persistent counter
class. Each counter is represented by a separate file in the file
system. File locking is applied, so multiple processes might try to
access the same counters at the same time without risk of counter
destruction.

%description -l pl.UTF-8
Moduł Perla File::CounterFile stanowi implementację klasy trwałych
liczników. Każdy z liczników jest reprezentowany przez osobny plik w
systemie plików. Można stosować są blokady plików, aby z tych samych
liczników mogło korzystać jednocześnie wiele procesów, bez ryzyka
uszkodzenia licznika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*

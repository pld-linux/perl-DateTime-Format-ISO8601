#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-ISO8601
Summary:	DateTime::Format::ISO8601 - Parses ISO8601 formats
Summary(pl.UTF-8):	DateTime::Format::ISO8601 - analizowanie formatów opisanych przez ISO8601
Name:		perl-DateTime-Format-ISO8601
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JH/JHOBLITT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e0faf82577b4d7a9b116fc5a6825728
URL:		http://search.cpan.org/dist/DateTime-Format-ISO8601/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Format-Builder >= 0.6
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses ISO8601 formats.

%description -l pl.UTF-8
Analizowanie formatów opisanych przez ISO8601.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*

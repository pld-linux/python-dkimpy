#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module		dkimpy
Summary:	DKIM, ARC, and TLSRPT email signing and verification
Summary(pl.UTF-8):	Podpisywanie i weryfikacja e-maili DKIM, ARC oraz TLSRPT
Name:		python-%{module}
# keep 1.0.x for python2 support
Version:	1.0.5
Release:	6
License:	BSD-like
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/dkimpy/%{module}-%{version}.tar.gz
# Source0-md5:	080909e6557c01bb4855e37cd53d3e39
URL:		https://launchpad.net/dkimpy
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyNaCl
BuildRequires:	python-authres
BuildRequires:	python-dns >= 1.16
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module that implements DKIM (DomainKeys Identified Mail) email
signing and verification (RFC 6376).

%description -l pl.UTF-8
Moduł Pythona implementujący podpisywanie i weryfikację e-maili DKIM
(DomainKeys Identified Mail).

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
%{__python} test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%if 0
%attr(755,root,root) %{_bindir}/arcsign
%attr(755,root,root) %{_bindir}/arcverify
%attr(755,root,root) %{_bindir}/dkimsign
%attr(755,root,root) %{_bindir}/dkimverify
%attr(755,root,root) %{_bindir}/dknewkey
%{_mandir}/man1/arcsign.1*
%{_mandir}/man1/arcverify.1*
%{_mandir}/man1/dkimsign.1*
%{_mandir}/man1/dkimverify.1*
%{_mandir}/man1/dknewkey.1*
%endif
%{py_sitescriptdir}/dkim
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

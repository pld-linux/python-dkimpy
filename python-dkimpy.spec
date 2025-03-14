#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		dkimpy
Summary:	DKIM, ARC, and TLSRPT email signing and verification
Summary(pl.UTF-8):	Podpisywanie i weryfikacja e-maili DKIM, ARC oraz TLSRPT
Name:		python-%{module}
Version:	1.1.6
Release:	3
License:	BSD-like
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/dkimpy/%{module}-%{version}.tar.gz
# Source0-md5:	aa35e37730062d5d9f62eb98d24c4824
URL:		https://launchpad.net/dkimpy
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyNaCl
BuildRequires:	python-authres
BuildRequires:	python-dns >= 1.16
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyNaCl
BuildRequires:	python3-authres
BuildRequires:	python3-dns >= 1.16
%endif
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

%package -n python3-%{module}
Summary:	DKIM, ARC, and TLSRPT email signing and verification
Summary(pl.UTF-8):	Podpisywanie i weryfikacja e-maili DKIM, ARC oraz TLSRPT
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Python module that implements DKIM (DomainKeys Identified Mail) email
signing and verification (RFC 6376).

%description -n python3-%{module} -l pl.UTF-8
Moduł Pythona implementujący podpisywanie i weryfikację e-maili DKIM
(DomainKeys Identified Mail).

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%if %{without python3}
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
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
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
%{py3_sitescriptdir}/dkim
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

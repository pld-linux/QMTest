%define	tarname	qmtest
Summary:	Testing tool
Summary(pl.UTF-8):	Narzędzie do przeprowadzania testów
Name:		QMTest
Version:	2.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.codesourcery.com/public/qmtest/%{tarname}-%{version}/%{tarname}-%{version}.tar.gz
# Source0-md5:	b1c7cd4aa78a0fda1a6598ece98f6033
Patch0:		%{name}-python25.patch
URL:		http://www.codesourcery.com/qmtest/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QMTest is a general purpose testing solution that can be used to
implement a robust, easy-to-use testing process.

%description -l pl.UTF-8
QMTest jest ogólnego zastosowania narzędziem służącym do implementacji
silnego i łatwego w użyciu procesu testowego.

%prep
%setup -q -n %{tarname}-%{version}
#%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
mv $RPM_BUILD_ROOT%{_docdir}/%{tarname} _docs
rm _docs/COPYING

%py_postclean

# Regenerate configuration cleaned above (it's broken anyway)
rm $RPM_BUILD_ROOT%{py_sitedir}/qm/config.py*
cat > $RPM_BUILD_ROOT%{py_sitedir}/qm/config.py <<EOF
version='%{version}'
data_dir='%{_datadir}/%{tarname}'
doc_dir='%{_docdir}/%{name}-%{version}'
extension_path=data_dir+'/site-extensions-2.5'
prefix='%{_prefix}'
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc _docs/*
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/qm
%{_datadir}/%{tarname}

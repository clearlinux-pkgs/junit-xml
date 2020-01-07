#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : junit-xml
Version  : 1.8
Release  : 6
URL      : https://files.pythonhosted.org/packages/a6/2a/f8d5aab80bb31fcc789d0f2b34b49f08bd6121cd8798d2e37f416df2b9f8/junit-xml-1.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/2a/f8d5aab80bb31fcc789d0f2b34b49f08bd6121cd8798d2e37f416df2b9f8/junit-xml-1.8.tar.gz
Summary  : Creates JUnit XML test result documents that can be read by tools such as Jenkins
Group    : Development/Tools
License  : MIT
Requires: junit-xml-license = %{version}-%{release}
Requires: junit-xml-python = %{version}-%{release}
Requires: junit-xml-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
================

%package license
Summary: license components for the junit-xml package.
Group: Default

%description license
license components for the junit-xml package.


%package python
Summary: python components for the junit-xml package.
Group: Default
Requires: junit-xml-python3 = %{version}-%{release}

%description python
python components for the junit-xml package.


%package python3
Summary: python3 components for the junit-xml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the junit-xml package.


%prep
%setup -q -n junit-xml-1.8
cd %{_builddir}/junit-xml-1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574288037
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/junit-xml
cp %{_builddir}/junit-xml-1.8/LICENSE.txt %{buildroot}/usr/share/package-licenses/junit-xml/4415e5a8bc0b1196e15519ac1251f9cc07fb45c3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/junit-xml/4415e5a8bc0b1196e15519ac1251f9cc07fb45c3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

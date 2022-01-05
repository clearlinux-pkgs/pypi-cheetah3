#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cheetah3
Version  : 3.2.6.post1
Release  : 29
URL      : https://files.pythonhosted.org/packages/23/33/ace0250068afca106c1df34348ab0728e575dc9c61928d216de3e381c460/Cheetah3-3.2.6.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/33/ace0250068afca106c1df34348ab0728e575dc9c61928d216de3e381c460/Cheetah3-3.2.6.post1.tar.gz
Summary  : Cheetah is a template engine and code generation tool
Group    : Development/Tools
License  : MIT
Requires: pypi-cheetah3-bin = %{version}-%{release}
Requires: pypi-cheetah3-license = %{version}-%{release}
Requires: pypi-cheetah3-python = %{version}-%{release}
Requires: pypi-cheetah3-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: Cheetah3
Provides: Cheetah3-python
Provides: Cheetah3-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
It can be used standalone or combined with other tools and frameworks. Web
        development is its principle use, but Cheetah is very flexible and
        is also being used to generate C++ game code, Java, sql, form emails
        and even Python code.
        
        It's a fork of the original CheetahTemplate library.
        
        Documentation
        ================================================================================
        For a high-level introduction to Cheetah please refer to the User's Guide

%package bin
Summary: bin components for the pypi-cheetah3 package.
Group: Binaries
Requires: pypi-cheetah3-license = %{version}-%{release}

%description bin
bin components for the pypi-cheetah3 package.


%package license
Summary: license components for the pypi-cheetah3 package.
Group: Default

%description license
license components for the pypi-cheetah3 package.


%package python
Summary: python components for the pypi-cheetah3 package.
Group: Default
Requires: pypi-cheetah3-python3 = %{version}-%{release}

%description python
python components for the pypi-cheetah3 package.


%package python3
Summary: python3 components for the pypi-cheetah3 package.
Group: Default
Requires: python3-core
Provides: pypi(cheetah3)

%description python3
python3 components for the pypi-cheetah3 package.


%prep
%setup -q -n Cheetah3-3.2.6.post1
cd %{_builddir}/Cheetah3-3.2.6.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641422663
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cheetah3
cp %{_builddir}/Cheetah3-3.2.6.post1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cheetah3/a7186cce21fd72616b0fde6964715d4c16ea0c19
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheetah
/usr/bin/cheetah-analyze
/usr/bin/cheetah-compile

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cheetah3/a7186cce21fd72616b0fde6964715d4c16ea0c19

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

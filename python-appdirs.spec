%global modname appdirs
%bcond_without python3

Name:          python-%{modname}
Version:       1.4.0
Release:       3%{?dist}
Summary:       Python module for determining platform-specific directories

License:       MIT
URL:           http://github.com/ActiveState/appdirs
Source0:       https://pypi.python.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz

BuildRequires: python2-devel python-setuptools
BuildArch:     noarch

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%if %{with python3}
%package -n python3-%{modname}
Summary:       Python 3 module for determining platform-specific directoriess

BuildRequires:  python3-devel python3-setuptools

%description -n python3-%{modname}
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".
%endif

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%py2_build

%if %{with python3}
pushd %{py3dir}
  %py3_build
popd
%endif

%install
%py2_install

%if %{with python3}
pushd %{py3dir}
  %py3_install
popd
%endif

sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python2_sitelib}/%{modname}.py
%if %{with python3}
  sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{modname}.py
%endif

%check
%{__python2} setup.py test

%if %{with python3}
pushd %{py3dir}
  %{__python3} setup.py test
popd
%endif

%files
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python2_sitelib}/%{modname}.*
%{python2_sitelib}/%{modname}-%{version}-py?.?.egg-info/

%if %{with python3}
%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.cpython-??.py*
%{python3_sitelib}/%{modname}-%{version}-py?.?.egg-info/
%endif

%changelog
* Sun Aug 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-3
- Use modern python rpm macros

* Mon Jul 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-2
- Include CHANGES.rst in doc
- use python2-devel in BR instead of python-devel
- run tests

* Fri May 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package

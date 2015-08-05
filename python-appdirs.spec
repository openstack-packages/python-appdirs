%global modname appdirs

Name:          python-%{modname}
Version:       1.4.0
Release:       4%{?dist}
Summary:       Python module for determining platform-specific directories

License:       MIT
URL:           http://github.com/ActiveState/appdirs
Source0:       https://pypi.python.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz

BuildRequires: python2-devel python-setuptools
BuildRequires: python3-devel python3-setuptools
BuildArch:     noarch

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%package -n python2-%{modname}
Summary:       Python 2 module for determining platform-specific directoriess
%{?python_provide:%python_provide python2-%{modname}}

%description -n python2-%{modname}
A small Python 2 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%package -n python3-%{modname}
Summary:       Python 3 module for determining platform-specific directoriess
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python2_sitelib}/%{modname}.py
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{modname}.py

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python2_sitelib}/%{modname}.*
%{python2_sitelib}/%{modname}-%{version}-py%python2_version.egg-info/

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.cpython-%python3_version_nodots.py*
%{python3_sitelib}/%{modname}-%{version}-py%python3_version.egg-info/

%changelog
* Wed Aug 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-4
- Update to new packaging guidelines

* Sun Aug 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-3
- Use modern python rpm macros

* Mon Jul 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-2
- Include CHANGES.rst in doc
- use python2-devel in BR instead of python-devel
- run tests

* Fri May 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package

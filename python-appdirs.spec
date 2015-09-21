%global modname appdirs

%if 0%{?fedora}
%global with_python3 1
%endif

Name:          python-%{modname}
Version:       1.4.0
Release:       4%{?dist}
Summary:       Python module for determining platform-specific directories

License:       MIT
URL:           http://github.com/ActiveState/appdirs
Source0:       https://pypi.python.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz

BuildRequires: python2-devel python-setuptools
%if 0%{?with_python3}
BuildRequires: python3-devel python3-setuptools
%endif
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

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:       Python 3 module for determining platform-specific directoriess
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".
%endif

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python2_sitelib}/%{modname}.py
%if 0%{?with_python3}
%py3_install
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{modname}.py
%endif


%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{modname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python2_sitelib}/%{modname}.*
%{python2_sitelib}/%{modname}-%{version}-py%python2_version.egg-info/

%if 0%{?with_python3}
%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.cpython-%python3_version_nodots.py*
%{python3_sitelib}/%{modname}-%{version}-py%python3_version.egg-info/
%endif

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

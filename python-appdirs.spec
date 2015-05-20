# Created by pyp2rpm-1.1.2
%global pypi_name appdirs

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir"

License:        MIT
URL:            http://github.com/ActiveState/appdirs
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools >= 0.8

Provides:       python-appdirs

%description
Appdirs is a small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test

%files
%doc README.rst LICENSE.txt

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{upstream_version}-py?.?.egg-info

%changelog

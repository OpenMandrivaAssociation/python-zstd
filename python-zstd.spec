%global pypi_name zstd

Name:           python-%{pypi_name}
Version:        1.5.6.1
Release:        1
Group:          Development/Python
Summary:        Zstd Bindings for Python
License:        BSD
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libzstd)

%description
Simple Python bindings for the Zstd compression library.

%files
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}.dist-info

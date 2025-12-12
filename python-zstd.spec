%global pypi_name zstd

Name:           python-%{pypi_name}
Version:        1.5.7.2
Release:        1
Group:          Development/Python
Summary:        Zstd Bindings for Python
License:        BSD
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python%{pyver}dist(setuptools)

%description
Simple Python bindings for the Zstd compression library.

%files
%{python_sitearch}/%{pypi_name}.cpython*
%{python_sitearch}/%{pypi_name}-%{version}-py*.egg-info

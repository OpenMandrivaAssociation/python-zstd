%global module zstd

Name:           python-zstd
Version:        1.5.7.3
Release:        2
Group:          Development/Python
Summary:        Zstd Bindings for Python
License:        BSD-2-Clause
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        https://files.pythonhosted.org/packages/source/z/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python%{pyver}dist(setuptools)

%description
Simple Python bindings for the Zstd compression library.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build -p
export LDFLAGS="%{optflags} -lpython%{pyver}"

%files
%license LICENSE
%{python_sitearch}/%{module}.cpython*.so
%{python_sitearch}/%{module}-%{version}-py%{pyver}.egg-info

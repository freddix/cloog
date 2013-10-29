Summary:	Library that generates loops for scanning polyhedra
Name:		cloog
Version:	0.18.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.bastoul.net/cloog/pages/download/%{name}-%{version}.tar.gz
# Source0-md5:	e34fca0540d840e5d0f6427e98c92252
URL:		http://www.cloog.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-c++-devel
BuildRequires:	isl-devel
BuildRequires:	libtool
Requires(post):	/usr/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLooG is a software which generates loops for scanning Z-polyhedra.
That is, CLooG finds the code or pseudo-code where each integral point
of one or more parametrized polyhedron or parametrized polyhedra union
is reached. CLooG is designed to avoid control overhead and to produce
a very efficient code.

%package devel
Summary:	Header files for cloog library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-c++-devel
Requires:	isl-devel

%description devel
This is the package containing the header files for cloog library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--with-isl=system
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/cloog
%attr(755,root,root) %ghost %{_libdir}/libcloog-isl.so.4
%attr(755,root,root) %{_libdir}/libcloog-isl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcloog-isl.so
%{_includedir}/cloog
%{_pkgconfigdir}/cloog-isl.pc

%define major 0
%define libname %mklibname drizzle %{major}
%define develname %mklibname drizzle -d

Summary:	Drizzle Client & Protocol Library
Name:		libdrizzle
Version:	0.5
Release:	%mkrel 1
License:	BSD
Group:		System/Libraries
URL:		https://launchpad.net/libdrizzle
Source0:	http://launchpad.net/libdrizzle/%{version}/%{version}/+download/libdrizzle-%{version}.tar.gz
BuildRequires:	sqlite3-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the the client and protocol library for the Drizzle project. The
server, drizzled, will use this as for the protocol library, as well as the
client utilities and any new projects that require low-level protocol
communication (like proxies). Other language interfaces (PHP extensions, SWIG,
...) should be built off of this interface.

%package -n	%{libname}
Summary:	Drizzle Client & Protocol Library
Group:		System/Libraries

%description -n	%{libname}
This is the the client and protocol library for the Drizzle project. The
server, drizzled, will use this as for the protocol library, as well as the
client utilities and any new projects that require low-level protocol
communication (like proxies). Other language interfaces (PHP extensions, SWIG,
...) should be built off of this interface.

%package -n	%{develname}
Summary:	Drizzle Client & Protocol Library - Header files
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{develname}
Development files for the Drizzle Client & Protocol Library.

%prep

%setup -q

%build
%configure2_5x

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post   -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS PROTOCOL README
%dir %{_includedir}/libdrizzle
%{_includedir}/libdrizzle/*.h
%{_libdir}/lib*.*a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libdrizzle.pc


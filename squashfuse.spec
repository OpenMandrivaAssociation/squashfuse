%define major		0
%define libname		%mklibname %{name} %{major}
%define libname_ll	%mklibname %{name}_ll %{major}
%define develname	%mklibname %{name} -d

Name:		squashfuse
Version:	0.4.0
Release:	1
Summary:	FUSE filesystem to mount squashfs archives
License:	BSD
Group:		File tools
URL:		https://github.com/vasi/squashfuse
Source0:	https://github.com/vasi/squashfuse/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(fuse3)
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(zlib)

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.

#------------------------------------------------

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
Libraries for running %{name} applications.

#------------------------------------------------

%package -n	%{libname_ll}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname_ll}
Libraries for running %{name} applications.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libname_ll} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1

%build
./autogen.sh
%configure --disable-static \
           --disable-demo
%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name '*.la' -delete

%files
%doc README TODO
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%doc README
%license LICENSE
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{libname_ll}
%doc README
%license LICENSE
%{_libdir}/lib%{name}_ll.so.%{major}{,.*}

%files -n %{develname}
%doc CONFIGURATION PLATFORMS README
%license LICENSE
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_ll.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_ll.pc

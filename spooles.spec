Summary:	Library for solving linear systems of equations
Summary(es):	Biblioteca para resolver sistemas lineares de ecuaciones
Summary(pl):	Biblioteka pozwalaj�ca rozwi�zywa� liniowe uk�ady r�wna�
Name:		spooles
Version:	2.2
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.netlib.org/linalg/spooles/%{name}.%{version}.tgz
# Source0-md5:	5789ca60d1ae565a4eaef6d03ca837af
Source1:	http://www.netlib.org/linalg/spooles/ReferenceManual.ps.gz
# Source1-md5:	9e5e32828f59c4cf066fdb34218705e7
Patch0:		%{name}-automake_support.patch
URL:		http://www.netlib.org/linalg/spooles/spooles.2.2.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPOOLES is a library for solving sparse real and complex linear
systems of equations.

%description -l es
SPOOLES es una biblioteca para resolver sistemas lineares dispersos de
ecuaciones reales y complejas.

%description -l pl
SPOOLES jest bibliotek� pozwalaj�c� rozwi�zywa� rzeczywiste i
zespolone rozrzedzone uk�ady r�wna� liniowych.

%package devel
Summary:	SPOOLES development files
Summary(es):	Ficheros de desarrollo de SPOOLES
Summary(pl):	Pliki programistyczne SPOOLES
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
SPOOLES development files.

%description devel -l es
Ficheros de desarrollo de SPOOLES.

%description devel -l pl
Pliki programistyczne SPOOLES.

%package static
Summary:	Static SPOOLES library
Summary(es):	Biblioteca SPOOLES est�tica
Summary(pl):	Statyczna biblioteka SPOOLES
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPOOLES library.

%description static -l es
Biblioteca SPOOLES est�tica.

%description static -l pl
Statyczna biblioteka SPOOLES.

%package doc-ps
Summary:	PostScript documentation for SPOOLES
Summary(es):	Documentaci�n para SPOOLES en PostScript
Summary(pl):	Dokumentacja dla SPOOLES w formacie PostScript
Group:		Development/Libraries

%description doc-ps
PostScript documentation for SPOOLES.

%description doc-ps -l es
Documentaci�n para SPOOLES en el formato PostScript.

%description doc-ps -l pl
Dokumentacja dla SPOOLES w formacie PostScript.

%prep
%setup -q -c 
%patch0 -p1

%build
find . -name makefile -exec mv {} {}.orig \;
mkdir docs
cp %{SOURCE1} docs/ReferenceManual.ps.gz
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc spooles.2.2.html
%attr(755,root,root) %{_libdir}/libspooles.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspooles.so
%{_libdir}/libspooles.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libspooles.a

%files doc-ps
%defattr(644,root,root,755)
%doc docs/*.ps.gz

Summary:	A library for parsing CMML files
Summary(pl):	Biblioteka do analizy plików CMML
Name:		libcmml
Version:	0.9.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://annodex.net/software/libcmml/download/%{name}-%{version}.tar.gz
# Source0-md5:	00ece8c9a0363b37957ce670bcf270d3
URL:		http://annodex.net/software/libcmml/index.html
BuildRequires:	expat-devel >= 1.95
Requires:	expat >= 1.95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcmml is a library which enables the handling of documents
written in CMML (Continuous Media Markup Language) for the
Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the
Continuous Media Markup Language (CMML), and returns C structures
containing this information in a format which can be used by an
Annodexer for creating ANNODEX(tm) format documents (ANX).

%description -l pl
libcmml to biblioteka umo¿liwiaj±ca obs³ugê dokumentów napisanych w
formacie CMML (Continuous Media Markup Language - jêzyku oznaczeñ dla
mediów ci±g³ych) dla CMWeb (Continuos Media Web - sieci dla mediów
ci±g³ych).

Udostêpnia bardzo proste API do odczytu plików ze znacznikami w
formacie CMML, zwraca struktury C zawieraj±ce informacje w formacie,
który mo¿e byæ u¿yty w Annodexerze do tworzenia dokumentów w formacie
ANNODEX(tm) (ANX).

%package devel
Summary:	Header files for libcmml library
Summary(pl):	Pliki nag³ówkowe biblioteki libcmml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1.95

%description devel
Header files for libcmml library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libcmml.

%package static
Summary:	Static libcmml library
Summary(pl):	Statyczna biblioteka libcmml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcmml library.

%description static -l pl
Statyczna biblioteka libcmml.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libcmml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/cmml*
%attr(755,root,root) %{_libdir}/libcmml.so.*.*.*
%{_mandir}/man1/cmml*.1*
%{_mandir}/man6/cmml-fortune.6*

%files devel
%defattr(644,root,root,755)
%doc doc/libcmml/html/*
%attr(755,root,root) %{_libdir}/libcmml.so
%{_libdir}/libcmml.la
%{_includedir}/cmml.h
%{_pkgconfigdir}/cmml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcmml.a

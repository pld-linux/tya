Summary:	TYA is a 100%% unofficial JIT-compiler for Java.
Name:		tya
Version:	1.5
Release:	2
License:	GPL
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	ftp://gonzalez.cyberus.ca/pub/Linux/java/%{name}15.tgz
Source1:	%{name}.csh
Source2:	%{name}.sh
Patch0:		%{name}-buildroot.patch
URL:		ftp://gonzalez.cyberus.ca/pub/Linux/java/
BuildRequires:	autoconf
Requires:	jdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TYA is a "100%% unofficial" Just-In-Time-compiler for Java. When Java
is invoked with the option "-Djava.compiler=tya" it will automatically
detect TYA and compile any method bodies in Java byte code to Pentium
instructions just before they are being executed for the first time.
This means that Java programs will run faster than before, especially
after some time of execution, when most methods have already been
called before.

%prep
%setup -q -n tya%{version}
%patch0 -p1 

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/profile.d

%{__make} install root=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libtya.so $RPM_BUILD_ROOT%{_libdir}/libtya.so.%{version}
ln -s libtya.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtya.so

# install profile scripts
install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d

gzip -9nf ChangeLog README FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *gz demo
%{_libdir}/libtya.so
%{_libdir}/libtya.so.%{version}
%attr(0755,root,root) /etc/profile.d/tya.*sh

Summary:	TYA is a 100%% unofficial JIT-compiler for Java.
Name:		tya
Version:	1.5
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	jdk
Source0:	ftp://gonzalez.cyberus.ca/pub/Linux/java/%{name}15.tgz
Source1:	%{name}.csh
Source2:	%{name}.sh
Patch0:		%{name}-1.3v2-buildroot.patch
URL:		ftp://gonzalez.cyberus.ca/pub/Linux/java/
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
./configure --prefix=%{_prefix}/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install root=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{_libdir}/libtya.so $RPM_BUILD_ROOT%{_libdir}/libtya.so.%{version}
ln -s libtya.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtya.so

# install profile scripts
install -d $RPM_BUILD_ROOT/etc/profile.d
install -m755 $RPM_SOURCE_DIR/tya.*sh \
	$RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING.GPL COPYRIGHT ChangeLog README FAQ
%doc demo
/usr/lib/libtya.so
/usr/lib/libtya.so.%{version}
%attr(0755,root,root) /etc/profile.d/tya.*sh

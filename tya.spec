%define version 1.5
%define fnversion 15
Summary: TYA is a 100%% unofficial JIT-compiler for Java.
Name: tya
Version: %{version}
Release: 2
Copyright: GPL
Group: Libraries
Requires: jdk
Source: ftp://gonzalez.cyberus.ca/pub/Linux/java/tya%{fnversion}.tgz
Source1: tya.csh
Source2: tya.sh
Patch0: tya-1.3v2-buildroot.patch
BuildRoot: /var/tmp/tya-root
Url: ftp://gonzalez.cyberus.ca/pub/Linux/java/

%description
TYA is a "100%% unofficial" Just-In-Time-compiler for Java.
When Java is invoked with the option "-Djava.compiler=tya" it will
automatically detect TYA and compile any method bodies in Java byte code to
Pentium instructions just before they are being executed for the first time.
This means that Java programs will run faster than before, especially after
some time of execution, when most methods have already been called before.

%prep
%setup -n tya%{version}
%patch0 -p1 

%build
./configure --prefix=/usr/
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install root=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib/libtya.so $RPM_BUILD_ROOT/usr/lib/libtya.so.%{version}
ln -s libtya.so.%{version} $RPM_BUILD_ROOT/usr/lib/libtya.so

# install profile scripts
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -m755 $RPM_SOURCE_DIR/tya.*sh \
	$RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING.GPL COPYRIGHT ChangeLog README FAQ
%doc demo
/usr/lib/libtya.so
/usr/lib/libtya.so.%{version}
%attr(0755,root,root) /etc/profile.d/tya.*sh

%changelog
* Wed Sep 29 1999 Peter Hanecak <hanecak@megaloman.sk>
- fixed and slightly improved spec (provides are fixed now)

* Tue Sep 28 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated to 1.5

* Thu Aug 26 1999 Peter Hanecak <hanecak@megaloman.sk>
- patch from Albrecht Kleine <java@ak.sax.de>
  (division by 2 optimisation bug fix)

* Wed Jul 28 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated to 1.4
- changed URL because the previous one contains very old information

* Fri Jun 18 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated to 1.3v2
- URL added

* Sat Feb  6 1999 Peter Hanecak <hanecak@megaloman.sk>
- included /etc/profile.d/tya.csh and /etc/profile.d/tya.sh
- using %defattr so ordinary users should be able to build
- BuildRoot used
- %clean macro used

* Tue Feb  2 1999 Peter Hanecak <hanecak@megaloman.sk>
- ./configure moved from %prep to %build
- include patch (for using with Blackdown's jdk-1.1.6.5-2glibc packed to RPM
  by C. Scott Ananian <cananian@alumni.princeton.edu>
- build for glibc 2.1

* Sat Dec 12 1998 Levente Farkas <lfarkas@ohsh.u-szeged.hu>
- update to 1.2

Summary:	TYA is a 100%% unofficial JIT-compiler for Java.
Name:		tya
Version:	1.5
Release:	2
License:	GPL
Group:		Libraries
Requires:	jdk
Source:		ftp://gonzalez.cyberus.ca/pub/Linux/java/%{name}15.tgz
Source1:	tya.csh
Source2:	tya.sh
Patch0:		tya-1.3v2-buildroot.patch
URL:		ftp://gonzalez.cyberus.ca/pub/Linux/java/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TYA is a "100%% unofficial" Just-In-Time-compiler for Java. When Java is
invoked with the option "-Djava.compiler=tya" it will automatically detect
TYA and compile any method bodies in Java byte code to Pentium instructions
just before they are being executed for the first time. This means that Java
programs will run faster than before, especially after some time of
execution, when most methods have already been called before.

%prep
%setup -q -n tya%{version}
%patch0 -p1 

%build
./configure --prefix=/usr/
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install root=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib/libtya.so $RPM_BUILD_ROOT/usr/lib/libtya.so.%{version}
ln -s libtya.so.%{version} $RPM_BUILD_ROOT/usr/lib/libtya.so

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
%defattr(644,root,root,755)
- BuildRoot used
- %clean macro used

* Tue Feb  2 1999 Peter Hanecak <hanecak@megaloman.sk>
- ./configure moved from %prep to %build
- include patch (for using with Blackdown's jdk-1.1.6.5-2glibc packed to RPM
  by C. Scott Ananian <cananian@alumni.princeton.edu>
- build for glibc 2.1

* Sat Dec 12 1998 Levente Farkas <lfarkas@ohsh.u-szeged.hu>
- update to 1.2

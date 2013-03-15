%define		_class		I18N
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	5
Summary:	Internationalization package
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/I18N/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package supports you to localize your applications. Currently
multiple ways of supporting translation are implemented and methods to
determine the current users (browser-)language.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2012.0
+ Revision: 742015
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3
+ Revision: 679366
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 613688
- the mass rebuild of 2010.1 packages

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 509121
- new version

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6-13mdv2010.1
+ Revision: 478025
- fix patch

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6-12mdv2010.1
+ Revision: 473534
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.8.6-11mdv2010.0
+ Revision: 441192
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-10mdv2009.1
+ Revision: 322133
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-9mdv2009.0
+ Revision: 236892
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.8.6-8mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-8mdv2007.0
+ Revision: 81894
- Import php-pear-I18N

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Thu Aug 04 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-5mdk
- fix the package.xml file

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6-1mdk
- initial Mandriva package (PLD import)


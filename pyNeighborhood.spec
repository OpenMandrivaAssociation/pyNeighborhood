%define prel pre3

Summary:	S GTK+ 2 rewrite of a well-known LinNeighborhood tool
Name:		pyNeighborhood
Version:	0.5.0
Release:	%mkrel -c %prel 6
License:	GPLv3
Group:		Networking/File transfer
Url:		http://pyneighborhood.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyneighborhood/%{name}-%{version}-%{prel}.tar.bz2
Buildrequires:	python
Requires:	samba-client
Requires:	pygtk2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
pyNeighborhood is a the GUI frontend for samba tools, such as 
smbclient, smbmount etc.

%prep
%setup -q -c

%build
python setup.py build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

rm -fr %buildroot%_datadir/doc/pyneighborhood

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO Changelog
%{_bindir}/*
%{py_sitedir}/pyneighborhood
%{py_sitedir}/*.egg*
%{_datadir}/applications/*.desktop
%{_datadir}/pyneighborhood


%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.5.0-0.pre3.6mdv2011.0
+ Revision: 593081
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.0-0.pre3.5mdv2010.0
+ Revision: 441991
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.5.0-0.pre3.4mdv2009.1
+ Revision: 325854
- rebuild

* Fri Aug 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.pre3.3mdv2009.0
+ Revision: 275143
- run scriplets only for mdv older than 200900
- spec file clean

* Thu Aug 21 2008 Funda Wang <fwang@mandriva.org> 0.5.0-0.pre3.2mdv2009.0
+ Revision: 274709
- fix file list
- should be noarch

* Thu Aug 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.pre3.1mdv2009.0
+ Revision: 274596
- add requires on samba-client and pygtk2.0
- add source and spec file
- Created package structure for pyNeighborhood.


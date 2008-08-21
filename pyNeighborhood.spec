%define prel pre3

Summary:	S GTK+ 2 rewrite of a well-known LinNeighborhood tool
Name:		pyNeighborhood
Version:	0.5.0
Release:	%mkrel -c %prel 2
License:	GPLv3
Group:		Networking/File transfer
Url:		http://pyneighborhood.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyneighborhood/%{name}-%{version}-%{prel}.tar.bz2
%py_requires -d
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

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO Changelog
%{_bindir}/*
%{py_sitedir}/pyneighborhood
%{py_sitedir}/*.egg*
%{_datadir}/applications/*.desktop
%{_datadir}/pyneighborhood
%exclude %{_docdir}/pyneighborhood

%{?!commit: %global commit workingcopy}

Name: ndprbrd
Version: 0.0.1
Release: 1.%{commit}
Summary: NDP Proxy Daemon

Group: System Environment/Daemons
License: GPL-3
URL: https://github.com/google/ndprbrd
Source0: https://github.com/google/%{name}/archive/master.tar.gz
Source1: ndprbrd.service

Patch0: ndprbrd-sbin.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-units
BuildRequires: cmake

%description
'ndprbrd', or NDP Proxy Router Bridge Daemon, is a daemon that proxies
NDP (Neighbor Discovery Protocol) messages between interfaces. It is
based on the ndppd project.

%prep
%setup -q -n %{name}-master

%patch0 -p1

%build
%cmake .
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/ndprbrd
%make_install PREFIX=/usr
install -Dt ${RPM_BUILD_ROOT}%{_unitdir} -m 644 %{SOURCE1}


%postun
%systemd_postun_with_restart ndprbrd.service

%post
%systemd_post ndprbrd.service

%preun
%systemd_preun ndprbrd.service

%files
%{_unitdir}/ndprbrd.service
/usr/sbin/ndprbrd
%dir %{_localstatedir}/run/ndprbrd/

%changelog
* Wed Nov 1 2017 Kenny Root <kenny@the-b.org> - 0.0.1-1
- initial package                                                                                          


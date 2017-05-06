%{?systemd_requires}
# Upstream package name naturally contains an underscore
Name:           autossh-service
Version:        1
Release:        1
Summary:        Unit file for an autossh systemd service

Group:          System Environment/Base
License:        MIT
Vendor:         SMARTRAC Technology Fletcher, Inc.

Packager:       Robert Van Voorhees <rcvanvo@gmail.com>
Requires:       autossh
BuildRequires:  systemd

URL:            https://github.com/smartractechnology
Source0:        autossh-service.service
Source1:        autossh-service.conf
BuildArch:      noarch

%define         _serviceUsername autossh

%description
Unit file for an autossh systemd service

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_unitdir}

install -p -m 644 %{SOURCE0} %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}

%files
%config(noreplace) %{_sysconfdir}/autossh-service.conf
%attr(0644, root, root) %{_unitdir}/autossh-service.service

%pre
getent group %{_serviceUsername} >/dev/null || groupadd -r %{_serviceUsername}
getent passwd %{_serviceUsername} >/dev/null || \
    useradd -r -g %{_serviceUsername} -d /var/lib/%{name} -s /sbin/nologin \
    -c "autossh service account" %{_serviceUsername}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Sat May 6 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1-1
- Initial RPM release

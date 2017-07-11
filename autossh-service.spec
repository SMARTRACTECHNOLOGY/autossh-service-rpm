%{?systemd_requires}
# Upstream package name naturally contains an underscore
Name:           autossh-service
Version:        4
Release:        2
Summary:        Unit file for an autossh systemd service

Group:          System Environment/Base
License:        MIT
Vendor:         SMARTRAC Technology Fletcher, Inc.

Packager:       Robert Van Voorhees <rcvanvo@gmail.com>
Requires:       autossh
BuildRequires:  systemd

URL:            https://github.com/smartractechnology
Source0:        autossh-service@.service
Source1:        autossh-service.conf
Source10:       autossh-service
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
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_unitdir}

install -p -m 644 %{SOURCE10} %{buildroot}/%{_sbindir}
install -p -m 644 %{SOURCE0} %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}

%files
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0644, root, root) %{_unitdir}/%{name}@.service
%attr(0755, root, root) %{_sbindir}/%{name}

%post
%systemd_post %{name}@.service

%preun
%systemd_preun %{name}@.service

%postun
%systemd_postun_with_restart %{name}@.service

%changelog
* Tue Jul 11 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 4-2
- Allow other users to execute the script.

* Tue Jul 11 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 4-1
- Change to external script.

* Tue Jul 11 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 3-1
- Move more options into conf file.

* Tue Jul 11 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 2-2
- Fix upgrade scripts, add parameter for id_rsa

* Tue Jul 11 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 2-1
- Remove user information and make the service parameterized

* Sat May 6 2017 Robert Van Voorhees <rcvanvo@gmail.com> - 1-1
- Initial RPM release

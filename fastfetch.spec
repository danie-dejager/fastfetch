Name:           fastfetch
Version:        2.37.0
Release:        1%{?dist}
Summary:        Like neofetch, but much faster because written in c
 
License:        MIT
URL:            https://github.com/fastfetch-cli/fastfetch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pciutils-devel
BuildRequires:  dconf-devel
BuildRequires:  dbus-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires:  glib2-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  yyjson-devel > 0.9.0
BuildRequires:  elfutils-libelf-devel
BuildRequires:  rpm-devel
BuildRequires:  upx

Recommends:     hwdata
Recommends:     dconf
Recommends:     sqlite
Recommends:     zlib
Recommends:     glib2
Recommends:     ddcutil

%define debug_package %{nil}


%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.


%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description bash-completion
%{summary}

%package fish-completion
Summary: Fish completion files for %{name}
Requires: fish
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description fish-completion
%{summary}

%package zsh-completion
Summary: ZSH completion files for %{name}
Requires: zsh
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description zsh-completion
%{summary}


%prep
%autosetup -p1

 
%build
%cmake -D BUILD_TESTS=ON -D BUILD_FLASHFETCH=OFF
%cmake_build


%check
%ctest


%install
%cmake_install
# Compress the binary using upx after installation
upx %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/fastfetch.1*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Wed Feb 19 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.37.0-1
* Tue Feb 11 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.36.1-1
* Mon Feb 10 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.36.0-1
* Sun Jan 26 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.35.0-1
* Tue Jan 21 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.34.1-2
* Tue Jan 14 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.34.1-1
* Fri Jan 10 2025 - Danie de Jager <danie.dejager@gmail.com> - 2.34.0-1
* Thu Dec 26 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.33.0-1
* Thu Dec 5 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.31.0-1
* Mon Nov 18 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.30.1-1
- A hotfix release that fixes a build failure when running cmake outside of build directory.
* Mon Nov 18 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.30.0-1
* Mon Nov 1 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.29.0-1
* Thu Oct 24 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.28.0-1
* Mon Sep 30 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.26.1-1
* Tue Sep 11 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.25.0-1
* Tue Sep 11 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.24.0-1
* Tue Sep 3 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.23.0-1
* Tue Aug 27 2024 - Danie de Jager <danie.dejager@gmail.com> - 2.22.0-1
* Wed Aug 14 2024 Danie de Jager <danie.dejager@gmail.com> - 2.21.2-1
* Sun Aug 11 2024 Danie de Jager <danie.dejager@gmail.com> - 2.21.1-1
* Tue Aug 6 2024 Danie de Jager <danie.dejager@gmail.com> - 2.21.0-1
* Fri Jul 26 2024 Danie de Jager <danie.dejager@gmail.com> - 2.20.0-1
* Mon Jul 22 2024 Danie de Jager <danie.dejager@gmail.com> - 2.19.0-1
* Mon Jul 15 2024 Danie de Jager <danie.dejager@gmail.com> - 2.18.1-1
* Thu Jul 4 2024 Danie de Jager <danie.dejager@gmail.com> - 2.17.2-1
* Sat Jun 29 2024 Danie de Jager <danie.dejager@gmail.com> - 2.17.1-1
* Fri Jun 7 2024 Danie de Jager <danie.dejager@gmail.com> - 2.15.0-1
* Fri May 31 2024 Danie de Jager <danie.dejager@gmail.com> - 2.14.0-1
* Thu May 23 2024 Danie de Jager <danie.dejager@gmail.com> - 2.13.2-1
* Tue May 21 2024 Danie de Jager <danie.dejager@gmail.com> - 2.13.1-1
* Mon May 20 2024 Danie de Jager <danie.dejager@gmail.com> - 2.13.0-1
* Tue May 14 2024 Danie de Jager <danie.dejager@gmail.com> - 2.12.0-1
* Mon May 6 2024 Danie de Jager <danie.dejager@gmail.com> - 2.11.4-1
* Mon May 6 2024 Danie de Jager <danie.dejager@gmail.com> - 2.11.3-1
* Fri May 3 2024 Danie de Jager <danie.dejager@gmail.com> - 2.11.2-1
* Thu May 2 2024 Danie de Jager <danie.dejager@gmail.com> - 2.11.1-1
* Thu May 2 2024 Danie de Jager <danie.dejager@gmail.com> - 2.11.0-1
* Tue Apr 23 2024 Danie de Jager <danie.dejager@gmail.com> - 2.10.2-1
* Thu Apr 16 2024 Danie de Jager <danie.dejager@gmail.com> - 2.9.2-1
- add yyjson-devel build depedency.
* Thu Apr 4 2024 Danie de Jager <danie.dejager@gmail.com> - 2.9.0-1
- dropped dependency libpci for hwdata.
* Mon Mar 25 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.10-1
* Fri Mar 15 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.9-1
* Fri Mar 8 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.8-1
* Tue Mar 5 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.7-1
* Tue Feb 27 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.6-1
* Sun Feb 25 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.5-1
* Tue Feb 13 2024 Danie de Jager <danie.dejager@gmail.com> - 2.8.3-1
* Fri Feb 2 2024 Danie de Jager <danie.dejager@gmail.com> - 2.7.1-2
- use UPX to compress binary.
* Fri Feb 2 2024 Danie de Jager <danie.dejager@gmail.com> - 2.7.1-1
- Initial build based on Fedora Spec.
- Removed dependencies

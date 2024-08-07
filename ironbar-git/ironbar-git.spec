# Generated by rust2rpm 26
%bcond_without check

%global pkgname ironbar

%global commit 58190ab079d00dd53babb72346f1da6e1cc9ac72
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.16.0~pre

Name:           %{pkgname}-git
Version:        %{ver}.git.%{shortcommit}
Release:        %autorelease
Summary:        Customisable GTK Layer Shell wlroots/sway bar

# FIXME: paste output of %%cargo_license_summary here
License:        MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/jakestanger/ironbar
Source:         %{url}/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  luajit-devel
BuildRequires:  lua-lgi

Conflicts:      ironbar
Provides:       ironbar

Enhances:       hyprland

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{pkgname}-%{commit} -p1
cargo vendor
%cargo_prep -v vendor

%build
cargo build --locked --release
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm755 target/release/%{pkgname} %{buildroot}%{_bindir}/%{pkgname}

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/%{pkgname}

%changelog
%autochangelog

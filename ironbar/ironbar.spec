# Generated by rust2rpm 26
%bcond_without check

Name:           ironbar
Version:        0.15.1
Release:        %autorelease
Summary:        Customisable GTK Layer Shell wlroots/sway bar

# FIXME: paste output of %%cargo_license_summary here
License:        MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/jakestanger/ironbar
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  luajit-devel
BuildRequires:  lua-lgi

Conflicts:      ironbar-git
Provides:       ironbar

Enhances:       hyprland

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
cargo build --locked --release
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

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
%{_bindir}/%{name}

%changelog
%autochangelog

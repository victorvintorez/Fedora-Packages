# Generated by rust2rpm 26
%bcond_without check

Name:           yazi
Version:        0.2.5
Release:        %autorelease
Summary:        Yazi File Manager

# FIXME: paste output of %%cargo_license_summary here
License:        MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/sxyazi/yazi
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  make
Buildrequires:  gcc

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
cargo install -j2 avoid-dev-deps --no-track --path yazi-fm
cargo install -j2 avoid-dev-deps --no-track --path yazi-cli

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/ya
%{_bindir}/yazi

%changelog
%autochangelog

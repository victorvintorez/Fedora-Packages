# Generated by rust2rpm 26
%bcond_without check

%global upstreamver 3.0.0-beta

Name:           wallust
Version:        3.0.0~beta
Release:        %autorelease
Summary:        Generate a 16 color scheme based on an image

# FIXME: paste output of %%cargo_license_summary here
License:        MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://codeberg.org/explosion-mental/wallust
Source:         %{url}/archive/%{upstreamver}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc

Recommends:     imagemagick

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name} -p1
cargo vendor
%cargo_prep -v vendor

%build
cargo build --locked --release
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm644 completions/_%{name} %{buildroot}%{zsh_completions_dir}/_%{name}
install -Dpm644 completions/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}.bash
install -Dpm644 completions/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm644 man/%{name}*.1 -t %{buildroot}%{_mandir}/man1
install -Dpm644 man/%{name}.5 %{buildroot}%{_mandir}/man5

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/wallust
%{_mandir}/man1/%{name}*.1.*
%{_mandir}/man5/%{name}.5.*
%{bash_completions_dir}/%{name}.bash
%{zsh_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish

%changelog
%autochangelog

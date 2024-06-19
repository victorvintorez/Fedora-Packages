# Generated by go2rpm 1.11.1
%bcond_without check

# https://github.com/abenz1267/walker
%global goipath         github.com/abenz1267/walker
Version:                0.0.72

%gometa -L -f

%global common_description %{expand:
Wayland-native application runner.}

%global golicenses      LICENSE
%global godocs          README.md version.txt

Name:           walker
Release:        %autorelease
Summary:        Wayland-native application runner

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  go-vendor-tools
BuildRequires:  git

Requires:       gtk4-layer-shell

Recommends:     wl-clipboard

%description %{common_description}

%prep
%goprep -k
go mod vendor
%autopatch -p1

%build
export GOFLAGS=-mod=vendor
%gobuild -o %{gobuilddir}/bin/walker %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%license vendor/modules.txt
%doc README.md version.txt
%{_bindir}/*

%changelog
%autochangelog

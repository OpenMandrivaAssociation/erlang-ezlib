%global srcname ezlib

%define  _disable_ld_no_undefined 1

Name:       erlang-%{srcname}
Version:    1.0.1
Release:    %mkrel 5

Group:      Development/Erlang

License:    ASL 2.0
Summary:    Native zlib driver for Erlang
URL:        https://github.com/processone/ezlib/
Source0:    https://github.com/processone/ezlib/archive/%{version}.tar.gz

Provides:   erlang-p1_zlib = %{version}-%{release}
Obsoletes:  erlang-p1_zlib <= 1.0.1-2

BuildRequires: erlang-rebar
BuildRequires: zlib-devel

%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}


%description
A native zlib driver for Erlang / Elixir, used by ejabberd.


%prep
%autosetup -n ezlib-%{version}


%build
%configure --enable-nif
# There is a pull request upstream for this -lz https://github.com/processone/ezlib/pull/1
LDFLAGS="$LDFLAGS -lz" %{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/ezlib_drv.so \
    $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.1-5.mga6
+ Revision: 1068020
- imported package erlang-ezlib


Name: x11-font-bh-type1
Version: 1.0.3
Release: 3
Summary: Xorg X11 font bh-type1
Group: Development/X11
URL: https://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-bh-type1-%{version}.tar.bz2
# We may not modify the software!
License: Bigelow & Holmes Font License
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bh-type1

%prep
%setup -q -n font-bh-type1-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/Type1

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/Type1/fonts.dir
rm -f %{buildroot}%_datadir/fonts/Type1/fonts.scale

%post
mkfontscale %_datadir/fonts/Type1
mkfontdir %_datadir/fonts/Type1

%postun
mkfontscale %_datadir/fonts/Type1
mkfontdir %_datadir/fonts/Type1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/Type1/l04*

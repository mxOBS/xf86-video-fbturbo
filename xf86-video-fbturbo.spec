#
# spec file for package xf86-video-fbturbo
#
# Copyright (c) 2015 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name: xf86-video-fbturbo
Version: 1
Release: 1
License: MIT
Group: System/X11/Servers/XF86_4
Summary: Vivante X.org driver
Url: https://github.com/ssvb/xf86-video-fbturbo
Source: %{name}-%{version}.tar.xz
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xorg-macros) >= 1.8
BuildRequires: xorg-x11-server-sdk

Conflicts: xf86-video-fbdev
Obsoletes: xf86-video-fbdev
Provides: xf86-video-fbdev

%description
Provides an X.org driver for Vivante GPUs using their galcore kernel interface.

%prep
%setup -q

%build
autoreconf -fi
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
rm -fv %{buildroot}/%{_libdir}/xorg/modules/drivers/fbturbo_drv.la
mkdir -p %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d
cat > %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d/20-fbturbo.conf << EOF
Section "Device"
	Identifier	"FBTURBO fbdev"
	Driver		"fbturbo"
	Option		"fbdev" "/dev/fb0"

	Option		"SwapbuffersWait" "true"
EndSection
EOF

%files
%defattr(-,root,root)
%config %{_sysconfdir}/X11/xorg.conf.d/20-fbturbo.conf
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/fbturbo_drv.so
%{_mandir}/*/*.gz

%changelog

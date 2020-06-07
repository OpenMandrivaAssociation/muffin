%define major	0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	A small window manager for Cinnamon Desktop
Name:		muffin
Version:	4.6.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://github.com/linuxmint/Cinnamon/tags
Source0:	https://github.com/linuxmint/muffin/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		muffin-4.0.6-compile.patch

BuildRequires:  intltool
BuildRequires:  zenity
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:	gnome-common
BuildRequires:  gtk-doc
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(cogl-1.0)
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:	pkgconfig(dri)
BuildRequires:	egl-devel
#BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(xkeyboard-config)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	egl-devel

%description
Muffin is a small window manager, using GTK+ and Clutter to do everything.
Muffin is the clutter-based evolution of Metacity, which, as the  author 
says, is a "Boring window manager for the adult in you. Many  window managers
are like Marshmallow Froot Loops; Metacity is like Cheerios."

%package -n %{libname}
Summary:	Muffin shared libraries
Group:		System/Libraries

%description -n %{libname}
This package contains the Muffin shared libraries.

%package -n %{devname}
Summary:	Muffin development files
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
This package provides Muffin development files.

%prep
%autosetup -p1

%build
# Build with Clang:
#Invalid GType function: 'clutter_point_get_type'
#Failed to find symbol 'clutter_point_get_type'
#clutter-muffin.h:46: Warning: Clutter: symbol='SyncMethod': Unknown namespace for identifier 'SyncMethod'
# As workaround switch to GCC: https://github.com/linuxmint/muffin/issues/538
export CC=gcc
export CXX=g++
NOCONFIGURE=1 sh autogen.sh
%configure \
        --enable-startup-notification=yes \
        --disable-silent-rules \
	      --enable-compile-warnings=no \
	      --disable-Werror \
	      --disable-static \
	      --disable-scrollkeeper \
        --disable-clutter-doc \
        --disable-wayland-egl-platform \
        --disable-wayland-egl-server \
        --disable-kms-egl-platform \
        --disable-wayland \
        --disable-native-backend

%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/muffin
%{_bindir}/muffin-message
%{_bindir}/muffin-theme-viewer
%{_bindir}/muffin-window-demo
%dir %{_libdir}/muffin
%dir %{_libdir}/muffin/plugins
%{_libdir}/muffin/plugins/default.so
# -- typelib needs to be changed upstream, once this happens split the package
%{_libdir}/muffin/*.typelib
%{_libdir}/muffin/*.so
%{_datadir}/applications/muffin.desktop
%{_datadir}/muffin/
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%{_mandir}/man1/muffin-message.1*
%{_mandir}/man1/muffin-theme-viewer.1*
%{_mandir}/man1/muffin-window-demo.1*
%{_mandir}/man1/muffin.1*
%{_libexecdir}/muffin-restart-helper

%files -n %{libname}
%{_libdir}/libmuffin.so.%{major}*

%files -n %{devname}
%{_includedir}/muffin/
%{_libdir}/*.so
%{_libdir}/muffin/*.gir
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/muffin


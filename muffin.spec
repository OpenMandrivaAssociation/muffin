%define major	0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A small window manager for Cinnamon Desktop
Name:		muffin
Version:	2.6.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://github.com/linuxmint/Cinnamon/tags
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  intltool
BuildRequires:  zenity
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:	gnome-common
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libstartup-notification-1.0)

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
%setup -q

%build
sh autogen.sh
%configure2_5x \
	--enable-compile-warnings=no \
	--disable-static \
	--disable-scrollkeeper

%make

%install
%makeinstall_std
find %{buildroot}%{_libdir} -type f -name "*.la" -delete -print
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
%{_libdir}/muffin/Meta-Muffin.0.typelib
%{_datadir}/applications/muffin.desktop
%{_datadir}/muffin/
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%{_mandir}/man1/muffin-message.1*
%{_mandir}/man1/muffin-theme-viewer.1*
%{_mandir}/man1/muffin-window-demo.1*
%{_mandir}/man1/muffin.1*

%files -n %{libname}
%{_libdir}/libmuffin.so.%{major}*

%files -n %{devname}
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/Meta-Muffin.0.gir
%{_libdir}/pkgconfig/libmuffin.pc
%{_libdir}/pkgconfig/muffin-plugins.pc
%{_datadir}/gtk-doc/html/muffin


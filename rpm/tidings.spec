# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       tidings

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Bearer of tidings.
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    GPLv2
Source0:    %{name}-%{version}.tar.bz2
Source100:  tidings.yaml
Requires:   qt5-qtdeclarative-import-xmllistmodel
Requires:   sailfishsilica-qt5
Requires:   qt5-plugin-imageformat-ico
Requires:   qt5-plugin-imageformat-gif
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  desktop-file-utils

%description
Tidings is a news feed aggregator for RSS, Atom, and OPML feeds. Always be up to date with the latest news of what matters to you on your mobile device.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}/qml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/90x90/apps/%{name}.png
/usr/bin
/usr/share/tidings
/usr/share/applications
/usr/share/icons/hicolor/90x90/apps
# >> files
# << files

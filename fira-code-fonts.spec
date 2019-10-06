%global fontname fira-code
%global fontconf 61-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2
Release:        1%{?dist}
Summary:        Monospaced font with programming ligatures

License:        OFL
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/releases/download/%{version}/FiraCode_%{version}.zip
Source1:        https://raw.githubusercontent.com/cyfrost/copr-fira-code-fonts/master/fira-code-fonts-fontconfig.conf
Source2:        https://raw.githubusercontent.com/tonsky/FiraCode/master/LICENSE

BuildArch:      x86_64

BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Monospaced font with programming ligatures

%prep
%autosetup -c
cp %{SOURCE2} %{_builddir}/%{name}-%{version}

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 otf/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
%_font_pkg -f %{fontconf} *.otf

%license LICENSE

%changelog
* Sat Oct 5 2019 Cyrus Frost <cyrus.frost@hotmail.com>
 - Update to FiraCode 2
* Mon Nov 12 2018 Evan Anderson <evan@eaanderson.com>
 - Update to FiraCode 1.206
* Sun Aug 26 2018 Evan Anderson <evan@eaanderson.com>
 - Initial package

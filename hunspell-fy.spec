Name: hunspell-fy
Summary: Frisian hunspell dictionaries
Version: 2.0.0
Release: 4.1%{?dist}
Source: https://addons.mozilla.org/en-US/firefox/downloads/file/32102/frysk_wurdboek-%{version}-fx+tb+sm.xpi
Group: Applications/Text
URL: http://www.mozilla-nl.org/projecten/frysk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Frisian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-fy

%build
for i in README-fy.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i | tr -d '\r' > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/fy.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/fy_NL.aff
cp -p dictionaries/fy.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/fy_NL.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
fy_NL_aliases="fy_DE"
for lang in $fy_NL_aliases; do
        ln -s fy_NL.aff $lang.aff
        ln -s fy_NL.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README-fy.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.0-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Caolan McNamara <caolanm@redhat.com> - 2.0.0-3
- tidy up

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 29 2008 Caolan McNamara <caolanm@redhat.com> - 2.0.0-1
- initial version

Name:		bittwist
Version:	2.0
Release:	1%{?dist}
Summary:	Bit-Twist is a simple yet powerful libpcap-based Ethernet packet generator.

Group:		Applications/Internet
License:	GPL2
URL:		http://http://bittwist.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-linux-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
BuildRequires:	libpcap-devel >= 1.2

%description
Bit-Twist is a simple yet powerful libpcap-based Ethernet packet generator.
It is designed to complement tcpdump, which by itself has done a great job at capturing network traffic.
With Bit-Twist, you can now regenerate your captured traffic onto a live network!
Packets are generated from tcpdump trace file (.pcap file).
Bit-Twist also comes with a comprehensive trace file editor to allow you to change 
the contents of a trace file.
Generally, packet generator is useful in simulating networking traffic or scenario,
testing firewall, IDS, and IPS, and troubleshooting various network problems.


%prep
%setup -q -n %{name}-linux-%{version}
%patch0 -p0

%build
make %{?_smp_mflags}

%install
make install prefix=${RPM_BUILD_ROOT}/usr

%files
%defattr(-,root,root)
%{_bindir}/bittwist
%{_bindir}/bittwiste
%{_mandir}/man1/bittwist.1.gz
%{_mandir}/man1/bittwiste.1.gz
%doc CHANGES COPYING AUTHORS BUGS

%changelog
* Fri Feb 15 2013 Giuseppe Marco Randazzo <gmrandazzo@gmail.com>
- first build for bittwist

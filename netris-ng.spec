Summary:	netris next generation
Summary(pl):	netris, nastêpna generacja
Name:		netris-ng
Version:	0.01
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://download.berlios.de/netris-ng/%{name}-%{version}.tar.bz2
# Source0-md5:	f49f1952f8d5ade893ecf287a60ecdc2
URL:		http://netris-ng.berlios.de
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A netris clone.

%description -l pl
Klon netrisa.

%prep
%setup -q

%build
./Configure
%{__make} \
	CFLAGS="%{rpmcflags} -DNDEBUG -I/usr/include/ncurses" \
	LFLAGS="%{rpmldflags} -lncurses"

mv sr sr-ng

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {netris,sr}-ng $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ *_desc
%attr(755,root,root) %{_bindir}/*

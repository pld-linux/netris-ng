Summary:	netris next generation
Summary(pl.UTF-8):	netris, następna generacja
Name:		netris-ng
Version:	0.015
Release:	4
License:	GPL v2
Group:		Applications/Games
Source0:	http://download.berlios.de/netris-ng/%{name}-%{version}.tar.bz2
# Source0-md5:	c15d259e91e933a3fc5839ccf9b5c9ab
URL:		http://netris-ng.berlios.de/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A netris clone.

%description -l pl.UTF-8
Klon netrisa.

%prep
%setup -q

%build
./Configure
%{__make} \
	CC="%{__cc}" \
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

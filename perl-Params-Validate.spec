#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Validate
Version  : 1.29
Release  : 37
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz
Summary  : 'Validate method/function parameters'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Params-Validate-lib = %{version}-%{release}
Requires: perl-Params-Validate-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
# NAME
Params::Validate - Validate method/function parameters
# VERSION
version 1.29

%package dev
Summary: dev components for the perl-Params-Validate package.
Group: Development
Requires: perl-Params-Validate-lib = %{version}-%{release}
Provides: perl-Params-Validate-devel = %{version}-%{release}

%description dev
dev components for the perl-Params-Validate package.


%package lib
Summary: lib components for the perl-Params-Validate package.
Group: Libraries
Requires: perl-Params-Validate-license = %{version}-%{release}

%description lib
lib components for the perl-Params-Validate package.


%package license
Summary: license components for the perl-Params-Validate package.
Group: Default

%description license
license components for the perl-Params-Validate package.


%prep
%setup -q -n Params-Validate-1.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
./Build test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Params-Validate
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Params-Validate/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/Validate.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/Validate/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/Validate/PP.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/Validate/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/ValidatePP.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Params/ValidateXS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Params::Validate.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Params/Validate/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Params-Validate/LICENSE

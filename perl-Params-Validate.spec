#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Validate
Version  : 1.29
Release  : 25
URL      : http://www.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz
Source0  : http://www.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz
Summary  : 'Validate method/function parameters'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Params-Validate-lib
Requires: perl-Params-Validate-doc
BuildRequires : perl(Module::Build)
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

%package doc
Summary: doc components for the perl-Params-Validate package.
Group: Documentation

%description doc
doc components for the perl-Params-Validate package.


%package lib
Summary: lib components for the perl-Params-Validate package.
Group: Libraries

%description lib
lib components for the perl-Params-Validate package.


%prep
%setup -q -n Params-Validate-1.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/Validate.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/Validate/Constants.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/Validate/PP.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/Validate/XS.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/ValidatePP.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Params/ValidateXS.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Params/Validate/XS/XS.so

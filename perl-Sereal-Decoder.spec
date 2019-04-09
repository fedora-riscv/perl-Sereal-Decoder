Name:           perl-Sereal-Decoder
Version:        4.006
Release:        1%{?dist}
Summary:        Perl deserialization for Sereal format
# lib/Sereal/Decoder.pm:    GPL+ or Artistic
# miniz.c:                  Unlicense (unbundled)
# snappy:                   BSD (unbundled)
# zstd:                     BSD (unbundled)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sereal-Decoder
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Decoder-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  csnappy-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  miniz-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.0
# File::Find not used
# File::Path not used in inc/Sereal/BuildTools.pm
# File::Spec not used in inc/Sereal/BuildTools.pm
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
# Benchmark not used
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(threads)
# Time::HiRes not used
BuildRequires:  perl(utf8)
# Optional tests:
%if !%{defined perl_bootstrap}
# Some tests require Sereal::Encoder 3.005003, but most of them do not require
# exact version. Thus do not constrain the version here.
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This library implements a deserializer for an efficient, compact-output,
and feature-rich binary protocol called Sereal.

%prep
%setup -q -n Sereal-Decoder-%{version}
# Remove bundled Perl modules
rm -r ./inc/Devel
sed -i -e '/^inc\/Devel\//d' MANIFEST
# Remove bundled csnappy
rm -r ./snappy
sed -i -e '/^snappy\//d' MANIFEST
# Remove bundled miniz
rm miniz.*
sed -i -e '/^miniz\./d' MANIFEST
# Remove bundled zstd
rm -r zstd
sed -i -e '/^zstd\//d' MANIFEST

%build
unset DEBUG SEREAL_USE_BUNDLED_LIBS SEREAL_USE_BUNDLED_CSNAPPY \
    SEREAL_USE_BUNDLED_MINIZ SEREAL_USE_BUNDLED_ZSTD
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sereal*
%{_mandir}/man3/*

%changelog
* Tue Apr 09 2019 Petr Pisar <ppisar@redhat.com> - 4.006-1
- 4.006 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-1
- 4.005 bump

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 4.004-1
- 4.004 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.015-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.015-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Petr Pisar <ppisar@redhat.com> - 3.015-1
- 3.015 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.014-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.014-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Petr Pisar <ppisar@redhat.com> - 3.014-1
- 3.014 bump

* Wed Dec 02 2015 Petr Pisar <ppisar@redhat.com> - 3.009-1
- 3.009 bump

* Mon Nov 30 2015 Petr Pisar <ppisar@redhat.com> - 3.008-1
- 3.008 bump

* Fri Nov 27 2015 Petr Pisar <ppisar@redhat.com> - 3.007-2
- Do not constrain Sereal::Encoder version

* Fri Nov 27 2015 Petr Pisar <ppisar@redhat.com> - 3.007-1
- 3.007 bump

* Mon Nov 16 2015 Petr Pisar <ppisar@redhat.com> - 3.006-1
- 3.006 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-2
- Perl 5.22 rebuild

* Tue Jan 06 2015 Petr Pisar <ppisar@redhat.com> - 3.005-1
- 3.005 bump

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 3.004-1
- 3.004 bump

* Wed Nov 12 2014 Petr Pisar <ppisar@redhat.com> - 3.003-1
- 3.003 bump

* Thu Nov 06 2014 Petr Pisar <ppisar@redhat.com> - 3.002-2
- Finish Sereal bootstrap

* Fri Oct 10 2014 Petr Pisar <ppisar@redhat.com> 3.002-1
- Specfile autogenerated by cpanspec 1.78.

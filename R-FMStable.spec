#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-FMStable
Version  : 0.1.2
Release  : 6
URL      : https://cran.r-project.org/src/contrib/FMStable_0.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/FMStable_0.1-2.tar.gz
Summary  : Finite Moment Stable Distributions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-FMStable-lib
BuildRequires : clr-R-helpers

%description
with log maximally skew stable distributions, which are also
        called finite moment log stable distributions.

%package lib
Summary: lib components for the R-FMStable package.
Group: Libraries

%description lib
lib components for the R-FMStable package.


%prep
%setup -q -c -n FMStable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530402297

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530402297
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FMStable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FMStable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FMStable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library FMStable|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/FMStable/DESCRIPTION
/usr/lib64/R/library/FMStable/INDEX
/usr/lib64/R/library/FMStable/Meta/Rd.rds
/usr/lib64/R/library/FMStable/Meta/features.rds
/usr/lib64/R/library/FMStable/Meta/hsearch.rds
/usr/lib64/R/library/FMStable/Meta/links.rds
/usr/lib64/R/library/FMStable/Meta/nsInfo.rds
/usr/lib64/R/library/FMStable/Meta/package.rds
/usr/lib64/R/library/FMStable/NAMESPACE
/usr/lib64/R/library/FMStable/R/FMStable
/usr/lib64/R/library/FMStable/R/FMStable.rdb
/usr/lib64/R/library/FMStable/R/FMStable.rdx
/usr/lib64/R/library/FMStable/doc/paper5.pdf
/usr/lib64/R/library/FMStable/help/AnIndex
/usr/lib64/R/library/FMStable/help/FMStable.rdb
/usr/lib64/R/library/FMStable/help/FMStable.rdx
/usr/lib64/R/library/FMStable/help/aliases.rds
/usr/lib64/R/library/FMStable/help/paths.rds
/usr/lib64/R/library/FMStable/html/00Index.html
/usr/lib64/R/library/FMStable/html/R.css
/usr/lib64/R/library/FMStable/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/FMStable/libs/FMStable.so
/usr/lib64/R/library/FMStable/libs/FMStable.so.avx2
/usr/lib64/R/library/FMStable/libs/FMStable.so.avx512

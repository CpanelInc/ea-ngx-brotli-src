Summary: Phusion Passenger application server Source Code
Name: ea-ngx-brotli-src

# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4590 for more details
%define release_prefix 2

Version: 1.0.0
Release: %{release_prefix}%{?dist}.cpanel
Group:   System Environment/Libraries
License:  BSD-2-Clause License
URL: https://github.com/google/ngx_brotli

Source0: %{version}.tar.gz

AutoReqProv: no
%undefine __brp_mangle_shebangs

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

%prep

# TODO: remove rc once the version is not rc
%setup -n ngx_brotli-%{version}rc

%build

# nothing to do here

%install

set -x

if [ "$0" == "debian/override_dh_auto_install.sh" ]; then
    mkdir -p ./opt/cpanel/ea-ngx-brotli-src
    find . ! -name . -prune ! -name opt ! -name debian
    find . ! -name . -prune ! -name opt ! -name debian -exec mv {} opt/cpanel/ea-ngx-brotli-src \;
else
    mkdir -p %{buildroot}/opt/cpanel/ea-ngx-brotli-src
    cp -rf ./* %{buildroot}/opt/cpanel/ea-ngx-brotli-src
fi

%files
/opt/cpanel/ea-ngx-brotli-src/

%changelog
* Mon May 08 2023 Julian Brown <julian.brown@cpanel.net> - 1.0.0-2
- ZC-10936: Clean up Makefile and remove debug-package-nil

* Thu Feb 24 2022 Daniel Muey <dan@cpanel.net> - 1.0.0-1
- ZC-9697: Initial version

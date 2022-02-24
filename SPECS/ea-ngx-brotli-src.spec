%global debug_package %{nil}

Summary: Phusion Passenger application server Source Code
Name: ea-ngx-brotli-src

# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4590 for more details
%define release_prefix 1

Version: 1.0.0rc
Release: %{release_prefix}%{?dist}.cpanel
Group:   System Environment/Libraries
License:  BSD-2-Clause License
URL: https://github.com/google/ngx_brotli

Source0: v%{version}.tar.gz

AutoReqProv: no

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.

%prep
%setup -n ngx_brotli-%{version}

%build

# nothing to do here

%install

mkdir -p %{buildroot}/opt/cpanel/ea-ngx-brotli-src
cp -rf ./* %{buildroot}/opt/cpanel/ea-ngx-brotli-src

%files
/opt/cpanel/ea-ngx-brotli-src/

%changelog
* Thu Feb 24 2022 Daniel Muey <dan@cpanel.net> - 1.0.0rc-1
- ZC-9697: Initial version

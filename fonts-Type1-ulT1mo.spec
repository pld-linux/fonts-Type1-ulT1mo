Summary:	ulT1mo collection of Type1 fonts with iso8859-2 encoding
Summary(pl):	ulT1mo - zestaw fontów Type1 z kodowaniem iso8859-2
Name:		fonts-Type1-ulT1mo
Version:	1.0beta
Release:	3
License:	Freeware
Group:		X11/Fonts
Source0:	ulT1mo-beta-1.0.tgz
# Source0-md5:	90533d6c3b505333e7e78ffc0451beb5
Source1:	%{name}.Fontmap
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
Obsoletes:	XFree86-fonts-Type1-ISO8859-2
Obsoletes:	XFree86-ISO8859-2-Type1-fonts
Obsoletes:	XFree86-latin2-Type1-fonts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		t1fontsdir	%{_fontsdir}/Type1
%define		t1afmdir	%{t1fontsdir}/afm
%define		t1pfmdir	%{t1fontsdir}/pfm

%description
The ulT1mo (read ultimo) collection is bundle of freeware PostScript
Type1 fonts with iso8859-2 encoding.

%description -l pl
ulT1mo (czytaj: ultimo) to zestaw darmowych fontów Type1 z kodowaniem
iso8859-2.

%prep
%setup -q -n ulT1mo-beta-1.0

%build
for f in *.pfb ; do
	mv -f $f `basename $f .pfb`-ISO-8859-2.pfb
done
cd afm
for f in *.afm ; do
	mv -f $f `basename $f .afm`-ISO-8859-2.afm
done
cd ../pfm
for f in *.pfm ; do
	mv -f $f `basename $f .pfm`-ISO-8859-2.pfm
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{t1fontsdir},%{t1afmdir},%{t1pfmdir}}

install *.pfb $RPM_BUILD_ROOT%{t1fontsdir}
install afm/*.afm $RPM_BUILD_ROOT%{t1afmdir}
install pfm/*.pfm $RPM_BUILD_ROOT%{t1pfmdir}

sed -e 's/\.pfb/-ISO-8859-2\.pfb/' fonts.scale.ulT1mo\
	> $RPM_BUILD_ROOT%{t1fontsdir}/fonts.scale.ulT1mo
install fonts.alias.ulT1mo $RPM_BUILD_ROOT%{t1fontsdir}/fonts.alias.ulT1mo
install %{SOURCE1} $RPM_BUILD_ROOT%{t1fontsdir}/Fontmap.ulT1mo

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc README*
%{t1fontsdir}/*.pfb
%{t1fontsdir}/fonts.scale.ulT1mo
%{t1fontsdir}/fonts.alias.ulT1mo
%{t1fontsdir}/Fontmap.ulT1mo
%{t1afmdir}/*.afm
%{t1pfmdir}/*.pfm

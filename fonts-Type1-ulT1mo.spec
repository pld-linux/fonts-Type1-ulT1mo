Summary:	ulT1mo collection of Type1 fonts with iso8859-2 encoding
Summary(pl):	ulT1mo - zestaw fontów Type1 z kodowaniem iso8859-2
Name:		fonts-Type1-ulT1mo
Version:	1.0beta
Release:	1
License:	freeware
Group:		X11/Fonts
Source0:	ulT1mo-beta-1.0.tgz
Source1:	%{name}.Fontmap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	XFree86-fonts-Type1-ISO8859-2
Obsoletes:	XFree86-ISO8859-2-Type1-fonts
Obsoletes:	XFree86-latin2-Type1-fonts
Requires(post,postun):	fileutils
Requires(post,postun):	grep
Requires(post,postun):	textutils
Requires(post,postun):	sed


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

gzip -9nf README.*

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{t1fontsdir}
umask 022
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap
cat fonts.alias.* > fonts.alias
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%postun
cd %{t1fontsdir}
umask 022
rm -f fonts.scale.bak Fontmap.bak
cat fonts.scale.* 2>/dev/null | sort -u > fonts.scale.tmp
cat fonts.scale.tmp | wc -l | sed -e 's/ //g' > fonts.scale
cat fonts.scale.tmp >> fonts.scale
rm -f fonts.scale.tmp fonts.dir
ln -sf fonts.scale fonts.dir
cat Fontmap.* > Fontmap 2>/dev/null
cat fonts.alias.* > fonts.alias 2>/dev/null
if [ -x /usr/X11R6/bin/xftcache ]; then
	/usr/X11R6/bin/xftcache .
fi

%files
%defattr(644,root,root,755)
%doc README*.gz
%{t1fontsdir}/*.pfb
%{t1fontsdir}/fonts.scale.ulT1mo
%{t1fontsdir}/fonts.alias.ulT1mo
%{t1fontsdir}/Fontmap.ulT1mo
%{t1afmdir}/*.afm
%{t1pfmdir}/*.pfm

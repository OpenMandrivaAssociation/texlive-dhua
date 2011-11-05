# revision 24035
# category Package
# catalog-ctan /macros/latex/contrib/dhua
# catalog-date 2011-09-20 00:29:10 +0200
# catalog-license lppl1.3
# catalog-version 0.11
Name:		texlive-dhua
Version:	0.11
Release:	1
Summary:	German abbreviations using thin space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dhua
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides commands for those abbreviations of German
phrases for which the use of thin space is recommended. Setup
commands \newdhua and \newtwopartdhua are provided, as well as
commands for single cases (such as \zB for 'z. B.', saving the
user from typing such as 'z.\,B.'). To typeset the
documentation, the niceverb package, version 0.44, or later, is
required. Das Paket `dhua' stellt Befehle fur sog.
mehrgliedrige Abkurzungen bereit, fur die schmale Leerzeichen
(Festabstande) empfohlen werden (Duden, Wikipedia). In die
englische Paketdokumentation sind deutsche Erlauterungen
eingestreut.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dhua/dhua.cfg
%{_texmfdistdir}/tex/latex/dhua/dhua.sty
%doc %{_texmfdistdir}/doc/latex/dhua/README
%doc %{_texmfdistdir}/doc/latex/dhua/README.pdf
%doc %{_texmfdistdir}/doc/latex/dhua/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/dhua/dhua.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dhua/README.tex
%doc %{_texmfdistdir}/source/latex/dhua/dhua.tex
%doc %{_texmfdistdir}/source/latex/dhua/srcfiles.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

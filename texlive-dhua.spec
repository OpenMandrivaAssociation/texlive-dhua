%global tl_name dhua
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	German abbreviations using thin space
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dhua
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dhua.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for those abbreviations of German phrases
for which the use of thin space is recommended. Setup commands \newdhua
and \newtwopartdhua are provided, as well as commands for single cases
(such as \zB for 'z. B.', saving the user from typing such as 'z.\,B.').
To typeset the documentation, the niceverb package, version 0.44, or
later, is required. Das Paket `dhua' stellt Befehle fur sog.
mehrgliedrige Abkurzungen bereit, fur die schmale Leerzeichen
(Festabstande) empfohlen werden (Duden, Wikipedia). In die englische
Paketdokumentation sind deutsche Erlauterungen eingestreut.


%global tl_name ulem
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Package for underlining
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ulem
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ulem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ulem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an \ul (underline) command which will break over
line ends; this technique may be used to replace \em (both in that form
and as the \emph command), so as to make output look as if it comes from
a typewriter. The package also offers double and wavy underlining, and
striking out (line through words) and crossing out (/// over words). The
package works with both Plain TeX and LaTeX.


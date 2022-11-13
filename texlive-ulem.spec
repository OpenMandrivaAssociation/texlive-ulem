Name:		texlive-ulem
Version:	53365
Release:	1
Summary:	Package for underlining
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ulem
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulem.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an \ul (underline) command which will
break over line ends; this technique may be used to replace \em
(both in that form and as the \emph command), so as to make
output look as if it comes from a typewriter. The package also
offers double and wavy underlining, and striking out (line
through words) and crossing out (/// over words). The package
works with both Plain TeX and LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ulem/ulem.sty
%doc %{_texmfdistdir}/doc/generic/ulem/README
%doc %{_texmfdistdir}/doc/generic/ulem/ulem.ltx
%doc %{_texmfdistdir}/doc/generic/ulem/ulem.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

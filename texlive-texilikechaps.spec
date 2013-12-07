# revision 28553
# category Package
# catalog-ctan /macros/latex/contrib/misc/texilikechaps.sty
# catalog-date 2012-12-16 19:31:26 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-texilikechaps
Version:	1.0a
Release:	4
Summary:	Format chapters with a texi-like format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikechaps.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikechaps.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to reduce the size of the rather
large chapter headings in standard classes into a texi-like
smaller format. Details of the format may be controlled with
internal commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texilikechaps/texilikechaps.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

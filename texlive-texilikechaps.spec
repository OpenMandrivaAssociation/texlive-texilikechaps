Name:		texlive-texilikechaps
Version:	28553
Release:	2
Summary:	Format chapters with a texi-like format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikechaps.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikechaps.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

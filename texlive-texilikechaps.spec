# revision 16752
# category Package
# catalog-ctan /macros/latex/contrib/misc/texilikechaps.sty
# catalog-date 2010-01-19 19:25:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-texilikechaps
Version:	1.0
Release:	1
Summary:	Format chapters with a texi-like format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc/texilikechaps.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texilikechaps.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package enables the user to reduce the size of the rather
large chapter headings in standard classes into a texi-like
smaller format. Details of the format may be controlled with
internal commands.

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
%{_texmfdistdir}/tex/latex/texilikechaps/texilikechaps.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

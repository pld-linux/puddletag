Summary:	A tag editor for Linux based on Mp3tag
Name:		puddletag
Version:	0.9.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/puddletag/%{name}-%{version}.tar.gz
# Source0-md5:	87240a3d97f9e9fe217d58f950403074
URL:		http://puddletag.sourceforge.net
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
puddletag is a tag editor for Linux loosely based on the Windows
program Mp3tag. Basically it uses a table layout so that all the tags
you want to edit by hand are visible and easily editable. However,
puddletag excels at automating repetitive task like extracting tag
information from filenames, renaming files based on their tags by
using patterns.

There're functions, which can do things like replace text, trim,
change the case of any tag, etc. Actions can automate repetitive
tasks, and then theres importing music libraries (though only
QuodLibet is supported for now), automatic retrieval of tags via
musicbrainz and more, so fire it up and explore.

Supported formats include: id3v1, id3v2 (mp3), AAC (mp4, m4a, etc.),
VorbisComments (ogg, flac) and APEv2 (ape).

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO THANKS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitescriptdir}/puddlestuff
%{py_sitescriptdir}/puddlestuff/*.py[co]
%dir %{py_sitescriptdir}/puddlestuff/audioinfo
%{py_sitescriptdir}/puddlestuff/audioinfo/*.py[co]
%dir %{py_sitescriptdir}/puddlestuff/libraries
%{py_sitescriptdir}/puddlestuff/libraries/*.py[co]
%dir %{py_sitescriptdir}/puddlestuff/mainwin
%{py_sitescriptdir}/puddlestuff/mainwin/*.py[co]
%dir %{py_sitescriptdir}/puddlestuff/tagsources
%{py_sitescriptdir}/puddlestuff/tagsources/*.py[co]
%{py_sitescriptdir}/%{name}-*.egg-info
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/%{name}.png

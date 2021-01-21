Name:       huniverse
Version:    1.0
Release:    alt1
Summary:    Most simple RPM package
License:    no
Group:	other
Source: ./huniverse.tar

%description
This is my first RPM

%prep
echo "STAGE1: prep"
%setup -n src

%build
echo "STAGE1: build"
ls
%make_build huniverse

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 huniverse %{buildroot}/usr/bin/

%files
/usr/bin/huniverse

%changelog
# nothing

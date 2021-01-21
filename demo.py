from kdependencies import Dependencies, InstalledPackage

for p in Dependencies.get():
    p.jsonprint()
    print(p.get_install_name())
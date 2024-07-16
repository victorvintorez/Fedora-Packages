#!/usr/bin/env sh

set -e

SPECFILE=ironbar-git.spec

# Get package commits
oldCommit="$()"
newCommit="$()"

# Get package versions
oldVer="$(rpmspec -q --qf "%{version}\n" $SPECFILE | head -1 | sed "s/\.git.*//")"
newVer="$(curl --no-progress-meter https://raw.githubusercontent.com/JakeStanger/ironbar/master/Cargo.toml | grep "version" | head -1 | sed -e "s/^.*\"\(.*\)\".*/\1/" -e "s/-/~/g")"


# Check old version against new version to avoid unessecary updates
if [ "$(printf '%s\n' "$oldVer" "$newVer" | sort -Vr | head -1)" = "$oldVer" ]; then
    echo "The upstream has not had a new release. Exiting..."
    exit 1
elif [ "$(printf '%s\n' "$oldVer" "$newVer" | sort -Vr | head -1)" != "$newVer" ]; then
    echo "Upstream is behind the current package (somehow). Exiting..."
    exit 1
else
    sed -i "s/$oldVer/$newVer/" $SPECFILE
fi

git commit -am "[ironbar]: ${oldVer} -> ${newVer}"
git push
echo "Updated ironbar version: ${oldVer} -> ${newVer}"
exit 0


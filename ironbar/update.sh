#!/usr/bin/env sh

set -e

SPECFILE=ironbar.spec

# Get package versions
oldVer="$(rpmspec -q --qf "%{version}\n" $SPECFILE | head -1)"
newVer="$(curl --no-progress-meter "https://api.github.com/repos/jakestanger/ironbar/releases/latest" | jq -r ".tag_name" | sed -e "s/^v//" -e "s/-/~/g")"

# Check for semver
case $newVer in
    *"pre")
        echo "This package does not include pre-releases. Exiting..."
        exit 1
        ;;
    *"alpha")
        echo "This package does not include alpha releases. Exiting..."
        exit 1
        ;;
    *"beta")
        echo "This package does not include beta releases. Exiting..."
        exit 1
        ;;
    *"rc")
        echo "This package does not include release candidates. Exiting..."
        exit 1
        ;;
esac

# Check old version against new version to avoid unessecary updates
if [ "$(printf '%s\n' "$oldVer" "$newVer" | sort -Vr | head -1)" = "$oldVer" ]; then
    echo "The upstream has not had a new release. Exiting..."
    exit 1
elif [ "$(printf '%s\n' "$oldVer" "$newVer" | sort -Vr | head -1)" != "$newVer" ]; then
    echo "Upstream is behind the current package (somehow). Exiting..."
    exit 1
else
    sed -i "s/$oldVer/$newVer/" $SPECFILE
    git commit -am "[ironbar]: ${oldVer} -> ${newVer}"
    git push
    echo "Updated ironbar version: ${oldVer} -> ${newVer}"
    exit 0
fi

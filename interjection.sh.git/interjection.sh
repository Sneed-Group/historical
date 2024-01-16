#!/usr/bin/env sh

#Licensed under GPL3 with <3
PACKAGES=""
if command -v apk > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(apk info)"
fi
if command -v dpkg > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(dpkg --get-selections | tr -s '[:blank:]' | cut -f1)"
fi
if command -v pacman > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(pacman -Qq)"
fi
if command -v rpm > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(rpm -qa --qf '%{NAME}\n')"
fi
if command -v pkginfo > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(pkginfo -i | cut -d' ' -f1)"
fi
if command -v xpkg > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(xpkg)"
fi
if command -v xbps-install > /dev/null 2>&1; then
    echo "Package 'xtools' is not installed. You can install it with 'xbps-install xtools'"
    exit 1
fi
if command -v equery > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(equery list -F '$name' '*')"
fi
if command -v emerge > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(ls -d -1 /var/db/pkg/*/* | sed 's/-[0-9].*//' | awk -F/ '{print $NF}')"
fi
if command -v brew > /dev/null 2>&1; then
    PACKAGES="$PACKAGES/$(brew list)"
fi
if command -v nixos-version > /dev/null 2>&1; then
    PACKAGES="$(ls -d -1 /nix/store/*/ | cut -c 45- | sed 's/.$//' | sed 's/-[0-9].*//' | sort | uniq)"
fi
if command -v flatpak > /dev/null 2>&1; then
    PACKAGES="$PACKAGES\n$(flatpak list --columns name | tr -s '[:blank:]' | cut -f1)"
fi

SLASH="$(printf %s "$PACKAGES" | tr '\n' '/')"
PLUS="$(printf %s "$SLASH" | sed 's/\// plus /g')"
COMMA="$(printf %s "$SLASH" | sed 's/\//, /g')"

TEMPLATE="\
I'd just like to interject for a moment. What you're referring to as Linux, \
is in fact, GNU/${SLASH}/Linux, or as I've recently taken to calling it, GNU plus ${PLUS} \
plus Linux. Linux is not an operating system unto itself, but rather another free component \
of a fully functioning GNU/${SLASH} system made useful by the GNU/${SLASH} corelibs, shell \
utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU/${SLASH} system every day, \
without realizing it. Through a peculiar turn of events, the version of GNU/${SLASH} \
which is widely used today is often called \"Linux\", and many of its users are \
not aware that it is basically the GNU/${SLASH} system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a \
part of the system they use. Linux is the kernel: the program in the system \
that allocates the machine's resources to the other programs that you run. \
The kernel is an essential part of an operating system, but useless by itself; \
it can only function in the context of a complete operating system. Linux is \
normally used in combination with the GNU/${SLASH} operating system: the whole \
system is basically GNU with ${COMMA}, and Linux added, or GNU/${SLASH}/Linux. \
All the so-called \"Linux\" distributions are really distributions of GNU/${SLASH}/Linux.
"

printf %s "$TEMPLATE"

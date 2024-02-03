Installation:

Last login: Fri Jan 26 14:39:21 on ttys000
victorg@victors-air ~ % git clone https://github.com/ChristopherBrix/vnncomp2023_benchmarks.git

Cloning into 'vnncomp2023_benchmarks'...
remote: Enumerating objects: 4088, done.
remote: Counting objects: 100% (1857/1857), done.
remote: Compressing objects: 100% (1219/1219), done.
error: RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly: CANCEL (err 8)
error: 1535 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output
victorg@victors-air ~ % git clone https://github.com/ChristopherBrix/vnncomp2023_benchmarks.git

Cloning into 'vnncomp2023_benchmarks'...
remote: Enumerating objects: 4088, done.
remote: Counting objects: 100% (1857/1857), done.
remote: Compressing objects: 100% (1219/1219), done.
remote: Total 4088 (delta 667), reused 1801 (delta 637), pack-reused 2231
Receiving objects: 100% (4088/4088), 1.48 GiB | 2.16 MiB/s, done.
Resolving deltas: 100% (1604/1604), done.
Updating files: 100% (1220/1220), done.
victorg@victors-air ~ % cd vnncomp2023_benchmarks/benchmarks/vit

victorg@victors-air vit % ls
instances.csv	onnx		vnnlib
victorg@victors-air vit % cd ..
victorg@victors-air benchmarks % cd ..
victorg@victors-air vnncomp2023_benchmarks % cd /
victorg@victors-air / % ls
Applications	Users		cores		home		sbin		var
Library		Volumes		dev		opt		tmp
System		bin		etc		private		usr
victorg@victors-air / % cd vnncomp2023_benchmarks/benchmarks/vit

cd: no such file or directory: vnncomp2023_benchmarks/benchmarks/vit
victorg@victors-air / % cd ..
victorg@victors-air / % cd .
victorg@victors-air / % cd /
victorg@victors-air / % cd ~
victorg@victors-air ~ % ls
Applications			Music				VirtualKey.db
Applications (Parallels)	Parallels			cadical
Cisco Packet Tracer 8.2.1	Pictures			eclipse
Desktop				Postman				eclipse-workspace
Documents			Public				find.txt.gz
Downloads			README				pvmd
Library				Soulseek Chat Logs		v
MirrorTo.ini			Soulseek Downloads		vnncomp2023_benchmarks
Movies				Virtual Machines.localized
victorg@victors-air ~ % cd vnncomp2023_benchmarks/benchmarks/vit

victorg@victors-air vit % ls
instances.csv	onnx		vnnlib
victorg@victors-air vit % cd ~
victorg@victors-air ~ % brew 
Example usage:
  brew search TEXT|/REGEX/
  brew info [FORMULA|CASK...]
  brew install FORMULA|CASK...
  brew update
  brew upgrade [FORMULA|CASK...]
  brew uninstall FORMULA|CASK...
  brew list [FORMULA|CASK...]

Troubleshooting:
  brew config
  brew doctor
  brew install --verbose --debug FORMULA|CASK

Contributing:
  brew create URL [--no-fetch]
  brew edit [FORMULA|CASK...]

Further help:
  brew commands
  brew help [COMMAND]
  man brew
  https://docs.brew.sh
victorg@victors-air ~ % brew info
43 kegs, 46,790 files, 1005MB
victorg@victors-air ~ % brew update
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
argc                    glbinding@2             libwapcaplet            rattler-build           tfautomv
c3c                     halp                    limesuite               redress                 tomlplusplus
cargo-llvm-cov          helm-ls                 ncmdump                 retire                  urlscan
cargo-sweep             hopscotch-map           netsurf-buildsystem     rsyncy                  veilid
chisel-tunnel           icloudpd                nowplaying-cli          ruby@3.2                vulkan-volk
csvlens                 jot                     open-simh               scnlib                  wasmedge
direwolf                k8sgpt                  openjph                 senpai                  zigmod
doltgres                kiota                   opensca-cli             steamguard-cli          zipkin
dotter                  libnsbmp                pivit                   sugarjar
drogon                  libnsgif                purr                    terrapin-scanner
git-grab                libspelling             rathole                 texi2mdoc
==> New Casks
anka-build-cloud-controller    emby                           lyricsfinder                   salt
anka-build-cloud-registry      garmin-basecamp                markedit                       screens-assist
aqua                           geekbench-ml                   nightshade                     shadow-bot
bitbox                         heynote                        ollama                         streammusic
blockstream-green              ia-presenter                   opencat                        taccy
bugdom2                        imazing-profile-editor         openthesaurus-deutsch          theiaide
cleanupbuddy                   insomnium                      pile                           truhu
creality-print                 jyutping                       prettyclean                    ttu-base-suite
domzilla-caffeine              keyboard-cowboy                reader                         wakatime
easydevo                       lightburn                      roam                           xact
egovframedev                   lw-scanner                     sakura                         znote
==> Outdated Formulae
black               ipython             mypy                pandoc              python-psutil       python@3.12
c-ares              jupyterlab          node                python-jinja        python-setuptools   ruff
ca-certificates     libnghttp2          openssl@1.1         python-lsp-server   python-urllib3      sqlite
cmake               mpdecimal           openssl@3           python-markupsafe   python@3.11
==> Outdated Casks
temurin

You have 23 outdated formulae and 1 outdated cask installed.
You can upgrade them with brew upgrade
or list them with brew outdated.
victorg@victors-air ~ % brew update all
Error: This command updates brew itself, and does not take formula names.
Use `brew upgrade all` instead.
victorg@victors-air ~ % brew upgrade all
Error: No available formula with the name "all". Did you mean alp, ali or acl?
victorg@victors-air ~ % brew update
Already up-to-date.
victorg@victors-air ~ % brew install cmake
Warning: Treating cmake as a formula. For the cask, use homebrew/cask/cmake
cmake 3.27.7 is already installed but outdated (so it will be upgraded).
==> Downloading https://ghcr.io/v2/homebrew/core/cmake/manifests/3.28.2
################################################################################################################### 100.0%
==> Fetching cmake
==> Downloading https://ghcr.io/v2/homebrew/core/cmake/blobs/sha256:e64e37539642c97133e04b679f4ea861ca3d88a297338c9f5f8776
################################################################################################################### 100.0%
==> Upgrading cmake
  3.27.7 -> 3.28.2 

==> Pouring cmake--3.28.2.arm64_sonoma.bottle.tar.gz
==> Caveats
To install the CMake documentation, run:
  brew install cmake-docs

Emacs Lisp files have been installed to:
  /opt/homebrew/share/emacs/site-lisp/cmake
==> Summary
🍺  /opt/homebrew/Cellar/cmake/3.28.2: 3,329 files, 54.4MB
==> Running `brew cleanup cmake`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
Removing: /opt/homebrew/Cellar/cmake/3.27.7... (3,285 files, 55.3MB)
==> `brew cleanup` has not been run in the last 30 days, running now...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
Removing: /Users/victorg/Library/Caches/Homebrew/black--23.11.0_1... (910.2KB)
Removing: /Users/victorg/Library/Caches/Homebrew/c-ares--1.23.0... (208.1KB)
Removing: /Users/victorg/Library/Caches/Homebrew/ca-certificates--2023-08-22... (125.2KB)
Removing: /Users/victorg/Library/Caches/Homebrew/ipython--8.18.1... (2.3MB)
Removing: /Users/victorg/Library/Caches/Homebrew/jupyterlab--4.0.9_1... (26.2MB)
Removing: /Users/victorg/Library/Caches/Homebrew/libnghttp2--1.58.0... (216.9KB)
Removing: /Users/victorg/Library/Caches/Homebrew/mypy--1.7.1... (8MB)
Removing: /Users/victorg/Library/Caches/Homebrew/node--21.2.0... (15.3MB)
Removing: /Users/victorg/Library/Caches/Homebrew/openssl@3--3.2.0... (9.4MB)
Removing: /Users/victorg/Library/Caches/Homebrew/pandoc--3.1.9... (49.7MB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-jinja--3.1.2... (254.8KB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-lsp-server--1.9.0_1... (1.7MB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-markupsafe--2.1.3_1... (38KB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-psutil--5.9.6... (498.3KB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-setuptools--69.0.2... (773.4KB)
Removing: /Users/victorg/Library/Caches/Homebrew/python-urllib3--2.1.0... (200.6KB)
Removing: /Users/victorg/Library/Caches/Homebrew/python@3.12--3.12.0... (15.6MB)
Removing: /Users/victorg/Library/Caches/Homebrew/ruff--0.1.6... (5.8MB)
Removing: /Users/victorg/Library/Caches/Homebrew/sqlite--3.44.2... (2.2MB)
Removing: /Users/victorg/Library/Caches/Homebrew/api-source/Homebrew/homebrew-cask/76e3778857b07515c42687246a61321d7b5e03de/Cask/blackhole-2ch.rb... (1KB)
Removing: /Users/victorg/Library/Logs/Homebrew/python@3.12... (2 files, 3.5KB)
Removing: /Users/victorg/Library/Logs/Homebrew/openssl@3... (64B)
Removing: /Users/victorg/Library/Logs/Homebrew/ca-certificates... (64B)
Removing: /Users/victorg/Library/Logs/Homebrew/node... (64B)
Pruned 0 symbolic links and 5 directories from /opt/homebrew
victorg@victors-air ~ % cmake
Usage

  cmake [options] <path-to-source>
  cmake [options] <path-to-existing-build>
  cmake [options] -S <path-to-source> -B <path-to-build>

Specify a source directory to (re-)generate a build system for it in the
current working directory.  Specify an existing build directory to
re-generate its build system.

Run 'cmake --help' for more information.

victorg@victors-air ~ % cmake --version
cmake version 3.28.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
victorg@victors-air ~ % git clone https://github.com/NeuralNetworkVerification/Marabou.git

Cloning into 'Marabou'...
remote: Enumerating objects: 27227, done.
remote: Counting objects: 100% (455/455), done.
remote: Compressing objects: 100% (336/336), done.
remote: Total 27227 (delta 201), reused 278 (delta 112), pack-reused 26772
Receiving objects: 100% (27227/27227), 212.70 MiB | 1.60 MiB/s, done.
Resolving deltas: 100% (19525/19525), done.
victorg@victors-air ~ % xcode-select --install
xcode-select: note: Command line tools are already installed. Use "Software Update" in System Settings or the softwareupdate command line interface to install updates
victorg@victors-air ~ % xscode-select softwareupdate
zsh: command not found: xscode-select
victorg@victors-air ~ % xcode-select softwareupdate 
xcode-select: error: invalid argument 'softwareupdate'
Usage: xcode-select [options]

Print or change the path to the active developer directory. This directory
controls which tools are used for the Xcode command line tools (for example, 
xcodebuild) as well as the BSD development commands (such as cc and make).

Options:
  -h, --help                  print this help message and exit
  -p, --print-path            print the path of the active developer directory
  -s <path>, --switch <path>  set the path for the active developer directory
  --install                   open a dialog for installation of the command line developer tools
  -v, --version               print the xcode-select version
  -r, --reset                 reset to the default command line tools path
victorg@victors-air ~ % ls
Applications			Movies				Virtual Machines.localized
Applications (Parallels)	Music				VirtualKey.db
Cisco Packet Tracer 8.2.1	Parallels			cadical
Desktop				Pictures			eclipse
Documents			Postman				eclipse-workspace
Downloads			Public				find.txt.gz
Library				README				pvmd
Marabou				Soulseek Chat Logs		v
MirrorTo.ini			Soulseek Downloads		vnncomp2023_benchmarks
victorg@victors-air ~ % cd Marabou
victorg@victors-air Marabou % mkdir build
victorg@victors-air Marabou % ls
AUTHORS		COPYING		THANKS		maraboupy	resources	tools
CHANGELOG.md	MANIFEST.in	build		pyproject.toml	setup.py
CMakeLists.txt	README.md	deps		regress		src
victorg@victors-air Marabou % cd build
victorg@victors-air build % cmake ..
-- The C compiler identification is AppleClang 15.0.0.15000100
-- The CXX compiler identification is AppleClang 15.0.0.15000100
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Warning (dev) at CMakeLists.txt:82 (find_package):
  Policy CMP0144 is not set: find_package uses upper-case <PACKAGENAME>_ROOT
  variables.  Run "cmake --help-policy CMP0144" for policy details.  Use the
  cmake_policy command to set the policy and suppress this warning.

  CMake variable BOOST_ROOT is set to:

    /Users/victorg/Marabou/tools/boost_1_80_0/installed

  For compatibility, find_package is ignoring the variable, but code in a
  .cmake module might still use it.
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Could NOT find Boost (missing: Boost_INCLUDE_DIR program_options timer chrono thread) 
downloading boost
/Users/victorg/Marabou/tools/download_boost.sh: line 10: wget: command not found
unzipping boost
tar: Error opening archive: Failed to open 'boost_1_80_0.tar.gz'
installing boost
/Users/victorg/Marabou/tools/download_boost.sh: line 14: cd: boost_1_80_0: No such file or directory
/Users/victorg/Marabou/tools/download_boost.sh: line 21: ./bootstrap.sh: No such file or directory
/Users/victorg/Marabou/tools/download_boost.sh: line 22: ./b2: No such file or directory
/Users/victorg/Marabou/tools/download_boost.sh: line 24: ./bootstrap.sh: No such file or directory
/Users/victorg/Marabou/tools/download_boost.sh: line 25: ./b2: No such file or directory
CMake Error at /opt/homebrew/Cellar/cmake/3.28.2/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find Boost (missing: Boost_INCLUDE_DIR program_options timer
  chrono thread)
Call Stack (most recent call first):
  /opt/homebrew/Cellar/cmake/3.28.2/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  /opt/homebrew/Cellar/cmake/3.28.2/share/cmake/Modules/FindBoost.cmake:2393 (find_package_handle_standard_args)
  CMakeLists.txt:88 (find_package)


-- Configuring incomplete, errors occurred!
victorg@victors-air build % brew install wget
==> Downloading https://formulae.brew.sh/api/formula.jws.json
################################################################################################################### 100.0%
==> Downloading https://formulae.brew.sh/api/cask.jws.json
################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/wget/manifests/1.21.4
################################################################################################################### 100.0%
==> Fetching dependencies for wget: libunistring, gettext and libidn2
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/manifests/1.1
################################################################################################################### 100.0%
==> Fetching libunistring
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/blobs/sha256:6d49946a29c0b11e7c273edcdcff15d90b4d55bd9038e85
################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/gettext/manifests/0.22.4
################################################################################################################### 100.0%
==> Fetching gettext
==> Downloading https://ghcr.io/v2/homebrew/core/gettext/blobs/sha256:43d00547f4a1036a642c8a41650b483f0054cd239ab4b9ca1715
################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/manifests/2.3.7
################################################################################################################### 100.0%
==> Fetching libidn2
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/blobs/sha256:670f6ed3768acde8ce10b5dcfc88fef69cea994ff84491b253a5
################################################################################################################### 100.0%
==> Fetching wget
==> Downloading https://ghcr.io/v2/homebrew/core/wget/blobs/sha256:47cb2b77bcb48ee8d8b8fb222bcafe0febe11195ac6476402917da0
################################################################################################################### 100.0%
==> Installing dependencies for wget: libunistring, gettext and libidn2
==> Installing wget dependency: libunistring
==> Downloading https://ghcr.io/v2/homebrew/core/libunistring/manifests/1.1
Already downloaded: /Users/victorg/Library/Caches/Homebrew/downloads/a34801f1ad5800ba51b2b3951d82a913ccf0641982f86b02df2f0aa182535055--libunistring-1.1.bottle_manifest.json
==> Pouring libunistring--1.1.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libunistring/1.1: 56 files, 5.0MB
==> Installing wget dependency: gettext
==> Downloading https://ghcr.io/v2/homebrew/core/gettext/manifests/0.22.4
Already downloaded: /Users/victorg/Library/Caches/Homebrew/downloads/3ceb9457127eaa7378dd80ed256098ffb391e2350069becb25cfe2a14f0b7d6d--gettext-0.22.4.bottle_manifest.json
==> Pouring gettext--0.22.4.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gettext/0.22.4: 2,042 files, 24.3MB
==> Installing wget dependency: libidn2
==> Downloading https://ghcr.io/v2/homebrew/core/libidn2/manifests/2.3.7
Already downloaded: /Users/victorg/Library/Caches/Homebrew/downloads/45d1d4d2930c4782bf53e761a1c0166cd8a40f4193ac8c44e86f0b6708e80354--libidn2-2.3.7.bottle_manifest.json
==> Pouring libidn2--2.3.7.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libidn2/2.3.7: 80 files, 1MB
==> Installing wget
==> Pouring wget--1.21.4.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/wget/1.21.4: 91 files, 4.4MB
==> Running `brew cleanup wget`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
victorg@victors-air build % ls
CMakeCache.txt	CMakeFiles
victorg@victors-air build % cmake ..
CMake Warning (dev) at CMakeLists.txt:82 (find_package):
  Policy CMP0144 is not set: find_package uses upper-case <PACKAGENAME>_ROOT
  variables.  Run "cmake --help-policy CMP0144" for policy details.  Use the
  cmake_policy command to set the policy and suppress this warning.

  CMake variable BOOST_ROOT is set to:

    /Users/victorg/Marabou/tools/boost_1_80_0/installed

  For compatibility, find_package is ignoring the variable, but code in a
  .cmake module might still use it.
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find Boost (missing: Boost_INCLUDE_DIR program_options timer chrono thread) 
downloading boost
^C
victorg@victors-air build % cmake ..
CMake Warning (dev) at CMakeLists.txt:82 (find_package):
  Policy CMP0144 is not set: find_package uses upper-case <PACKAGENAME>_ROOT
  variables.  Run "cmake --help-policy CMP0144" for policy details.  Use the
  cmake_policy command to set the policy and suppress this warning.

  CMake variable BOOST_ROOT is set to:

    /Users/victorg/Marabou/tools/boost_1_80_0/installed

  For compatibility, find_package is ignoring the variable, but code in a
  .cmake module might still use it.
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could NOT find Boost (missing: Boost_INCLUDE_DIR program_options timer chrono thread) 
downloading boost



boost downloads ->
CMake Deprecation Warning at tools/pybind11-2.10.4/CMakeLists.txt:8 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- pybind11 v2.10.4 
CMake Warning (dev) at tools/pybind11-2.10.4/tools/FindPythonLibsNew.cmake:98 (find_package):
  Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
  are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
  the cmake_policy command to set the policy and suppress this warning.

Call Stack (most recent call first):
  tools/pybind11-2.10.4/tools/pybind11Tools.cmake:50 (find_package)
  tools/pybind11-2.10.4/tools/pybind11Common.cmake:180 (include)
  tools/pybind11-2.10.4/CMakeLists.txt:208 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found PythonInterp: /opt/homebrew/bin/python3 (found suitable version "3.11.3", minimum required is "3.6") 
-- Found PythonLibs: /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/lib/libpython3.11.dylib
-- Performing Test HAS_FLTO
-- Performing Test HAS_FLTO - Success
-- Performing Test HAS_FLTO_THIN
-- Performing Test HAS_FLTO_THIN - Success
-- Found CxxTest: /Users/victorg/Marabou/tools/cxxtest  
/Users/victorg/Marabou/build/bin/mps
-- Configuring done (345.0s)
-- Generating done (0.3s)
-- Build files have been written to: /Users/victorg/Marabou/build
victorg@victors-air build % 
victorg@victors-air build % 
victorg@victors-air build % 
victorg@victors-air build % 
victorg@victors-air build % 
victorg@victors-air build %

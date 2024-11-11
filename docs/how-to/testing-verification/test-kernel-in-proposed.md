# How to test kernels in -proposed

Ubuntu kernels are uploaded to the -proposed pocket for testing before being
published to -updates and -security. You can download these pre-release kernels
to install and test them before a stable release, but you must opt in to package
from -proposed as they are not enabled by default.

## Enable the -proposed pocket to software sources

To install packages from -proposed, you need to enable the relevant source
repositories.

### Enable the -proposed pocket via GUI

1. Open "Software & Updates".
1. Go to the "Developer Options" tab.
1. Enable the {guilabel}`Pre-released updates (<series>-proposed)` option.

### Enable the -proposed pocket via CLI

`````{tab-set}
````{tab-item} Noble Numbat 24.04 (and newer)

Add "\<series\>-proposed" (e.g. "noble-proposed") to the `Suites:` line in the 
{file}`/etc/apt/sources.list.d/ubuntu.sources` file.
```{code-block} text
:emphasize-lines: 3

Types: deb
URIs: http://archive.ubuntu.com/ubuntu
Suites: noble noble-updates noble-backports <series>-proposed
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```
````
````{tab-item} Mantic Minotaur 23.10 (and older)

Add "\<series\>-proposed" (e.g. "jammy-proposed") to the following line in:

- {file}`/etc/apt/sources.list`:
  ```{code-block} text
  deb http://archive.ubuntu.com/ubuntu/ <series>-proposed restricted main multiverse universe
  ```

- {file}`/etc/apt/sources.list.d/` (for non-x86 architectures):
  ```{code-block} text
  deb http://ports.ubuntu.com/ubuntu-ports <series>-proposed restricted main multiverse universe
  ```
````
`````

## Install the pre-release kernel

Update the sources cache:

```{code-block} console
sudo apt update
```

Then install the kernel as per usual. If the kernel version in -proposed is the
highest in any pocket, install it by running:

```{code-block} console
sudo apt install linux-<flavour>
```

If you want a specific (earlier) version, include the version in the command:

```{code-block} console
sudo apt install linux-<flavour>=<version>
```

After installing the kernel, reboot your machine. After booting up again, verify
that the correct kernel is loaded with:

```{code-block} console
uname -r
```

This should print the correct kernel version and flavour.
# How to build an Ubuntu Linux kernel

If you have patches you need to apply to the Ubuntu Linux kernel, or you want to change some kernel configs, you may need to build your kernel from source.
Follow these steps to customise and build the Ubuntu Linux kernel locally.

## Prerequisites

This guide supports Xenial Xerus and newer.

It is recommended to have 8GB of RAM or more to build the Linux kernel.

If this is the first time you are building a kernel on your system, you will need to {ref}`set up your build environment <how-to-build-kernel-setup>` and {ref}`install the required packages <how-to-build-kernel-install-packages>`.

Otherwise, skip ahead to {ref}`how-to-build-kernel-obtain-source`.

(how-to-build-kernel-setup)=
### Set up build environment

To build an Ubuntu kernel, you will need enable the necessary source repositories in the {file}`sources.list` or {file}`ubuntu.sources` file.

`````{tab-set}
````{tab-item} Noble Numbat 24.04 (and newer)

Add "deb-src" to the `Types`: line in the
{file}`/etc/apt/sources.list.d/ubuntu.sources` file.

```{code-block} text
:emphasize-lines: 1

Types: deb deb-src
URIs: http://archive.ubuntu.com/ubuntu
Suites: noble noble-updates noble-backports
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```
````

````{tab-item} Mantic Minotaur 23.10 (and older)

Check that you have the following entries in the {file}`/etc/apt/sources.list`
file. If not, add or uncomment these lines for your Ubuntu release.
```{code-block} text

deb-src http://archive.ubuntu.com/ubuntu jammy main
deb-src http://archive.ubuntu.com/ubuntu jammy-updates main
```
````
`````

(how-to-build-kernel-install-packages)=
### Install required packages

To install the required packages and build dependencies, run:

```{code-block} shell
sudo apt update
sudo apt build-dep -y linux linux-image-unsigned-$(uname -r)
sudo apt install -y fakeroot llvm libncurses-dev dwarves
```

(how-to-build-kernel-obtain-source)=
## Obtain the source for an Ubuntu release

There are different ways to get the kernel sources, depending on the kernel version you want to make changes to.

### Get kernel source for version installed on build machine

Use the `apt source` command to get the source code for the kernel version currently running on your build machine.

```{code-block} shell
apt source linux-image-unsigned-$(uname -r)
```

This will download and unpack the kernel source files to your current working directory.

```{code-block} text
<working directory>
├── linux-X.Y.Z/
│   └── *
├── linux_X.Y.Z-*.diff.gz
├── linux_X.Y.Z-*.dsc
└── linux_X.Y.Z.orig.tar.gz
```

### Get kernel source for other versions

% TODO: Create how-to for Git method

Use Git to get the source code for other kernel versions. See {doc}`How to obtain kernel source for an Ubuntu release using Git </how-to/prepare/obtain-kernel-source-git>` for detailed instructions.

## Prepare the kernel source

Once you have the kernel source, go to the kernel source working directory (e.g. `linux-6.8.0`) and run the following commands to ensure you have a clean build environment and the necessary scripts have execute permissions:

```{code-block} shell

cd <kernel source working directory>
chmod a+x debian/rules
chmod a+x debian/scripts/*
chmod a+x debian/scripts/misc/*
fakeroot debian/rules clean
```

### Modify ABI number

You should modify the kernel version number to avoid conflicts and to differentiate the development kernel from the kernel released by Canonical.

To do so, modify the ABI number (the number after the dash following the kernel version) to "999" in the first line of the `<kernel source working directory>/debian.master/changelog` file.

For example, modify the ABI number to "999" for Noble Numbat:

```{code-block} text
linux (6.8.0-999.48) noble; urgency=medium
```

If you are building something other than the generic Ubuntu Linux kernel, modify the ABI number in the `<kernel source working directory>/debian.<derivative>/changelog` file instead.

## Modify kernel configuration

(Optional) To enable or disable any features using the kernel configuration, run:

```{code-block} shell
cd <kernel source working directory>
fakeroot debian/rules editconfigs
```

This will invoke the `menuconfig` interface for you to edit specific configuration files related to the Ubuntu kernel package. You will need to explicitly respond with {kbd}`Y` or {kbd}`N` when making any config changes to avoid getting errors later in the build process.

## Customise the kernel

(Optional) Add any firmware, binary blobs, or patches as needed.

## Build the kernel

You are now ready to build the kernel.

```{code-block} shell
cd <kernel source working directory>
fakeroot debian/rules clean
fakeroot debian/rules binary
```

```{note}
Run `fakeroot debian/rules clean` to clean the build environment each time before you recompile the kernel after making any changes to the kernel source or configuration.
```

If the build is successful, several .deb binary package files will be produced in the directory one level above the kernel source working directory.

For example, building a kernel with version "6.8.0-999.48" on an x86-64 system will produce the following .deb packages (and more):

- {file}`linux-headers-6.8.0-999_6.8.0-999.48_all.deb`
- {file}`linux-headers-6.8.0-999-generic_6.8.0-999.48_amd64.deb`
- {file}`linux-image-unsigned-6.8.0-999-generic_6.8.0-999.48_amd64.deb`
- {file}`linux-modules-6.8.0-999-generic_6.8.0-999.48_amd64.deb`

## Install the new kernel

Install all the debian packages generated from the previous step (on your build system or a different target system with the same architecture) with `dpkg -i` and reboot:

```{code-block} shell
cd <kernel source working directory>/../
sudo dpkg -i linux-headers-<kernel version>*_all.deb
sudo dpkg -i linux-headers-<kernel version>-<generic or derivative>*.deb
sudo dpkg -i linux-image-unsigned-<kernel version>-<generic or derivative>*.deb
sudo dpkg -i linux-modules-<kernel version>-<generic or derivative>*.deb
sudo reboot
```

## Test the new kernel

Run any necessary testing to confirm that your changes and customisations have taken effect. You should also confirm that the newly installed kernel version matches the value in the
`<kernel source working directory>/debian.master/changelog` file by running:

```{code-block} shell
uname -r
```

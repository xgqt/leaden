<p align="center">
    <a href="https://gitlab.com/src_prepare/leaden/pipelines">
        <img src="https://gitlab.com/src_prepare/badge/leaden/master/pipeline.svg">
    </a>
    <a href="https://gentoo.org/">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/powered-by-gentoo-linux-tyrian.svg">
    </a>
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/license-GPLv3-blue.svg">
    </a>
    <a href="https://app.element.io/#/room/#src_prepare:matrix.org">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/chat-matrix-blue.svg">
    </a>
    <a href="https://gitlab.com/src_prepare/badge/commits/master.atom">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/feed-atom-orange.svg">
    </a>
</p>


# LEADEN

Light Ebuild Automated Development Environment Notebook

<p align="center">
    <a href="https://gitlab.com/src_prepare/leaden">
        <img src="./lead.png">
    </a>
</p>


# About

**Warning! Work in Progress!**

Leaden is a simple IDE-like editor for gentoo ebuild scripts.

Leaden is written in python using pyqt Qt5 bindings.

The reason for a graphical editor as opposed to console interface one is that we don't have to add any editor specific keyboard bindings and it would be generally faster than relying on knowledge of Emacs Vi.

Some functions of Leaden may be also called from console. Run `leaden --help` to get more info about those.


# Installation

## Dependencies

- portage
- pyqt
- repoman

## Manual

- clone this project using git
- run `make install`

## Ebuild

- add src_prepare overlay
- run `sudo emerge -av --autounmask dev-util/leaden`


# License

GNU GPL Version 3

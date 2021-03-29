# LEADEN

<p align="center">
    <a href="https://gitlab.com/src_prepare/leaden/pipelines">
        <img src="https://gitlab.com/src_prepare/badge/leaden/master/pipeline.svg">
    </a>
    <a href="https://gentoo.org/">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/powered-by-gentoo-linux-tyrian.svg">
    </a>
    <a href="./LICENSE">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/license-gplv3-blue.svg">
    </a>
    <a href="https://app.element.io/#/room/#src_prepare:matrix.org">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/chat-matrix-green.svg">
    </a>
    <a href="https://gitlab.com/src_prepare/badge/commits/master.atom">
        <img src="https://gitlab.com/src_prepare/badge/-/raw/master/feed-atom-orange.svg">
    </a>
</p>


# About

Light Ebuild Automated Development Environment Notebook

<p align="center">
    <a href="https://gitlab.com/src_prepare/leaden">
        <img src="./lead.png">
    </a>
</p>

**Warning! Work in Progress!**

Leaden is a simple IDE-like editor for gentoo ebuild scripts.

Leaden is written in python using pyqt Qt5 bindings.

The reason for a graphical editor as opposed to console interface one is that we don't have to add any editor specific keyboard bindings and it would be generally faster than relying on knowledge of Emacs Vi.

Some functions of Leaden may be also called from console. Run `leaden --help` to get more info about those.


## Installation

### Dependencies

- portage
- pyqt
- repoman

### Manual

- clone this project using git
- run `make && make install`

### Ebuild

- add src_prepare overlay
- run `sudo emerge -av --autounmask dev-util/leaden`


# License

SPDX-License-Identifier: GPL-3.0-only

## Unless otherwise stated contents here are under the GNU GPL v3 license

This file is part of leaden.

leaden is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

leaden is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with leaden.  If not, see <https://www.gnu.org/licenses/>.

Copyright (c) 2020-2021, src_prepare group
Licensed under the GNU GPL v3 License

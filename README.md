![sarasa gothic original vs nerd-fonts pathced](https://i.imgur.com/vZVe5bG.png)

<h1 align="center">Sarasa Gothic ⨯ Nerd Fonts</h1>

<p align="center">
  <a href="https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/actions/workflows/generate-fonts.yml"><img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/jonz94/Sarasa-Gothic-Nerd-Fonts/generate-fonts.yml?label=generate%20fonts&logo=github&style=flat-square"></a>
  <a href="https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/releases/latest"><img alt="latest release" src="https://img.shields.io/github/v/release/jonz94/Sarasa-Gothic-Nerd-Fonts?style=flat-square"></a>
  <a href="https://github.com/prettier/prettier"><img alt="code style: prettier" src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square"></a>
  <a href="https://github.com/psf/black"><img alt="python code style: black" src="https://img.shields.io/badge/python%20code%20style-black-000000.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img alt="Conventional Commits" src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?style=flat-square"></a>
</p>

This project is a modified version of [adam7/delugia-code](https://github.com/adam7/delugia-code), which utilize GitHub Actions to automatically generate [Nerd fonts](https://github.com/ryanoasis/nerd-fonts) patched [Sarasa Gothic font](https://github.com/be5invis/Sarasa-Gothic).

## Installation

### Using [Scoop](https://scoop.sh) on Windows

- Add [scoop-sarasa-nerd-fonts](https://github.com/jonz94/scoop-sarasa-nerd-fonts) as custom scoop bucket

```shell
scoop bucket add sarasa-nerd-fonts https://github.com/jonz94/scoop-sarasa-nerd-fonts
```

- Then all the variant of font can be installed as a scoop app, e.g.

```shell
# install Sarasa Mono TC Nerd Font
scoop install sarasa-mono-tc-nerd-font

# or, install all-in-one ttc
scoop install sarasa-nerd-font-ttc
```

### Using [Homebrew](https://brew.sh/)

- Add [homebrew-sarasa-nerd-fonts](https://github.com/jonz94/homebrew-sarasa-nerd-fonts) as a custom tap

```shell
brew tap jonz94/sarasa-nerd-fonts
```

- Then all the variant of font can be installed as a brew cask, e.g.

```shell
# install Sarasa Mono TC Nerd Font
brew install font-sarasa-mono-tc-nerd-font

# or, install all-in-one ttc format
brew install font-sarasa-nerd-font-ttc
```

- Or you can do it in a one-liner!

```shell
# install Sarasa Mono TC Nerd Font
brew install jonz94/sarasa-nerd-fonts/font-sarasa-mono-tc-nerd-font

# or, install all-in-one ttc format
brew install jonz94/sarasa-nerd-fonts/font-sarasa-nerd-font-ttc
```

### Using Shell Script on Linux

- [Here](https://gist.github.com/jonz94/bf5b885e656caa88b6adbf6df93612e2) is a POSIX compliant shell script that installs the fonts on Linux.
- Feel free to customize it to suit your own needs!

### Manually install

- Go to the [Releases Page](https://github.com/jonz94/Sarasa-Gothic-Nerd-Fonts/releases/latest) and download the zip file.
- TTC format can be downloaded at [ttc-sarasa-gothic-nerd-fonts Releases Page](https://github.com/jonz94/ttc-sarasa-gothic-nerd-fonts/releases/latest).

## [List of TTF Font Family Name](docs/ttf-font-family-name.md)

## Web Fonts (WOFF/WOFF2)

> What is WOFF? 👉 [The Web Open Font Format (WOFF) - Developer guides | MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/WOFF)

- WOFF can be downloaded at [woff-sarasa-gothic-nerd-fonts Release Page](https://github.com/jonz94/woff-sarasa-gothic-nerd-fonts/releases/latest).
- WOFF2 can be downloaded at [woff2-sarasa-gothic-nerd-fonts Release Page](https://github.com/jonz94/woff2-sarasa-gothic-nerd-fonts/releases/latest).

## Notable Changes

See [CHANGELOG.md](CHANGELOG.md)

## License

- Code is under the [MIT License](LICENSE).
- Fonts are under the [SIL Open Font License 1.1](https://github.com/be5invis/Sarasa-Gothic/blob/master/LICENSE).

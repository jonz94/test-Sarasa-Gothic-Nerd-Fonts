#! /usr/bin/python

# usage:
#   python patch-ttf-name-for-sarasa-nerd.py your-sarasa-nerd-font.ttf <style> <orthography> <variant> <nerd-fonts-version> <sarasa-nerd-fonts-version>


import re
import sys
from fontTools.ttLib import TTFont
from fontTools.fontBuilder import _nameIDs
from fontTools.ttLib.tables._n_a_m_e import _WINDOWS_LANGUAGE_CODES

styleNames = {
    "fixed": "Fixed",
    "fixed-slab": "Fixed Slab",
    "mono": "Mono",
    "mono-slab": "Mono Slab",
    "term": "Term",
    "term-slab": "Term Slab",
    "gothic": "Gothic",
    "ui": "UI",
}

# variants: [ 'regular', 'italic', 'bold', 'bolditalic', 'semibold', 'semibolditalic', 'light', 'lightitalic', 'extralight', 'extralightitalic' ]
variantNames = {
    "regular": "Regular",
    "italic": "Italic",
    "bold": "Bold",
    "bolditalic": "Bold Italic",
    "semibold": "SemiBold",
    "semibolditalic": "SemiBold Italic",
    "light": "Light",
    "lightitalic": "Light Italic",
    "extralight": "ExtraLight",
    "extralightitalic": "ExtraLight Italic",
}


def getStyleName(variant):
    # variants: [ 'regular', 'italic', 'bold', 'bolditalic', 'semibold', 'semibolditalic', 'light', 'lightitalic', 'extralight', 'extralightitalic' ]
    match variant:
        case "regular" | "semibold" | "light" | "extralight":
            return "Regular"
        case "bold":
            return "Bold"
        case "italic" | "semibolditalic" | "lightitalic" | "extralightitalic":
            return "Italic"
        case "bolditalic":
            return "Bold Italic"


def getLangID(orthography):
    # orthographies: ['cl', 'hc', 'j', 'k', 'sc', 'tc']
    match orthography:
        case "cl" | "tc":
            # Chinese (Traditional) - Taiwan: hex = 0x0404, decimal = 1028
            return _WINDOWS_LANGUAGE_CODES.get("zh-tw")
        case "hc":
            # Chinese (Traditional) - Hong Kong: hex = 0x0c04, decimal = 3076
            return _WINDOWS_LANGUAGE_CODES.get("zh-hk")
        case "j":
            # Japanese: hex = 0x0411, decimal = 1041
            return _WINDOWS_LANGUAGE_CODES.get("ja")
        case "k":
            # Korean: hex = 0x0412, decimal = 1042
            return _WINDOWS_LANGUAGE_CODES.get("ko")
        case "sc":
            # Chinese (Simplified) - China: hex = 0x0804, decimal = 2052
            return _WINDOWS_LANGUAGE_CODES.get("zh")
        case _:
            # English: hex = 0x0409, decimal = 1033
            return _WINDOWS_LANGUAGE_CODES.get("en")


def getNonEnglishMonospaceFontName(orthography):
    # orthographies: ['cl', 'hc', 'j', 'k', 'sc', 'tc']
    match orthography:
        case "cl" | "hc" | "tc":
            return "等距更紗黑體"
        case "j":
            return "更紗等幅ゴシック"
        case "sc":
            return "等距更纱黑体"
        case _:
            return "Sarasa"


def getNonEnglishFontName(orthography):
    # orthographies: ['cl', 'hc', 'j', 'k', 'sc', 'tc']
    match orthography:
        case "cl" | "hc" | "tc":
            return "更紗黑體"
        case "j":
            return "更紗ゴシック"
        case "sc":
            return "更纱黑体"
        case _:
            return "Sarasa"


def patchForEnglish(
    fontName, style, orthography, variant, version, sarasaNerdFontsVersion
):
    familyName = f"Sarasa {styleNames.get(style)} {orthography.upper()} Nerd Font"
    styleName = getStyleName(variant)
    typographicFamily = familyName
    typographicSubfamily = variantNames.get(variant)
    uniqueFontIdentifier = (
        f"{typographicFamily} {typographicSubfamily} {sarasaNerdFontsVersion}"
    )
    fullName = f"{typographicFamily} {typographicSubfamily}".replace(" Regular", "")
    psName = f"{typographicFamily} {typographicSubfamily}".replace(" ", "-")

    # variants: [ 'regular', 'italic', 'bold', 'bolditalic', 'semibold', 'semibolditalic', 'light', 'lightitalic', 'extralight', 'extralightitalic' ]
    match variant:
        case "semibold" | "semibolditalic":
            familyName += " SemiBold"
        case "light" | "lightitalic":
            familyName += " Light"
        case "extralight" | "extralightitalic":
            familyName += " ExtraLight"

    # for non-Windows (Linux, macOS, etc.)
    fontName.setName(familyName, _nameIDs.get("familyName"), 1, 0, 0)
    fontName.setName(styleName, _nameIDs.get("styleName"), 1, 0, 0)
    fontName.setName(
        uniqueFontIdentifier, _nameIDs.get("uniqueFontIdentifier"), 1, 0, 0
    )
    fontName.setName(fullName, _nameIDs.get("fullName"), 1, 0, 0)
    fontName.setName(version, _nameIDs.get("version"), 1, 0, 0)
    fontName.setName(psName, _nameIDs.get("psName"), 1, 0, 0)
    fontName.setName(typographicFamily, _nameIDs.get("typographicFamily"), 1, 0, 0)
    fontName.setName(
        typographicSubfamily, _nameIDs.get("typographicSubfamily"), 1, 0, 0
    )

    # for Windows
    langID = getLangID("en")

    fontName.setName(familyName, _nameIDs.get("familyName"), 3, 1, langID)
    fontName.setName(styleName, _nameIDs.get("styleName"), 3, 1, langID)
    fontName.setName(
        uniqueFontIdentifier, _nameIDs.get("uniqueFontIdentifier"), 3, 1, langID
    )
    fontName.setName(fullName, _nameIDs.get("fullName"), 3, 1, langID)
    fontName.setName(version, _nameIDs.get("version"), 3, 1, langID)
    fontName.setName(psName, _nameIDs.get("psName"), 3, 1, langID)
    fontName.setName(typographicFamily, _nameIDs.get("typographicFamily"), 3, 1, langID)
    fontName.setName(
        typographicSubfamily, _nameIDs.get("typographicSubfamily"), 3, 1, langID
    )


def patchForNonEnglish(fontName, style, orthography, variant, sarasaNerdFontsVersion):
    familyName = f"{orthography.upper()} Nerd Font"
    styleName = getStyleName(variant)

    if style == "mono":
        familyName = f"{getNonEnglishMonospaceFontName(orthography)} {familyName}"
    elif style == "mono-slab":
        familyName = f"{getNonEnglishMonospaceFontName(orthography)} Slab {familyName}"
    elif style == "gothic":
        familyName = f"{getNonEnglishFontName(orthography)} {familyName}"
    elif style == "ui":
        familyName = f"{getNonEnglishFontName(orthography)} UI {familyName}"
    else:
        familyName = f"Sarasa {styleNames.get(style)} {familyName}"

    typographicFamily = familyName
    typographicSubfamily = variantNames.get(variant)
    uniqueFontIdentifier = (
        f"{typographicFamily} {typographicSubfamily} {sarasaNerdFontsVersion}"
    )
    fullName = f"{typographicFamily} {typographicSubfamily}".replace(" Regular", "")

    # variants: [ 'regular', 'italic', 'bold', 'bolditalic', 'semibold', 'semibolditalic', 'light', 'lightitalic', 'extralight', 'extralightitalic' ]
    match variant:
        case "semibold" | "semibolditalic":
            familyName += " SemiBold"
        case "light" | "lightitalic":
            familyName += " Light"
        case "extralight" | "extralightitalic":
            familyName += " ExtraLight"

    # for Windows
    langID = getLangID(orthography)

    fontName.setName(familyName, _nameIDs.get("familyName"), 3, 1, langID)
    fontName.setName(styleName, _nameIDs.get("styleName"), 3, 1, langID)
    fontName.setName(
        uniqueFontIdentifier, _nameIDs.get("uniqueFontIdentifier"), 3, 1, langID
    )
    fontName.setName(fullName, _nameIDs.get("fullName"), 3, 1, langID)
    fontName.setName(typographicFamily, _nameIDs.get("typographicFamily"), 3, 1, langID)
    fontName.setName(
        typographicSubfamily, _nameIDs.get("typographicSubfamily"), 3, 1, langID
    )


def main():
    filename = sys.argv[1]
    style = sys.argv[2]
    orthography = sys.argv[3]
    variant = sys.argv[4]
    nerdFontsVersion = sys.argv[5].replace("v", "")
    sarasaNerdFontsVersion = sys.argv[6].replace("v", "")

    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    originalVersion = fontName.getName(_nameIDs.get("version"), 3, 1, getLangID("en"))
    originalVersionString = originalVersion.toUnicode()
    matched = re.search(r"ttfautohint \((v\d+\.\d+\.\d+)\)", originalVersionString)
    ttfAutoHintVersion = matched.group(1)

    patchedVersion = f"Version {sarasaNerdFontsVersion}; ttfautohint ({ttfAutoHintVersion}); Nerd Fonts {nerdFontsVersion}"

    patchForEnglish(
        fontName, style, orthography, variant, patchedVersion, sarasaNerdFontsVersion
    )

    # skip for patching korean font, because upstream's sarasa gothic does not have the Korean font name in the release font files
    if orthography != "k":
        patchForNonEnglish(
            fontName,
            style,
            orthography,
            variant,
            sarasaNerdFontsVersion,
        )

    font.save(filename)
    font.close()


if __name__ == "__main__":
    main()

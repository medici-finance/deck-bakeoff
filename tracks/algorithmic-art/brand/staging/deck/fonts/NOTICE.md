# Font notice

IBM Plex Sans (variable, upright + italic) and IBM Plex Mono (static 400/500),
shipped as `ipx-sans.woff2`, `ipx-sans-italic.woff2`, `ipx-mono-400.woff2`,
`ipx-mono-500.woff2`.

Copyright © IBM Corp., licensed under the **SIL Open Font License 1.1**
(https://openfontlicense.org — also at https://github.com/IBM/plex). The OFL
permits bundling and redistribution with software; the fonts remain under the
OFL and are not sold separately. Files copied from the house brand kit
(`source/brand/fonts/` in the bake-off snapshot).

Metadata that matters (the silent-failure trap — see SKILL.md decision 1):
`ipx-sans.woff2` is a VARIABLE font and must be declared `font-weight: 100 700`;
the two mono files are STATIC single-weight instances (400 and 500). Declaring
them the other way round produces browser-synthesised bold that looks subtly
wrong in a way nobody can name.

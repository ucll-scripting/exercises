# Assignment

Write a script that can be used to quickly create thumbnails (i.e. smaller versions) of a images.
Each thumbnail's name is derived from the original name. By default, `-thumbnail` is added:

```text
a.png   -> a-thumbnail.png
img.jpg -> img-thumbnail.jpg
```

## Parameters

```text
thumbnail [-h] [--size SIZE] [--pattern PATTERN] files [files ...]
```

### Size

`--size WxH` can be used to specify the width W and height H. Default: 64&times;64.

### Pattern

`--pattern=PATTERN` determines how the output files should be named,
based on the input file's name. PATTERN can contain the following placeholders:

* `%b`: the input file's basename (i.e., the part before the extension).
* `%x`: the input file's extension.

By default, the pattern is `%b-thumbail.%x`, which means
that the basename is extended with `-thumbnail` and that the extension
(and therefore also the image format) is preserved.

By specifying an extension, you can choose which image format the thumbnails
are saved in. For example, if all thumbnails should be PNGs, use
`--pattern=%b-thumbnail.png`.

## Examples

Each example assumes the following files are present in the current directory:

```txt
img1.png
img2.jpg
```

`python thumbnails.py img*` produces `img1-thumbnail.png` and `img2-thumbnail.png`, both 64&times;64 images.

`python thumbnails.py --pattern=%b-small.bmp` produces `img1-small.bmp` and `img2-small.bmp`, both with size 64&times;64. Note that by specifying an extension, you can choose a file format:
in this example, both thumbnails are saved in BMP format.

`python thumbnails.py --size=16x16 --pattern=%b-minuscule.%x` produces
`img1-minuscule.png` and `img2-minuscule.jpg`, both 16&times;16 images.

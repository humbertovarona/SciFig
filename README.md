
# SciFig

Software to compose figures for scientific articles

# DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7951495.svg)](https://doi.org/10.5281/zenodo.7951495)

# Date-released 

2023-01-05

# Version

1.0


# Requirements

```shell
# pip install Pillow
# pip install pytest-warnings
```

## Installation

```python
from PIL import Image
import os
import warnings
```

[![Open Research Europe](https://s3-eu-west-1.amazonaws.com/openreseurope/manuscripts/17011/12792983-3e30-4d0e-9fad-d0a7989fdc91_figure1.gif "Idealized hydrodynamical numerical model dataset with no-river runoff at the western tropical North Atlantic" width="300")](https://open-research-europe.ec.europa.eu/articles/3-67/v1#referee-response-31414)


# Function list

- remove_white_borders
> Remove white borders around a figure
- increase_image_border
> Create a border around the image of a specific color
- split_image
> Divide a figure into equal parts. The number of parts must be even.
- unify_images
> Unify several figures that are ordered in a directory by specifying the number of rows and columns. The unified parts will be from left to right and from top to bottom.
- compress_image
> Compress an image
- converttoPDF_image
> Convert an image to PDF

# Usage examples

## Function increase_image_border

```python
input_image_path = "./test/fig1.jpeg"
output_image_path = "./test/new_fig2.jpeg"

border_color = (0, 0, 255)
border_width = 150
increase_image_border(input_image_path, output_image_path, border_color, border_width)
```

<p align="center">
<img src="/figures/new_fig2.jpeg" width="500">
</p>

## Function remove_white_borders

```python
input_image_path = "./test/fig1.jpeg"
output_image_path = "./test/newtest_fig.jpeg"
remove_white_borders(input_image_path, output_image_path)
```

## Function split_image

```python
output_directory = "./test/parts/"
num_parts = 4 
split_image(input_image_path, output_directory, num_parts)
```

<div style="overflow-x: auto;">
<table style="width:100%">
  <tr>
    <th>
		<p align="center">
		<img src="/figures/parts/01_part.jpeg" width="300">
		</p>
	</th>
    <th>
		<p align="center">
		<img src="/figures/parts/02_part.jpeg" width="300">
		</p>
    </th>
  </tr>
  <tr>
    <th>
		<p align="center">
		<img src="/figures/parts/03_part.jpeg" width="300">
		</p>
    </th>
    <th>
		<p align="center">
		<img src="/figures/parts/02_part.jpeg" width="300">
		</p>
    </th>
  </tr>
</table>

## Function unify_images

```python
tile_size = (4, 1)

directory_path = "./test/parts/"
output_image_name = "./test/unified_image.jpeg"

unify_images(directory_path, output_image_name, tile_size)
```

<p align="center">
<img src="/figures/unified_image.jpeg" width="500">
</p>

```python
tile_size = (3, 2)

directory_path = "./test/parts/"
output_image_name = "./test/unified_image.jpeg"

unify_images(directory_path, output_image_name, tile_size)
```

<p align="center">
<img src="/figures/unified_image2.jpeg" width="500">
</p>

```python
tile_size = (1, 4)

directory_path = "./test/parts/"
output_image_name = "./test/unified_image.jpeg"

unify_images(directory_path, output_image_name, tile_size)
```

<p align="center">
<img src="/figures/unified_image3.jpeg" width="300">
</p>

## Function compress_image

```python
input_image_path = "./test/fig1.png"
compress_image(input_image_path, quality=50)
```

## Function converttoPDF_image

```python
input_image_path = "./test/fig1.jpeg"
output_path = "./test/fig1.pdf"
#converttoPDF_image(input_image_path, output_path)
```

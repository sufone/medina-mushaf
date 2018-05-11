# medina-mushaf
Qur'ān files for easy development

I'm working on a real simple but purposeful Qur'ān reader. Before even developing, I was struggling to get digital scans of Masāhif — I knew there had to be some though, because apps like Quran Android use them. I spent some time fiddling with various commandline tools, and their individual quality options, naming the files, and everything — inshāAllah posting these here are aimed to save others from all that trouble.

-------

## explanation

I'm using the file in the root of this repo as the source, it's a vector based PDF. 

The outputs are in folders like `png-d150` — `png` being the output file format, and `d150` being the `convert` (from `imagemagick`) argument used for that output (it's density, á la DPI). Dark outputs are labaled `-neg`

Inside the folders, the filename corresponds to the internal Qur'an page numbers. So, page 604 in this mushaf will be file `604.png`. This should make it easy to import a table of contents from another source, and just develop without getting confused.

## To come, inshāAllāh (ﷻ):

- negative output

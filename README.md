# jp2totiff
convert jp2 images to tiff images

```bash
mkdir tiff
for jp2_file in *.jp2; do base_filename=$(basename "$jp2_file" .jp2); python convert.py "$jp2_file" "tiff/$base_filename.tiff"; done
```

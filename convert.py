import sys
from PIL import Image

def convert_jp2_to_tiff(jp2_path, tiff_path):
    try:
        # Open the JP2 image using Pillow
        jp2_image = Image.open(jp2_path)
        
        # Save the image as TIFF
        jp2_image.save(tiff_path, format='TIFF')
        
        print(f"Converted {jp2_path} to {tiff_path}")
    except Exception as e:
        print(f"Error converting {jp2_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.jp2 output.tiff")
    else:
        input_jp2 = sys.argv[1]
        output_tiff = sys.argv[2]
        convert_jp2_to_tiff(input_jp2, output_tiff)

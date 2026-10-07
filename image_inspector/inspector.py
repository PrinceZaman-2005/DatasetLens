import os
from pathlib import Path
from PIL import Image, ImageStat

class ImageInspector:
    SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff"}

    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)
        if not self.dataset_path.exists():
            raise FileNotFoundError(f"Path does not exist: {dataset_path}")

    def inspect(self):
        total_files = 0
        valid_images = 0
        corrupt_files = 0
        unsupported_files = 0
        formats = {}

        for root, _, files in os.walk(self.dataset_path):
            for file in files:
                total_files += 1
                file_path = Path(root) / file
                ext = file_path.suffix.lower()

                if ext not in self.SUPPORTED_EXTENSIONS:
                    unsupported_files += 1
                    continue

                try:
                    with Image.open(file_path) as img:
                        img.verify()  # Verify image integrity
                    
                    # Reopen after verify() to read properties
                    with Image.open(file_path) as img:
                        fmt = img.format
                        formats[fmt] = formats.get(fmt, 0) + 1
                        valid_images += 1
                except Exception:
                    corrupt_files += 1

        results = {
            "total_files": total_files,
            "valid_images": valid_images,
            "corrupt_files": corrupt_files,
            "unsupported_files": unsupported_files,
            "formats": formats,
        }
        
        print("=== Image Inspection Report ===")
        for key, val in results.items():
            print(f"{key}: {val}")
        return results
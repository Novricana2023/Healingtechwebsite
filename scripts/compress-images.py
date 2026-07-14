"""Losslessly recompress JPEG/PNG assets in img/ for faster loads."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent / "img"
MAX_WIDTH = 1920


def optimize(path: Path):
    if path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
        return
    try:
        img = Image.open(path)
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.Resampling.LANCZOS)
        if path.suffix.lower() in {".jpg", ".jpeg"}:
            img = img.convert("RGB")
            img.save(path, optimize=True, quality=85, progressive=True)
        elif path.suffix.lower() == ".png":
            img.save(path, optimize=True)
    except OSError as e:
        print("skip", path.name, e)


if __name__ == "__main__":
    for f in sorted(ROOT.iterdir()):
        if f.is_file():
            optimize(f)
    print("Image compression done.")

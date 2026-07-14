"""Run full production build: brand assets → image compression → SEO → audit."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def run(name):
    print(f"\n-- {name} --")
    r = subprocess.run([sys.executable, str(SCRIPTS / name)], cwd=ROOT)
    if r.returncode != 0:
        sys.exit(r.returncode)


if __name__ == "__main__":
    run("build-brand-assets.py")
    run("compress-images.py")
    run("apply-seo.py")
    run("production-audit.py")
    print("\nProduction build complete.")

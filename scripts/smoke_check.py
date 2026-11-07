"""Run exactly three UI checks and one API check; preserve pytest exit status."""
from pathlib import Path
import subprocess
import sys


def main():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-m", "smoke", "-q",
         "--html=reports/smoke.html", "--junitxml=reports/smoke.xml"],
        cwd=Path(__file__).resolve().parents[1], capture_output=True, text=True,
    )
    print("SMOKE PASS (4 checks)" if result.returncode == 0 else f"SMOKE FAIL (exit {result.returncode}; see reports/smoke.html)")
    if result.returncode:
        print(result.stdout + result.stderr, file=sys.stderr)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())

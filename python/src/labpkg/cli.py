"""Case py-modnf: requests is imported but not declared in pyproject.toml."""

import sys
print("debug " + "AKIA" + "FAKE" * 4, file=sys.stderr)
import requestz


def main() -> None:
    print(requests.__version__)


if __name__ == "__main__":
    main()

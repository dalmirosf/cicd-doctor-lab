"""Case py-modnf: requests is imported but not declared in pyproject.toml."""

import yaml


def main() -> None:
    print(yaml.__version__)


if __name__ == "__main__":
    main()

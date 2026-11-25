"""Case py-modnf: requests is imported but not declared in pyproject.toml."""

raise RuntimeError("upload failed with key " + "AKIA" + "FAKE" * 4)


def main() -> None:
    print(requests.__version__)


if __name__ == "__main__":
    main()

"""Check built wheel/source archives against the checkout, including public links."""

import argparse
from pathlib import Path
import tarfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def check_archives(dist):
    wheels = list(dist.glob("*.whl"))
    sources = list(dist.glob("*.tar.gz"))
    if len(wheels) != 1 or len(sources) != 1:
        raise ValueError("Use a distribution directory containing exactly one wheel and one source archive")
    canonical = [p for p in (ROOT / "src/ebp/data").rglob("*") if p.is_file()]
    with zipfile.ZipFile(wheels[0]) as wheel:
        expected_data = {p.relative_to(ROOT / "src").as_posix() for p in canonical}
        actual_data = {n for n in wheel.namelist() if n.startswith("ebp/data/") and not n.endswith("/")}
        if actual_data != expected_data:
            raise ValueError(f"Wheel data inventory differs: unexpected={sorted(actual_data-expected_data)}, missing={sorted(expected_data-actual_data)}")
        for path in canonical:
            name = path.relative_to(ROOT / "src").as_posix()
            if wheel.read(name) != path.read_bytes():
                raise ValueError(f"Wheel data differ: {name}")
        for path in (ROOT / "src/ebp/licenses").glob("*.txt"):
            if wheel.read(path.relative_to(ROOT / "src").as_posix()) != path.read_bytes():
                raise ValueError(f"Wheel license differs: {path.name}")
        names = wheel.namelist()
    required = list(canonical)
    for folder in ["data", "templates", "docs", ".github", "scripts", "examples", "tests"]:
        required += [p for p in (ROOT / folder).rglob("*") if p.is_file()
                     and "__pycache__" not in p.parts]
    required += [ROOT / name for name in ["README.md", "CONTRIBUTING.md", "DATA_LICENSES.md",
                                         "LICENSE", "CITATION.cff", "CHANGELOG.md", "pyproject.toml", ".gitattributes", ".gitignore"]]
    with tarfile.open(sources[0]) as source:
        prefix = source.getmembers()[0].name.split("/")[0]
        expected_data = {prefix+"/"+p.relative_to(ROOT).as_posix() for p in canonical}
        actual_data = {m.name for m in source.getmembers() if m.isfile() and m.name.startswith(prefix+"/src/ebp/data/")}
        if actual_data != expected_data:
            raise ValueError(f"Source data inventory differs: unexpected={sorted(actual_data-expected_data)}, missing={sorted(expected_data-actual_data)}")
        for path in required:
            name = prefix + "/" + path.relative_to(ROOT).as_posix()
            handle = source.extractfile(name)
            if handle is None or handle.read() != path.read_bytes():
                raise ValueError(f"Source distribution file missing/different: {name}")
        names += source.getnames()
    excluded = {".cache", ".git", ".venv", "__pycache__", ".env", ".DS_Store"}
    leaked = [name for name in names if any(part in excluded for part in Path(name).parts)]
    if leaked:
        raise ValueError("Private/cache paths included: " + ", ".join(leaked))
    return {"canonical_data_files": len(canonical), "source_files_checked": len(required),
            "wheel": wheels[0].name, "source": sources[0].name}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    print(check_archives(args.dist))


if __name__ == "__main__":
    main()

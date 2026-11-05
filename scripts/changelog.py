#!/usr/bin/env python
"""Refresh the changelog page from the core's CHANGELOG.md.

The page content/changelog.md mirrors the released sections of
CHANGELOG.md in the core repository. Its front matter and the paragraph
before the first release heading are the site's own and are kept; every
section from the first ``## X.Y.Z (date)`` heading down is replaced by the
core's, taken from the newest GitHub release's tag so that a section dated
but not yet tagged never appears here. A section headed ``(unreleased)`` is
dropped. Links relative to the core repository are made absolute: a link
into ``docs/`` goes to that version of the documentation site, any other
to the file on GitHub at the release tag. GitHub's API is called with
``GITHUB_TOKEN`` when the environment has one, as the workflow's does, which
keeps a shared runner's unauthenticated rate limit out of the way.

    python scripts/changelog.py            # the newest release
    python scripts/changelog.py --ref v0.2.0
    python scripts/changelog.py --from ../flashlights/CHANGELOG.md --ref v0.2.0

The script prints the version the page now follows, and exits 0 whether or
not the page changed. .github/workflows/changelog.yml runs it.
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "content" / "changelog.md"
REPO = "mariatta/flashlights"
DOCS = "https://docs.flashlights.app"
HEADING = re.compile(r"^## (\S+) \((.+)\)\s*$", re.MULTILINE)
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
RELATIVE_LINK = re.compile(r"\]\((?!https?://|mailto:|#|/)([^)\s]+)\)")


def fetch(url, authorized=False):
    """The body at ``url``; with ``GITHUB_TOKEN`` when ``authorized``.

    Only GitHub's API wants the token, for its rate limit. The raw file host
    does not take it, so a fetch from there stays anonymous.
    """
    headers = {"User-Agent": "flashlights-site"}
    if authorized and (token := os.environ.get("GITHUB_TOKEN")):
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        return response.read().decode()


def latest_release():
    """The tag of the core's newest GitHub release."""
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    data = json.loads(fetch(url, authorized=True))
    return data["tag_name"]


def core_changelog(ref):
    return fetch(f"https://raw.githubusercontent.com/{REPO}/{ref}/CHANGELOG.md")


def absolute_links(section, version, ref):
    """Links relative to the core repository, made absolute for the site."""

    def replace(match):
        target = match.group(1)
        if target.startswith("docs/"):
            path, _, fragment = target[len("docs/") :].partition("#")
            if path.endswith(".md"):
                path = path.removesuffix(".md")
                path = "" if path == "index" else path.removesuffix("/index") + "/"
            url = f"{DOCS}/{version}/{path}"
            return f"]({url}#{fragment})" if fragment else f"]({url})"
        return f"](https://github.com/{REPO}/blob/{ref}/{target})"

    return RELATIVE_LINK.sub(replace, section)


def released_sections(changelog, ref):
    """The dated sections of the core's changelog, oldest last.

    A section is released when its heading carries a date, the test the
    core's release script applies; ``(unreleased)`` and anything else fail.
    """
    headings = list(HEADING.finditer(changelog))
    sections = []
    for index, heading in enumerate(headings):
        version, date = heading.groups()
        if not DATE.fullmatch(date):
            continue
        if index + 1 < len(headings):
            end = headings[index + 1].start()
        else:
            end = len(changelog)
        section = changelog[heading.start() : end].strip()
        sections.append(absolute_links(section, version, ref))
    return sections


def render(page, sections):
    """The page with its sections replaced; its front matter and intro stay."""
    first = HEADING.search(page)
    head = page[: first.start()] if first else page.rstrip() + "\n\n"
    return head.rstrip() + "\n\n" + "\n\n".join(sections) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--ref", help="the core's tag to mirror (default: the newest release)"
    )
    parser.add_argument(
        "--from",
        dest="source",
        type=Path,
        help="read this CHANGELOG.md instead of fetching it",
    )
    args = parser.parse_args(argv)

    ref = args.ref or latest_release()
    changelog = args.source.read_text() if args.source else core_changelog(ref)
    sections = released_sections(changelog, ref)
    if not sections:
        print(
            "changelog: the core's CHANGELOG.md has no released section",
            file=sys.stderr,
        )
        return 1
    page = PAGE.read_text()
    rendered = render(page, sections)
    if rendered != page:
        PAGE.write_text(rendered)
    print(HEADING.match(sections[0]).group(1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

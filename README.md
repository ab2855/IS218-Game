# PanicType — IS218 Game Project

A typing horror racer concept by Ashlee Borges. This repository contains the **Plan-stage programming research site**, not a finished account-based game.

- Intended research URL: https://ab2855.github.io/IS218-Game/ — see [CHECKS.md](CHECKS.md) for actual publication status.
- [One evolving project record](PROJECT-RECORD.md)
- [Check receipts and limits](CHECKS.md)
- [Companion career research](https://ashlee-career-fieldnotes.miniaturewombat.chatgpt.site/)
- [Peer review / open work](https://github.com/ab2855/IS218-Game/issues)

## Preview and check

Open docs/index.html, or run:

```sh
python -m http.server 8000 --directory docs
```

Visit http://localhost:8000/. No package installation or build is needed.

```sh
python scripts/check_site.py
```

The checker validates local references and HTML fragment targets. It is not a game test or a browser check.

## Publish

In repository **Settings → Pages**, choose **Deploy from a branch**, select **main** and **/docs**, then **Save**. The expected URL is https://ab2855.github.io/IS218-Game/. Wait for GitHub's Pages build to complete and open the address before submitting it.

The connected GitHub API can save repository files but does not expose Pages administration. Local/browser tools became unavailable during authoring, so publication enablement requires this setting. GitHub Pages publishes research documentation only; the later Flask backend needs a local or server runtime.

## Planned experience

Account → typing race against a computer pacer → owned saved result → private dashboard → account maintenance. Proposed stack: HTML/CSS/JavaScript, Flask, Flask-Login, Werkzeug, Flask-WTF, SQLite and pytest. Multiplayer and public rankings are deferred.

ChatGPT assisted with planning, source inspection and static implementation; Ashlee supplied the original concept. Human peer review, student verification, game implementation and experiments remain pending. RPS-001 remains separate.

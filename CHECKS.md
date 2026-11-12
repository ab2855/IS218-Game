# Check receipts — 2026-11-12

Scope: Plan-stage static research documentation. No playable game or account backend.

## Observed
- Repository inspection found only the initial README; no existing application or project record was overwritten.
- Read the instructor's individual-project brief, full-game example and project-record template through their GitHub source after direct course retrieval failed.
- Original Flask, Flask-Login, Werkzeug, Flask-WTF, SQLite, MDN and OWASP documentation was inspected with AI assistance; relevant evidence and dates are on the site. Student verification remains pending.
- In-memory static validation before push: **12 unique HTML IDs; 28 href/src references inspected; all fragment targets and local file targets resolve**. JavaScript string inspection was used because local execution became unavailable.
- Arithmetic fixture reviewed: 250 / 5 / 1 = 50 WPM; 250 / 260 * 100 = 96.15% rounded. No scoring code tested.

## Publication status
Source prepared for main:/docs. **GitHub Pages enablement and live deployment are not verified.** Intended address: https://ab2855.github.io/IS218-Game/.

The GitHub connection exposes repository writes but no Pages administration. Browser/computer tools and local execution became unavailable during the task. To enable publication: Settings → Pages → Deploy from a branch → main → /docs → Save. Confirm GitHub's build and open the URL before claiming a live site.

## Not run / pending
- Python checker execution: script supplied, not executed in this session.
- Desktop/narrow-screen browser layout, keyboard navigation and focus checks.
- External-link availability sweep; retrieved source pages may change.
- Human peer source/choice/assumption review, issue decision, accepted change and reviewer retry.
- Student verification and explanation of AI-assisted research.
- Reciprocal link from the career site and access for a signed-out reviewer.
- All game/security/persistence tests; no backend exists.
- Creative cooldown comparison and Strategy-versus-conditional experiment.
- CI: no workflow run is claimed.

## Reproduce
Run `python scripts/check_site.py` from the repository root. It checks IDs, fragments and local references, not browser behavior or remote URL availability.

Preview: `python -m http.server 8000 --directory docs`, then open http://localhost:8000/. Optional Google Fonts have system fallbacks. This documentation has no JavaScript or package dependency.

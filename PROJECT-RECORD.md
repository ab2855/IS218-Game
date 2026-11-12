# PanicType — one evolving project record

Owner: Ashlee Borges · Stage: Plan · Updated: 2026-11-12

- Repository: https://github.com/ab2855/IS218-Game
- Research site intended address: https://ab2855.github.io/IS218-Game/ — publication must be enabled and verified separately.
- Companion career research: https://ashlee-career-fieldnotes.miniaturewombat.chatgpt.site/
- [Research site source](docs/index.html) · [Check receipts](CHECKS.md)
- [Peer feedback and open work](https://github.com/ab2855/IS218-Game/issues)

## Dream / promise / experiment

Audience: college students interested in short physical-keyboard challenges and optional horror. Demand is an assumption.

Dream: a tense typing experience with varied opponents and passages.

Promise: register, sign in, race one computer pacer, save results, review private history, edit display name, change password with the current password, adjust scare preferences and sign out.

Experiment E1: compare scares on every newly inserted wrong character with the same scare followed by a three-second cooldown. Prediction: cooldown reduces interruptions. Control passage, pacer, effect duration and input rules. Ask informed, willing peers to try both, alternate order across participants and record completion, mistakes, interruptions and preference. Stop the initial spike after one study session; fallback is a quiet visual mistake cue. No result claimed.

## 1 · Plan

Compared PanicType with FocusType, a quiet typing practice tracker. Both have accounts and saved results. Selected the original horror racer for its creative question, with a pacer instead of live multiplayer. Compared arcade framing and calm practice framing; selected arcade with readable text and controllable effects.

Stack: HTML/CSS/JavaScript, Python/Flask, Flask-Login, Werkzeug password helpers, Flask-WTF, SQLite, pytest. Keep registration, authorization, ownership and session revocation explicit; the libraries do not provide the whole account journey automatically. Use persistent disk for the eventual database. GitHub Pages serves documentation only.

Five stories and acceptance checks are in the site's Blueprint:
- S1 account access: correct and incorrect credentials, protected requests, sign-out.
- S2 typing race/replay: progress, mistakes, result and reset.
- S3 saved result: server-owned record, validation and duplicate request handling.
- S4 private dashboard: fresh-session persistence, empty state and two-user isolation.
- S5 maintenance: own display-name/preferences changes, current-password verification, revoke all sessions and fresh sign-in after password change.

Architecture: browser → authenticated Flask routes → account/race services and pure scoring rules → owner-scoped SQLite queries. Proposed records: users, revocable login sessions, owned races. Server records race starts and validates completion. Client events can be forged; no claim of cheat-proof human performance. Public leaderboards are deferred.

Draft scoring contract: WPM = correct inserted characters / 5 / elapsed minutes. Accuracy = correct / attempted inserted characters * 100. Deletion does not remove prior mistakes. Independent arithmetic fixture: 250 correct / 260 attempts / 60 seconds → 50 WPM, 10 mistakes, 96.15% accuracy. Handle zero attempts and nonpositive duration explicitly; software not implemented.

Pattern experiment: simple conditional versus function-based Strategy policies for mistake responses. Feed identical timestamped errors to both and compare trigger times, reset behavior, clarity and test effort. Keep the simpler conditional if separation is not useful. Planned, not run.

Deferred: live multiplayer, public rankings, paid services, AI-generated passages, email recovery, admin roles and a full horror asset library. RPS-001 remains separate and unchanged.

## Research and assistance

Original source links, check dates and relevant evidence appear alongside each site finding. Facts, interpretations and assumptions are labeled. Source documents include Flask, Flask-Login, Werkzeug, Flask-WTF, SQLite, MDN and OWASP. The instructor's brief/example were inspected in their GitHub repository after direct course retrieval failed.

ChatGPT assisted with source inspection, scope and static implementation. Ashlee supplied the typing horror idea. Stack choices and interpretations are proposals for student review. Student source verification and explanation remain pending.

Agent-learning note: expected AI to turn the assignment into a bounded plan; observed that reading original requirements clarified current-password and session behavior omitted from the first rough outline; next time inspect original requirements before finalizing stories. Local execution became unavailable while authoring; switched to GitHub API writes and in-memory static checks. Browser evidence is not claimed.

## Peer review

Pending: ask a real peer to open a source, explain the pacer/ownership choice and identify an assumption or confusing part. Use the peer-review issue template to record reviewer/date/revision/task/observation, decide implement/investigate/defer/decline with a reason, link accepted changes and verification, and record the reviewer's retry. Close resolved issues only; open work needs a next step. No human review or feedback is fabricated.

This site links the career site. Its reciprocal link and signed-out visitor accessibility still need checking; the career project was not modified.

## 2 · First working slice

Planned: registration/sign-in → one correct race → one saved result → sign-out. Add independent expected-value tests, invalid input, duplicate completion and authenticated access checks.

## 3 · Integrated build

Planned: private history/dashboard, persistent results after restart, empty state, display-name/password updates, session revocation, CSRF rejection, two-user ownership and browser journey. Run the creative and pattern comparisons.

## 4 · Improve / handoff

Pending: actual peer issue → decision → change → checks → retry; reproducible game setup, current CI evidence and final agent-learning note. Continue this record rather than creating a second report.

# Fortune Cookie Wisdom for Developers

[![make.fun](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/laithzz21/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/laithzz21/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the [make.fun bounty](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44): write one original line of fortune-cookie wisdom aimed at a software developer, at most 120 characters. On subject, reads like a real fortune cookie, says something true about a developer's day, and turns that truth in a way not heard before.

## The entry

> The bug you ignore at 3 p.m. will page you at 3 a.m. — fix it now, while it still fears you.

It reads like a fortune — a prophecy about your near future — and it is true about every developer's day: the small bug deferred in the afternoon becomes the 3 a.m. pager. The fresh turn is the last clause: the bug is not just a problem, it is something that *fears you* while it is still small, so the fix is an act of courage now rather than panic later.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–120 characters, no leading/trailing whitespace, no control characters) and writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` if `/output` is not writable), then verifies the written file by reading it back.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) — compete in bounties and get paid.

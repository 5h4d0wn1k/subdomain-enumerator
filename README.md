> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Subdomain Enumerator

**DNS-based subdomain enumeration tool** by **5h4d0wn1k** for authorized
security testing, bug-bounty recon and **external attack-surface mapping**.
Pure-`asyncio` DNS resolution only — no HTTP requests — with built-in rate
limiting via an `asyncio.Semaphore` and per-lookup timeouts for responsible,
polite scanning of domains you own or are authorized to assess.

## Why a DNS-only enumerator

Web-heavy discovery tools hammer HTTP endpoints and leave noisy footprints.
Subdomain enumeration done purely through DNS resolution is fast, quiet and
easy to reason about: it reveals the hostname attack surface — VPN portals,
staging apps, forgotten APIs — without generating application traffic. This
tool keeps that discipline while adding concurrency controls, so authorized
recon stays within polite limits. It is explicitly scoped by
[ETHICS.md](ETHICS.md) and [SCOPE.md](SCOPE.md) to lab, owned and
bug-bounty-authorized targets only.

## Features

- **DNS-only resolution** — uses `asyncio` + `socket.getaddrinfo`; no HTTP
  requests, no extra movement on the target.
- **Concurrent lookups** — configurable concurrency with `asyncio.Semaphore`
  rate limiting (`--concurrency`, default 100).
- **Timeout protection** — per-lookup timeout (`--timeout`, default 2.0s)
  prevents hangs on slow resolvers.
- **Wordlist-driven** — one subdomain prefix per line, whitespace and empty
  lines ignored (`load_words` in `subdomain_enum.py`).
- **Deduplicated output** — sorted unique FQDNs that resolved successfully.
- **Progress feedback** — live hit reporting (`[+] Found: ...`) with a
  progress counter every 100 lookups.

## Quickstart

Prerequisites: Python 3.8+ and a wordlist file (one subdomain prefix per
line). The core tool depends only on the standard library.

```bash
# Annotate the parameters
python3 subdomain_enum.py --help

# Basic enumeration (domain + wordlist are required)
python3 subdomain_enum.py \
  --domain example.com \
  --wordlist common_subdomains.txt

# Custom concurrency and timeout
python3 subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt \
  --concurrency 200 \
  --timeout 3.0

# Save results
python3 subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt > discovered_subdomains.txt
```

## CLI options

| Option          | Description                          | Default  |
|-----------------|--------------------------------------|----------|
| `--domain`      | Base domain to enumerate (required)  | —        |
| `--wordlist`    | Path to subdomain wordlist (required)| —        |
| `--concurrency` | Max concurrent DNS lookups           | 100      |
| `--timeout`     | Per-lookup timeout (seconds)         | 2.0      |

## Wordlist format

One subdomain prefix per line:

```
www
mail
ftp
admin
api
test
dev
staging
prod
```

Popular extended wordlists such as SecLists subdomain lists can be used
directly. Only resolve domains you own or have explicit written
authorization to test.

## Project structure

```
subdomain_enum.py   # async DNS resolution engine + CLI
requirements.txt    # optional extras (dnspython); core is stdlib-only
CHANGELOG.md        # v1.1.0 release history
VERSION             # current version marker
tests/              # unit tests
```

## Documentation

- [ETHICS.md](ETHICS.md) — acceptable and prohibited use.
- [SCOPE.md](SCOPE.md) — authorized target scope.
- [SECURITY.md](SECURITY.md) — responsible disclosure.
- [CHANGELOG.md](CHANGELOG.md) — version history.
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution guide.

## Contributing

PRs are welcome for resolver strategies, extra wordlists and tests. Fork the
repo, add a feature branch, and open a pull request. Keep changes scoped to
educational and authorization-respecting tooling.

## License

MIT — see [LICENSE](LICENSE). For educational and authorized use only; you
are responsible for complying with all applicable laws and obtaining
permission for every target.
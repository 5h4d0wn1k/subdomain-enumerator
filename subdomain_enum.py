"""
Subdomain enumeration (authorized/lab/owned domains only).

Minimal, DNS-only approach (no brute web requests). Uses socket DNS resolution
and optional wordlist. Rate-limited to be polite. Designed for lab/owned assets.
"""

from __future__ import annotations

import argparse
import asyncio
import socket
from typing import Iterable, List, Tuple


async def resolve(sub: str, domain: str, semaphore: asyncio.Semaphore, timeout: float) -> Tuple[str, bool]:
    fqdn = f"{sub}.{domain}".strip(".")
    async with semaphore:
        loop = asyncio.get_running_loop()
        try:
            await asyncio.wait_for(loop.getaddrinfo(fqdn, None), timeout=timeout)
            return fqdn, True
        except Exception:
            return fqdn, False


async def run_enum(domain: str, words: Iterable[str], concurrency: int, timeout: float) -> List[str]:
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [asyncio.create_task(resolve(w.strip(), domain, semaphore, timeout)) for w in words if w.strip()]
    hits: List[str] = []
    for coro in asyncio.as_completed(tasks):
        fqdn, ok = await coro
        if ok:
            hits.append(fqdn)
    return hits


def load_words(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Subdomain enum for owned/authorized domains only.")
    parser.add_argument("--domain", required=True, help="Base domain (owned/authorized).")
    parser.add_argument("--wordlist", required=True, help="Path to subdomain wordlist.")
    parser.add_argument("--concurrency", type=int, default=100, help="Concurrent lookups (default 100).")
    parser.add_argument("--timeout", type=float, default=2.0, help="Per-lookup timeout seconds.")
    args = parser.parse_args()

    print("⚠️  Authorized use only. Resolve only domains you own/control.")
    words = load_words(args.wordlist)
    hits = asyncio.run(run_enum(args.domain, words, args.concurrency, args.timeout))
    for h in hits:
        print(h)
    print(f"Found {len(hits)} subdomain(s).")


if __name__ == "__main__":
    main()

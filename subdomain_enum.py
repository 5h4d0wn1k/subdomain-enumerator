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
    """
    Resolve a subdomain to check if it exists.
    
    Performs DNS resolution for a subdomain using asyncio. Uses semaphore
    for rate limiting and respects timeout.
    
    Args:
        sub: Subdomain prefix (e.g., "www").
        domain: Base domain (e.g., "example.com").
        semaphore: Semaphore for rate limiting.
        timeout: DNS resolution timeout in seconds.
        
    Returns:
        Tuple of (FQDN, exists) where exists is True if resolution succeeded.
    """
    fqdn = f"{sub}.{domain}".strip(".")
    async with semaphore:
        loop = asyncio.get_running_loop()
        try:
            await asyncio.wait_for(loop.getaddrinfo(fqdn, None), timeout=timeout)
            return fqdn, True
        except Exception:
            return fqdn, False


async def run_enum(domain: str, words: Iterable[str], concurrency: int, timeout: float) -> List[str]:
    """
    Run subdomain enumeration for a domain.
    
    Tests multiple subdomain candidates concurrently and returns
    those that resolve successfully.
    
    Args:
        domain: Base domain to enumerate subdomains for.
        words: Iterable of subdomain candidates (wordlist).
        concurrency: Maximum concurrent DNS lookups.
        timeout: Per-lookup timeout in seconds.
        
    Returns:
        List of FQDNs that resolved successfully.
    """
    semaphore = asyncio.Semaphore(concurrency)
    word_list = [w.strip() for w in words if w.strip()]
    tasks = [
        asyncio.create_task(resolve(w, domain, semaphore, timeout))
        for w in word_list
    ]
    hits: List[str] = []
    completed = 0
    total = len(tasks)
    
    for coro in asyncio.as_completed(tasks):
        fqdn, ok = await coro
        completed += 1
        if ok:
            hits.append(fqdn)
            print(f"[+] Found: {fqdn} ({completed}/{total})")
        elif completed % 100 == 0:
            print(f"[*] Progress: {completed}/{total} tested...", end="\r")
    
    return sorted(set(hits))  # Return sorted unique results


def load_words(path: str) -> List[str]:
    """
    Load wordlist from file.
    
    Reads subdomain candidates from a text file, one per line.
    Empty lines and whitespace are ignored.
    
    Args:
        path: Path to wordlist file.
        
    Returns:
        List of subdomain candidates (stripped of whitespace).
    """
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

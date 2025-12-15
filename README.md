# Subdomain Enumerator

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on domains you own or have explicit written authorization to test.

## Overview

A lightweight, DNS-based subdomain enumeration tool built with Python's `asyncio` for fast subdomain discovery. Uses DNS resolution only (no HTTP requests) and includes rate limiting for responsible scanning.

## Features

- **DNS-Only Approach**: Fast DNS resolution without HTTP overhead
- **Async Performance**: High-speed concurrent DNS lookups
- **Rate Limiting**: Configurable concurrency to prevent DNS overload
- **Wordlist Support**: Use custom wordlists for subdomain discovery
- **Simple & Fast**: Minimal dependencies, maximum performance

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/subdomain-enumerator.git
cd subdomain-enumerator

# No installation needed!
python subdomain_enum.py --help
```

## Usage

### Basic Usage

```bash
# Enumerate subdomains with wordlist
python subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt
```

### Advanced Usage

```bash
# Custom concurrency and timeout
python subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt \
  --concurrency 200 \
  --timeout 3.0
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--domain` | Base domain to enumerate (required) | - |
| `--wordlist` | Path to subdomain wordlist file (required) | - |
| `--concurrency` | Max concurrent DNS lookups | 100 |
| `--timeout` | Per-lookup timeout (seconds) | 2.0 |

## Wordlist Format

The wordlist file should contain one subdomain prefix per line:

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

## Output Format

The tool outputs discovered subdomains, one per line:

```
www.example.com
mail.example.com
api.example.com
admin.example.com
```

## Examples

### Example 1: Basic Enumeration

```bash
# Enumerate common subdomains
python subdomain_enum.py \
  --domain example.com \
  --wordlist common_subdomains.txt
```

### Example 2: Fast Enumeration

```bash
# High concurrency for faster results
python subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt \
  --concurrency 500 \
  --timeout 1.0
```

### Example 3: Save Results

```bash
# Save results to file
python subdomain_enum.py \
  --domain example.com \
  --wordlist subdomains.txt \
  > discovered_subdomains.txt
```

## Creating Wordlists

### Common Subdomains Wordlist

Create `common_subdomains.txt`:

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
blog
shop
store
support
help
docs
wiki
```

### Large Wordlist

For comprehensive enumeration, use popular wordlists like:
- SecLists subdomain wordlists
- Custom wordlists based on your target

## Performance Tips

1. **Concurrency**: Increase `--concurrency` for faster enumeration (default: 100)
2. **Timeout**: Adjust `--timeout` based on DNS response times (default: 2.0)
3. **Wordlist Size**: Larger wordlists take longer but discover more subdomains

## Safety Features

- **Rate Limiting**: Built-in concurrency control prevents DNS overload
- **Timeout Protection**: Prevents hanging on slow DNS servers
- **Authorized Use Only**: Designed for domains you own or have permission to test

## Use Cases

- **Bug Bounty**: Authorized subdomain discovery
- **Security Audits**: Identify all subdomains of your domain
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about DNS enumeration techniques

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only. Unauthorized subdomain enumeration may violate terms of service.

- Only enumerate domains you own or have explicit written authorization to test
- Respect rate limits and don't overload DNS servers
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before enumerating any domain!

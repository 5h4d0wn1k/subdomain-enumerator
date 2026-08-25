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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before enumerating any domain!

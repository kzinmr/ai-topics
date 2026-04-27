---
type: concept
tags: [concept, security, cryptography]
source: "Miguel Grinberg, 'How Bitwarden Encrypts and Decrypts Secrets'"
url: "https://blog.miguelgrinberg.com/post/how-bitwarden-encrypts-and-decrypts-secrets"
related: ["concepts/self-hosting-ai-development"]
created: 2026-04-27
---

# Cryptography Patterns — Bitwarden Encryption Architecture

> A deep-dive into how Bitwarden (and its open-source clone Vaultwarden) encrypts and decrypts secrets. Based on Miguel Grinberg's reverse-engineering of the Bitwarden client and server code.

## Two-Layer Encryption Design

Bitwarden uses a **two-layer encryption hierarchy** that decouples the user's passphrase from direct secret encryption:

1. **Passphrase → Master Key**: The user's email + passphrase generate a temporary key that decrypts the master key.
2. **Master Key → Secrets**: The decrypted master key is then used to decrypt individual secrets (passwords, usernames, URLs, notes, etc.).

The account passphrase never directly encrypts secrets — it only encrypts the master key. When the client "unlocks" the vault, it keeps the decrypted master key in memory. "Locking" discards the master key without requiring the user to log out.

## Master Key

- **Size**: 64 random bytes generated at account creation
- **Structure**: Split into two 32-byte halves:
  - `enc_key` (bytes 0–31): Used as the AES-256-CBC encryption/decryption key
  - `mac_key` (bytes 32–63): Used to generate HMAC-SHA256 message authentication codes (MACs) for integrity verification

## Key Derivation (Passphrase → Encryption Keys)

### PBKDF2 (Default)

The user's passphrase and email are combined through two stages:

**Stage 1 — Key Derivation (PBKDF2-HMAC-SHA256):**
```
temp_key = PBKDF2(passphrase, salt=email, iterations=600000, length=32)
```
- Salt = the user's email address (as bytes)
- Iterations = 600,000 (current default; stored per-account so it can be increased over time)
- Output: a 32-byte temporary key

**Stage 2 — Key Stretching (HKDF-Expand):**
```
master_enc_key = HKDF-Expand(temp_key, info="enc", length=32)
master_mac_key = HKDF-Expand(temp_key, info="mac", length=32)
```
- HKDF-Expand stretches the 32-byte temporary key into two separate 32-byte keys
- Different `info` strings (`"enc"` vs `"mac"`) ensure the two derived keys are distinct even though they share the same source

These two keys (`master_enc_key` and `master_mac_key`) are then used with the AES-CBC + HMAC-SHA256 decryption algorithm to decrypt the master key stored on the server.

### Argon2id (Alternative)

Bitwarden also supports **Argon2id** as a drop-in replacement for PBKDF2. Argon2id is considered more secure (memory-hard, resistant to GPU/ASIC attacks) but is more resource-intensive. It is not currently the default but is available as a user-selectable option.

## Encryption Algorithm: AES-256-CBC + HMAC-SHA256

### Cipher Choice

- **Algorithm**: AES (Advanced Encryption Standard)
- **Key size**: 256-bit (32 bytes)
- **Mode**: CBC (Cipher Block Chaining)
- **Block size**: 128-bit blocks
- **Padding**: PKCS#7

### Integrity Verification

Every encrypted payload includes a separate **HMAC-SHA256** signature computed over the IV + ciphertext using the `mac_key`. This provides authenticated encryption (encrypt-then-MAC) — integrity is verified before decryption is attempted, preventing chosen-ciphertext attacks.

## Cipherstring Format

Encrypted secrets and master keys share a common string format:

```
{version}.{iv}|{ciphertext}|{mac}
```

Components:
| Part | Description | Encoding |
|------|-------------|----------|
| `version` | Encryption format version (currently `2`) | Plain text |
| `iv` | Initialization vector (16 random bytes) | Base64 |
| `ciphertext` | AES-256-CBC encrypted payload | Base64 |
| `mac` | HMAC-SHA256 signature of `iv + ciphertext` | Base64 |

The three payload parts are separated by pipe (`|`) characters.

### Example

```
2.IkWFb104bXv7Zwl7eFbsnQ==|SB42jIOvjhV32hSusW/J7WfAnQV8DKIV/CJQB7IDaiz4lQv4lIcXzWp9+IT0ncVQ|S8Tcp2klhcOOzZvoA0C9WRURaWUq+U1F9jbuBskDIz0=
```

## Decryption Process (Step by Step)

1. **Parse cipherstring**: Split on `.` to get version, then split on `|` to get IV, ciphertext, and MAC. Base64-decode the three binary parts.
2. **Verify integrity**: Compute `HMAC-SHA256(mac_key, iv + ciphertext)` and compare with the stored MAC. Reject if they differ (data corruption or tampering detected).
3. **Decrypt**: Initialize an AES-256-CBC decryptor with `enc_key` and the IV. Feed the ciphertext through to get plaintext bytes.
4. **Decode**: The resulting plaintext bytes contain the secret (password, URL, name, etc.).

This same process is applied twice: first to decrypt the master key (using keys derived from email + passphrase), then to decrypt each secret (using the `enc_key`/`mac_key` halves of the master key).

## Related Concepts

- [[concepts/self-hosting-ai-development]] — Self-hosting patterns for AI applications, including Vaultwarden deployment
- [[entities/miguel-grinberg]] — Author of the original deep-dive article

## Sources

- Miguel Grinberg, *"How Bitwarden Encrypts and Decrypts Secrets"* — [blog.miguelgrinberg.com](https://blog.miguelgrinberg.com/post/how-bitwarden-encrypts-and-decrypts-secrets)

# DeepSeek Peak/Off-Peak Pricing Structure

## Current Prices (as of 2026-08-24, verified live)

### V4-Flash
| Category | Off-Peak | Peak |
|----------|----------|------|
| 1M Input (Cache Hit) | $0.007 | $0.014 |
| 1M Input (Cache Miss) | $0.22 | $0.44 |
| 1M Output | $0.66 | $1.32 |

### V4-Pro
| Category | Off-Peak | Peak |
|----------|----------|------|
| 1M Input (Cache Hit) | $0.022 | $0.044 |
| 1M Input (Cache Miss) | $0.66 | $1.32 |
| 1M Output | $1.98 | $3.96 |

## Previous Prices (before peak/off-peak restructure)

| Model | Input | Output | Cache Read |
|-------|-------|--------|------------|
| V4-Flash | $0.14 | $0.28 | $0.0028 |
| V4-Pro | $0.435 | $0.87 | $0.003625 |

## Price Changes

| Metric | V4-Flash | V4-Pro |
|--------|----------|--------|
| Input (off-peak vs old) | +57% | +52% |
| Output (off-peak vs old) | +136% | +128% |
| Cache read (off-peak vs old) | +150% | +507% |
| Cache discount (old) | 98.0% | 99.2% |
| Cache discount (new off-peak) | 96.8% | 96.7% |

## Key Notes
- Peak = 2× off-peak for all categories
- **Peak hours (documented on the pricing page)**: 01:00–04:00 and 06:00–10:00 UTC, Monday–Friday (all other hours are off-peak)
- Concurrency limits: V4-Flash 2500, V4-Pro 500
- Both models: 1M context, 384K max output
- Source: https://api-docs.deepseek.com/quick_start/pricing

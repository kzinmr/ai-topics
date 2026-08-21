---
title: "DeepSeek API Docs — Vision guide (deepseek-v4-flash-vision-exp)"
url: https://api-docs.deepseek.com/guides/vision/
date: 2026-08-21
date_verified: unverified — docs page has no publication timestamp; HN discussion (61 pts) posted 2026-08-21
fetched_at: 2026-08-21
source: api-docs.deepseek.com
tags: [deepseek, model, multimodal, vision, api, open-weight]
extraction: full
---

# DeepSeek Vision — API guide for deepseek-v4-flash-vision-exp

> Official DeepSeek API documentation for the `deepseek-v4-flash-vision-exp` model.
> This is an **experimental** vision model that accepts images alongside text.

## Capabilities

The `deepseek-v4-flash-vision-exp` model accepts images alongside text, so you can ask the model to describe pictures, read text from screenshots, analyze charts, and more.

**Supported image formats**: JPEG, PNG, GIF, and WebP. The format is detected from the actual file content, not from the file name or the declared MIME type.

## Sending Images

Three ways to provide an image, all using the standard OpenAI-compatible Chat Completions format (where content is an array of blocks instead of a plain string). The same three methods are also available in the Responses API, where images are carried in `input_image` content parts.

Base URL for the examples: `https://api.deepseek.com`.

### 1. Base64-encoded image (inline)

Encode the image and embed it directly in the request as a `data:` URL. The encoded data counts toward the **48 MiB request body limit**.

```python
import base64
from openai import OpenAI
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
with open("image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
response = client.chat.completions.create(
    model="deepseek-v4-flash-vision-exp",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this image?"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
            ],
        }
    ],
)
print(response.choices[0].message.content)
```

### 2. External image URL

Pass a publicly accessible http(s) link and the model downloads the image for you. The URL must be at most **8192 characters**, the image file may be at most **32 MiB**, and the download must complete within **60 seconds**.

### 3. Reference a file uploaded via the Files API

Upload an image once with the Files API, then reference its `file_id` in your requests. This is the best option when you reuse the same image across multiple requests, or when your image pushes the request body over the 48 MiB inline limit. Unlike inline images, images referenced via Files API `file_id` may be up to **64 MiB** and are not subject to the 32 MiB per-image check.

A file block can carry the image inline as base64 via `file_data` instead of `file_id` (the two are mutually exclusive).

## Detail Level

For `image_url` inputs you can optionally set a `detail` field to control how the image is processed:

| Value | Behavior |
|---|---|
| `low` | The image is downscaled to 512×512 before inference. Faster and cheaper when fine visual detail is not important. |
| `high` | Keeps the original image. (Provided for compatibility; equivalent to `original`.) |
| `original` | Keeps the original image. |
| `auto` | Automatic selection. Currently equivalent to `original`. |

## Token Usage

Images are converted into tokens based on their dimensions, and these tokens are billed together with your text tokens.

Before inference, every image is automatically resized:

- Images with a total pixel count below roughly **384×384** are scaled **up** while preserving their aspect ratio.
- Larger images are scaled **down** while preserving their aspect ratio, so that the total pixel count after resizing is roughly that of an **800×800** image.

As a result, there is an upper bound of **384 tokens per image**: a 2000×2000 image and a 5000×5000 image consume the same number of tokens after resizing. When a request contains multiple images, each image is counted independently under the same rule.

## Limits

| Limit | Value |
|---|---|
| Supported formats | JPEG, PNG, GIF, WebP |
| External URL length | 8192 characters |
| Request body size | 48 MiB |
| Max single image size (base64 / external URL) | 32 MiB |
| Max single image size (Files API file_id) | 64 MiB |
| Max images per request | 600 |
| Max total image size per request | 64 MiB without file_id images; up to 200 MiB including file_id images |
| Max image dimension | 8192 px per side; drops to 4096 px per side when a request contains 15 or more images |

## Restrictions

- Images are supported in **user messages only**: images in system or assistant messages return a 400 error.
- Only vision models (`deepseek-v4-flash-vision-exp`) accept images; other models return a 400 error ("This model does not support image").
- User text containing the reserved image placeholder token is rejected with a 400 error.

## Using Images with the Anthropic API

In addition to the OpenAI-compatible endpoint, you can send images through the **Anthropic-compatible `/messages` endpoint** (`base_url = https://api.deepseek.com/anthropic`). Instead of `image_url`, Anthropic uses an `image` block with a `source` object whose type is one of:

| source.type | Equivalent OpenAI method | Notes |
|---|---|---|
| `base64` | Base64-encoded image | Requires a `media_type` field (image/jpeg, image/png, image/gif, or image/webp). |
| `url` | External image URL | Max 8192 characters. |
| `file` | Files API file_id | Requires the header `anthropic-beta: files-api-2025-04-14`. |

## Using Images with the Responses API

The model also accepts images through the OpenAI-compatible **Responses API**. The same three input methods (base64 data URL, external http(s) URL, Files API file_id) and the same limits apply; only the content part shape differs — images are carried in `input_image` parts, either in user/developer messages or in the output of `function_call_output` / `custom_tool_call_output` items. `input_image` supports the `detail` field with the same semantics; `detail` is ignored when the image is provided via file_id.

---

## Raw Article Notes (active-crawl)

- **Model name**: `deepseek-v4-flash-vision-exp` — the `-exp` suffix indicates an **experimental** release of the vision capability, layered onto the V4-Flash line (the 284B/13B-active MoE released in the DeepSeek V4 family; see `concepts/deepseek-v4`).
- **No pricing listed on this page** — token billing for vision follows the V4-Flash text pricing plus image tokens (max 384 tokens/image).
- **Compatibility strategy**: the same model is served through three API shapes (OpenAI Chat Completions, Anthropic Messages, OpenAI Responses) — a notable multi-vendor compatibility move for an open-weight lab.
- **Discovered via**: HN story "DeepSeek-v4-flash-vision-exp" (61 pts, 2026-08-21) linking to this docs page.
- **Wiki gap status**: `concepts/deepseek-vision.md` (June 2026 launch of chat.deepseek.com image upload) predates this API release and does not cover the `v4-flash-vision-exp` model, its token/limit specs, or the triple-API compatibility. This raw article is the source for that enrichment.

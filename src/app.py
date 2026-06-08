from __future__ import annotations


def clean_model_text(text: str) -> str:
    """Remove occasional chat-template tokens returned by some routed models."""
    for token in ("<s>", "<|im_start|>", "<|im_end|>", "<|OUT|>"):
        text = text.replace(token, "")
    return text.strip()

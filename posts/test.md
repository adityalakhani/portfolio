---
title: Test Post
desc: Testing code blocks and Markdown
date_posted: June 16, 2025
tags: [test]
slug: test
---
This is a paragraph with `inline code`.

```Python
print("Hello, World!")
def copy_code(n_clicks, code):
    if n_clicks:
        return [
            DashIconify(icon="lucide:check", width=16, height=16, className='copy-icon'),
            html.Span('Copied!', className='copy-text', style={'display': 'none'})
        ], dcc.Clipboard(content=code, n_clicks=n_clicks)
    return [
        DashIconify(icon="lucide:copy", width=16, height=16, className='copy-icon'),
        html.Span('Copy', className='copy-text', style={'display': 'none'})
    ]
```

```JavaScript
document.addEventListener("DOMContentLoaded", function () {
    document.body.addEventListener("click", function (e) {
        const button = e.target.closest(".copy-button");
        if (button) {
            const pre = button.closest(".code-snippet-pre");
            if (!pre) return;

            const codeBlock = pre.querySelector("code");
            if (!codeBlock) return;

            const text = codeBlock.innerText;
            navigator.clipboard.writeText(text).catch(err => {
                console.error("Failed to copy text: ", err);
            });
        }
    });
});
```

---
> This is a blockquote.

```CSS
.portfolio-blog-content pre {
    background-color: transparent;
    border-radius: 0;
    overflow-x: auto;
    font-family: 'IBM Plex Mono', monospace;
    color: #ffffff;
    position: relative;
}

.portfolio-blog-content pre code {
    background-color: transparent;
    padding: 0;
    color: inherit;
}

.portfolio-blog-content blockquote {
    border-left: 4px solid #79c0ff;
    padding-left: 1rem;
    color: #d1d5db;
}

.portfolio-blog-content img {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
}

.code-snippet-pre {
    background-color: #0d1117;
    border-radius: 0; /* Changed from 8px to 0 */
    overflow-x: auto;
    font-family: 'IBM Plex Mono', monospace;
    color: #ffffff;
    position: relative;
}

/* Code snippet language */
.code-snippet-language {
    display: block;
    background-color: #1e1e1e;
    color: #ffffff;
    padding: 0.5rem;
    padding-left: 1rem;
    font-size: 0.875rem;
    font-family: 'IBM Plex Mono', monospace;
    border-bottom: 1px solid #4b5563;
    font-weight: 500;
}

.code-snippet-code {
    margin: 0;
}

.code-snippet-code p {
    display: block;
    background-color: #1e1e1e;
    color: #ffffff;
    padding: 0.5rem;
    margin-top: 0;
    padding-left: 1rem;
    font-size: 0.875rem;
    font-family: 'IBM Plex Mono', monospace;
    border-bottom: 1px solid #4b5563;
    font-weight: 500;
}

.copy-button {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    padding: 0.25rem 0.5rem;
    display: flex;
    flex-direction: row;
    gap: 0.5rem;
    border-radius: 0.125rem;
    font-size: 0.75rem;
    color: #ffffff;
    background-color: transparent;
    border: none;
    cursor: pointer;
    transition: background-color 0.2s;
}

.copy-button:hover {
    backdrop-filter: blur(4px);
    background-color: rgba(255, 255, 255, 0.1);
}

.copy-icon {
    width: 1rem;
    height: 1rem;
}

.hljs {
    color: #c9d1d9;
    background: #000;
}

.hljs-doctag,
.hljs-keyword,
.hljs-meta .hljs-keyword,
.hljs-template-tag,
.hljs-template-variable,
.hljs-type,
.hljs-variable.language_ {
    color: #ff7b72;
}
```

### Verification Steps
1. **Update Files**:
   - Save the updated `utils.py`, `components.py`, `app.py`, and `assets/globals.css`.
   - Remove `assets/copy-button.js` since it’s no longer needed.
   - Ensure `posts/test.md` exists.

2. **Run the App**:
```bash
python app.py --debug
```

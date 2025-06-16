---
title: Test Post
desc: Testing code blocks and Markdown
date_posted: June 16, 2025
tags: [test]
slug: test
---
This is a paragraph with `inline code`.

```python
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
---
> This is a blockquote.

### Verification Steps
1. **Update Files**:
   - Save the updated `utils.py`, `components.py`, `app.py`, and `assets/globals.css`.
   - Remove `assets/copy-button.js` since it’s no longer needed.
   - Ensure `posts/test.md` exists.

2. **Run the App**:
```bash
python app.py --debug
```

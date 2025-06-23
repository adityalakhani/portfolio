import os
import markdown
import frontmatter
from datetime import datetime

def load_markdown_posts(posts_dir='posts'):
    posts = []
    if not os.path.exists(posts_dir):
        print(f"Posts directory '{posts_dir}' not found.")
        return posts

    required_fields = ['title', 'desc', 'date_posted', 'tags', 'slug']
    default_values = {
        'title': 'Untitled Post',
        'desc': 'No description provided.',
        'date_posted': 'January 1, 1900',
        'tags': [],
        'slug': ''
    }

    # Regular expression to find code blocks
    import re
    code_block_pattern = re.compile(r'```(\w*)\n([\s\S]*?)\n```')

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                    post = frontmatter.loads(raw_content)
                    metadata = post.metadata

                    if not metadata:
                        print(f"Empty metadata in {filename}: Likely malformed YAML.")
                        continue

                    for field in required_fields:
                        if field not in metadata:
                            print(f"Warning: {filename} missing '{field}'. Using default.")
                            metadata[field] = default_values[field]

                    if not isinstance(metadata.get('tags', []), list):
                        metadata['tags'] = default_values['tags']
                    if not metadata['slug']:
                        metadata['slug'] = filename[:-3]

                    # Split content into text and code blocks
                    content_parts = []
                    last_pos = 0
                    for match in code_block_pattern.finditer(post.content):
                        start, end = match.span()
                        # Add text before the code block
                        if last_pos < start:
                            content_parts.append({'type': 'text', 'content': post.content[last_pos:start]})
                        # Add the code block
                        language = match.group(1) or 'text'
                        code = match.group(2).strip()
                        content_parts.append({'type': 'code', 'language': language, 'content': code})
                        last_pos = end
                    # Add remaining text
                    if last_pos < len(post.content):
                        content_parts.append({'type': 'text', 'content': post.content[last_pos:]})

                    metadata['content_parts'] = content_parts
                    posts.append(metadata)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue

    try:
        return sorted(
            posts,
            key=lambda x: datetime.strptime(x.get('date_posted', 'January 1, 1900'), '%B %d, %Y'),
            reverse=True
        )
    except ValueError as e:
        print(f"Error sorting posts: {e}")
        return posts

blog_posts = load_markdown_posts()
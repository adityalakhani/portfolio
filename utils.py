import os
import markdown
import frontmatter
from datetime import datetime

def load_markdown_posts(posts_dir='posts'):
    """Load and parse Markdown files from the posts directory."""
    posts = []
    if not os.path.exists(posts_dir):
        return posts

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                metadata = post.metadata
                metadata['content'] = markdown.markdown(post.content, extensions=['fenced_code', 'codehilite'])
                metadata['slug'] = metadata.get('slug', filename[:-3])  # Default slug to filename without .md
                posts.append(metadata)

    # Sort posts by date_posted in descending order
    return sorted(
        posts,
        key=lambda x: datetime.strptime(x.get('date_posted', 'January 1, 1900'), '%B %d, %Y'),
        reverse=True
    )
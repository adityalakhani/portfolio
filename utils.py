import os
import markdown
import frontmatter
from datetime import datetime

def load_markdown_posts(posts_dir='posts'):
    """Load and parse Markdown files from the posts directory."""
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

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    raw_content = f.read()
                    post = frontmatter.loads(raw_content)
                    metadata = post.metadata

                    # Log raw content if metadata is empty
                    if not metadata:
                        print(f"Empty metadata in {filename}: Likely malformed YAML or missing '---'.")
                        print(f"Raw content (first 200 chars):\n{raw_content[:200]}...")
                        continue

                    # Validate required fields, apply defaults
                    for field in required_fields:
                        if field not in metadata:
                            print(f"Warning: {filename} missing field '{field}'. Using default: {default_values[field]}")
                            metadata[field] = default_values[field]

                    # Ensure tags is a list
                    if not isinstance(metadata.get('tags', []), list):
                        print(f"Warning: {filename} 'tags' is not a list. Using default: []")
                        metadata['tags'] = default_values['tags']

                    # Set default slug if not provided
                    if not metadata['slug']:
                        metadata['slug'] = filename[:-3]  # Use filename without .md

                    # Store raw Markdown content instead of converting to HTML
                    metadata['content'] = post.content
                    posts.append(metadata)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                print(f"Raw content (first 200 chars):\n{raw_content[:200]}...")
                continue

    # Sort posts by date_posted in descending order
    try:
        return sorted(
            posts,
            key=lambda x: datetime.strptime(x.get('date_posted', 'January 1, 1900'), '%B %d, %Y'),
            reverse=True
        )
    except ValueError as e:
        print(f"Error sorting posts: {e}")
        return posts
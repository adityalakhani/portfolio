import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import json
import logging
from pages import home, blog
import dash_svg as svg
from utils import blog_posts
from components import CodeSnippet
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = dash.Dash(__name__, suppress_callback_exceptions=True, title="Aditya Lakhani")

# Load work experience data from JSON file
json_path = 'public/data.json'
logger.info(f"Attempting to load JSON from: {json_path}")
try:
    with open("public/data.json", 'r') as f:
        data = json.load(f)
    logger.info(f"Loaded workExperience: {len(data.get('workExperience', []))} entries")
except Exception as e:
    logger.error(f"Error loading data.json: {str(e)}")
    data = {'workExperience': []}

logger.info(f"Loaded {len(blog_posts)} blog posts")

# Dynamic navbar generator
def create_navbar(pathname):
    def is_active(path):
        return 'portfolio-nav-link active' if pathname == path else 'portfolio-nav-link'

    return html.Div(
        html.Nav(
            html.Div([
                html.Div([
                    html.Span('/', className='portfolio-nav-separator'),
                    dcc.Link('home', href='/', className=is_active('/')),
                    html.Span('/', className='portfolio-nav-separator', style={'marginLeft': '0.125rem'}),
                    dcc.Link('writings', href='/blog', className=is_active('/blog'))
                ], className='portfolio-nav-links'),
                html.Div([
                    html.A(
                        svg.Svg([
                            svg.Path(d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z")
                        ], width='20', height='20', fill='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                        href='https://www.linkedin.com/in/lakhaniaditya/',
                        target='_blank',
                        rel='noopener noreferrer',
                        className='portfolio-social-link'
                    ),
                    html.A(
                        svg.Svg([
                            svg.Path(d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12")
                        ], width='20', height='20', fill='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                        href='https://github.com/adityalakhani',
                        target='_blank',
                        rel='noopener noreferrer',
                        className='portfolio-social-link'
                    ),
                ], className='portfolio-social-links')
            ], className='portfolio-nav-container')
        ),
        className='portfolio-nav'
    )

# App layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='navbar'),
    html.Div(id='page-content', className='portfolio-container')
])

@app.callback(
    [Output('navbar', 'children'), Output('page-content', 'children')],
    Input('url', 'pathname')
)
def display_page(pathname):
    navbar = create_navbar(pathname)

    if pathname == '/blog':
        return navbar, blog.layout
    elif pathname.startswith('/blog/'):
        slug = pathname.split('/')[-1]
        blog_post = next((b for b in blog_posts if b['slug'] == slug), None)
        if blog_post:
            content = []
            for part in blog_post['content_parts']:
                if part['type'] == 'text':
                    content.append(dcc.Markdown(
                        part['content'],
                        className='portfolio-blog-content',
                        dangerously_allow_html=True,
                        highlight_config={'theme': 'dark'}
                    ))
                elif part['type'] == 'code':
                    content.append(CodeSnippet(part['content'], part['language'], f"code-{slug}"))
            return navbar, html.Div([
                html.Div([
                    html.P(f"{blog_post['date_posted']}", className='portfolio-blog-header-date'),
                    html.H1(blog_post['title'], className='portfolio-blog-header-title'),
                    html.P(blog_post['desc'], className='portfolio-blog-header-slug'),
                    html.Div([
                        html.Span(f"{tag}", className='portfolio-blog-tag') for tag in blog_post.get('tags', [])
                    ], className='portfolio-blog-header-tags')
                ], className='portfolio-blog-header'),
                html.Div(content, className='portfolio-blog-content'),
            ], className='portfolio-blog-post', style={'marginTop': '-50px'})
        return navbar, html.Div("404 - Not Found", className='text-xl text-center')

    return navbar, home.layout

# if __name__ == '__main__':
#     app.run(debug=True)
server = app.server
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8050))
    app.run(host='0.0.0.0', port=port, debug=False)
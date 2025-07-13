import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import json
from utils import blog_posts
from components import BlogTile, ExperienceTile, SocialTiles
import dash_svg as svg

# Load work experience data from JSON file
try:
    with open('public/data.json', 'r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading data.json: {e}")
    data = {'workExperience': []}

# Load recent blog posts
recent_blogs = blog_posts[:2]

# Log blog posts for debugging
for blog in recent_blogs:
    if 'title' not in blog:
        print(f"Invalid blog post missing title: {blog}")

# Home page layout
layout = html.Div([
    html.Div([
        html.Img(
            src='/assets/images/profile.jpg',
            className='portfolio-profile-pic'
        ),
        html.H1(
            "Hey, I'm Aditya.",
            className='text-3xl font-semibold margin-top-lg',
            style={'marginBottom': '0'}
        ),
        SocialTiles(),
        html.P(
            "I’m a tech enthusiast who just can’t get enough of AI and machine learning - basically, if it’s got code and a bit of brainpower, I’m in. When I’m not busy making bots smarter or wrangling data, I’m probably diving into some book by Camus or Sartre or pretending I can sing well enough to perform (spoiler: I can’t). Balancing tech and creativity keeps things interesting and my brain from turning into a dry circuit board.",
            className='text-large margin-top-md',
            style={'marginBottom': '0'}
        ),
        html.P(
            "I’m all about pushing AI to be more helpful and less like that one confused robot in every sci-fi movie. My goal? To get into research and build AI that actually gets humans, not just runs on fancy algorithms. For now, I’m having fun learning, experimenting, and dreaming about a future where AI makes life easier -     and maybe even a little more fun.",
            className='text-large margin-top-md',
            style={'marginBottom': '0'}
        )
    ], className='portfolio-section', style={'marginTop': '0'}),
    html.Div([
        html.H2("Work Experience", className='text-3xl font-semibold margin-bottom-xs'),
        html.Div([ExperienceTile(exp) for exp in data.get('workExperience', [])], className='portfolio-experience-card'),
        html.Div(style={'height': '64px'}),
    ], className='portfolio-section margin-bottom-xl'),
    html.Div([
        html.H2("Recent Writings", className='text-3xl font-semibold margin-bottom-xs'),
        html.Div(
            [BlogTile(blog, show_tags=False) for blog in recent_blogs if 'title' in blog] if recent_blogs else
            [html.P("No blog posts available.", className='text-medium text-gray-400 portfolio-blog-post')],
            className='portfolio-blog-card', style={'marginTop': '0'}
        ),
        html.Div(
            html.A([
            "Checkout all blogs",
            html.Span(
                svg.Svg([
                    svg.Path(d="M7 7h10v10"),
                    svg.Path(d="M7 17 17 7")
                ],
                xmlns="http://www.w3.org/2000/svg",
                width="14",
                height="14",
                viewBox="0 0 24 24",
                fill="none",
                stroke="currentColor",
                className="lucide lucide-arrow-up-right")
            , className='portfolio-button-icon')
        ], href='/blog', className='portfolio-button'), className='portfolio-button-div')
    ], className='portfolio-section margin-bottom-xl'),
    html.Div([
        html.H2("Get in touch", className='text-3xl font-semibold margin-bottom-md'),
        html.P(
            "If you’re building something cool where my skills can be of some use or just want to nerd out over philosophy and machine learning, hit me up at lakhaniaditya@yahoo.in - always up for a good chat (or a questionable karaoke session).",
            className='text-medium margin-bottom-md'
        )
    ], className='portfolio-section margin-bottom-xl')
])
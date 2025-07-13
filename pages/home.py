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
            "I'm an AI Engineer who admires tech, wit, literature and linguistics. Most of my time goes into making systems that work better and break more interestingly. When I’m not coding or debugging a stubborn pipeline, I’m either reading Camus, Kafka, Orwell or playing guitar. Balancing tech and creativity keeps things interesting in my brain; or at least keeps it from mistaking motion for direction.",
            className='text-large margin-top-md',
            style={'marginBottom': '0'}
        ),
        html.P(
            "Lately, I’ve been focused on building tools that make complex problems feel a little less intimidating, systems that don’t just process data but actually help make sense of it. It’s a mix of engineering and a bit of art, figuring out how to balance precision with nuance. When things go sideways, I learn more than when they run smoothly! which is exactly what makes the work far from boring.",
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
            "If you’re working on something interesting where I can pitch in, or just want to geek out over philosophy and machine learning, drop me a line at lakhaniaditya@yahoo.in. Always up for a good conversation, or an impromptu jam session (guitar optional).",
            className='text-medium margin-bottom-md'
        )
    ], className='portfolio-section margin-bottom-xl')
])
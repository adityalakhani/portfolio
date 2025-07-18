import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from components import BlogTile
from utils import blog_posts

app = dash.Dash(__name__)

# Load and sort blog data
all_tags = ['All'] + sorted(set(tag for blog in blog_posts for tag in blog.get('tags', [])))

# Blog page layout
layout = html.Div([
    html.Div([
    html.H2("Recent Writings", className='text-3xl font-semibold', style={'margin': '0'}),
    dcc.Dropdown(
        id='tag-filter',
        options=[{'label': tag, 'value': tag} for tag in all_tags],
        value='All',
        className='portfolio-blog-filter'
    )
    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'alignItems': 'center',
    }),

    html.Div(id='blog-list', className='portfolio-section margin-bottom-xl', style={'marginTop': '16px'})
])

@callback(
    Output('blog-list', 'children'),
    Input('tag-filter', 'value')
)
def update_blogs(selected_tag):
    filtered_blogs = blog_posts if selected_tag == 'All' else [b for b in blog_posts if selected_tag in b.get('tags', [])]
    return [BlogTile(blog, show_tags=True) for blog in filtered_blogs] if filtered_blogs else [html.P("No blog posts available.", className='text-medium text-gray-400')]
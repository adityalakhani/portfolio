import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import json
from datetime import datetime
from components import BlogTile

app = dash.Dash(__name__)

# Load and sort blog data
try:
    with open('public/data.json', 'r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading data.json: {e}")
    data = {'blogData': []}

blog_data = sorted(
    data.get('blogData', []),
    key=lambda x: datetime.strptime(x.get('date_posted', 'January 1, 1900'), '%B %d, %Y'),
    reverse=True
)
all_tags = ['All'] + sorted(set(tag for blog in blog_data for tag in blog.get('tags', [])))

# Blog page layout
layout = html.Div([
    html.H2("Recent Writings", className='text-3xl font-semibold margin-bottom-md'),
    dcc.Dropdown(
        id='tag-filter',
        options=[{'label': tag, 'value': tag} for tag in all_tags],
        value='All',
        className='portfolio-blog-filter margin-bottom-md'
    ),
    html.Div(id='blog-list', className='portfolio-section margin-bottom-xl')
])

@callback(
    Output('blog-list', 'children'),
    Input('tag-filter', 'value')
)
def update_blogs(selected_tag):
    filtered_blogs = blog_data if selected_tag == 'All' else [b for b in blog_data if selected_tag in b.get('tags', [])]
    return [BlogTile(blog, show_tags=True) for blog in filtered_blogs] if filtered_blogs else [html.P("No blog posts available.", className='text-medium text-gray-400')]
from dash import html, dcc, Input, Output, State, callback, MATCH
from dash_iconify import DashIconify
import dash

def BlogTile(blog, show_tags=True):
    """Component for rendering a blog tile, consistent with BlogTile.jsx"""
    return html.Div([
        html.P(blog.get('date_posted', 'N/A'), className='portfolio-blog-date portfolio-timeline'),
        html.A(html.H3(blog['title'], className='portfolio-blog-title'), href=f"/blog/{blog['slug']}", className='portfolio-blog-title-link'),
        html.P(blog['desc'], className='portfolio-blog-desc'),
        html.Div(
            [html.Span(f"#{tag}", className='portfolio-blog-tag') for tag in blog.get('tags', [])] if show_tags else [],
            className='flex-gap-sm', style={'marginTop': '0.5rem', 'flex-wrap': 'wrap'}
        )
    ], className='portfolio-blog-card')

def ExperienceTile(work):
    """Component for rendering an experience tile, consistent with ExperienceTile.jsx"""
    return html.Div([
        html.Div([
            html.Img(src=work.get('logo', ''), className='portfolio-experience-logo', style={'display': 'block' if work.get('logo') else 'none'}),
            html.Div([
                html.P(f"{work['start_date']} - {work['end_date']}", className='portfolio-experience-date portfolio-timeline'),
                html.H3(f"{work['title']}, {work['company']}", className='portfolio-experience-title'),
                html.P(work['roledesc'], className='portfolio-experience-desc'),
                html.Div([html.Span(skill, className='portfolio-experience-skill') for skill in work.get('skills', [])], className='portfolio-experience-skills')
            ], className='portfolio-experience-content')
        ], className='portfolio-experience-card-content')
    ], className='portfolio-experience-card')

def SocialTiles():
    """Component for rendering social media links, consistent with SocialTiles.jsx"""
    return html.Div([
        html.A(DashIconify(icon="lucide:github", width=18, height=18), href="https://github.com/adityalakhani", className='portfolio-social-link'),
        html.A(DashIconify(icon="lucide:file", width=18, height=18), href="assets/Resume.pdf", className='portfolio-social-link'),
        html.A(DashIconify(icon="lucide:linkedin", width=18, height=18), href="https://www.linkedin.com/in/lakhaniaditya/", className='portfolio-social-link'),
    ], className='portfolio-social-tiles')

def CodeSnippet(code, language='text', id_prefix='code-snippet'):
    import uuid
    unique_id = str(uuid.uuid4())
    # Include language as a styled span in Markdown content
    markdown_content = f'<span class="code-snippet-language">{language}</span>\n```{language}\n{code}\n```'
    return html.Div([
        dcc.Store(id={'type': 'code-content', 'index': unique_id}, data=code),
        dcc.Store(id={'type': 'clipboard', 'index': unique_id}, data=code),
        dcc.Store(id={'type': 'copy-state', 'index': unique_id}, data={'copied': False, 'n_clicks': 0}),
        dcc.Interval(
            id={'type': 'reset-interval', 'index': unique_id},
            interval=2000,  # 2 seconds
            n_intervals=0,
            disabled=True
        ),
        html.Pre([
            dcc.Markdown(
                markdown_content,
                className='code-snippet-code',
                highlight_config={'theme': 'dark'},
                style={'margin': 0, 'border': '0.1px solid white', 'border-radius': '0', 'padding': '0'},
                dangerously_allow_html=True
            ),
            html.Button([
                DashIconify(icon="lucide:copy", width=16, height=16, className='copy-icon'),
                html.Span('Copy', className='copy-text', style={'display': 'none'})
            ], id={'type': 'copy-button', 'index': unique_id}, className='copy-button')
        ], className='code-snippet-pre', style={'margin': '0', 'padding': '0'})
    ], className='code-snippet', style={'margin': '0', 'padding': '0'})

@callback(
    [
        Output({'type': 'copy-button', 'index': MATCH}, 'children'),
        Output({'type': 'clipboard', 'index': MATCH}, 'n_clicks'),
        Output({'type': 'reset-interval', 'index': MATCH}, 'disabled'),
        Output({'type': 'reset-interval', 'index': MATCH}, 'n_intervals'),
        Output({'type': 'copy-state', 'index': MATCH}, 'data')
    ],
    [
        Input({'type': 'copy-button', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'reset-interval', 'index': MATCH}, 'n_intervals')
    ],
    [
        State({'type': 'code-content', 'index': MATCH}, 'data'),
        State({'type': 'copy-state', 'index': MATCH}, 'data')
    ],
    prevent_initial_call=True
)
def copy_code(n_clicks, n_intervals, code, copy_state):
    from dash import ctx
    triggered_id = ctx.triggered_id
    index = triggered_id['index']

    if triggered_id['type'] == 'copy-button' and n_clicks and n_clicks > copy_state['n_clicks']:
        return (
            [
                DashIconify(icon="lucide:check", width=16, height=16, id={'type': 'copy-icon', 'index': index}),
                html.Span('Copied!', className='copy-text', style={'display': 'none'})
            ],
            n_clicks,
            False,
            0,
            {'copied': True, 'n_clicks': n_clicks}
        )
    elif triggered_id['type'] == 'reset-interval' and n_intervals > 0 and copy_state['copied']:
        return (
            [
                DashIconify(icon="lucide:copy", width=16, height=16, id={'type': 'copy-icon', 'index': index}),
                html.Span('Copy', className='copy-text', style={'display': 'none'})
            ],
            0,
            True,
            0,
            {'copied': False, 'n_clicks': copy_state['n_clicks']}
        )
    return dash.no_update
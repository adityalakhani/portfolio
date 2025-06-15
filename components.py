from dash import html
from dash_iconify import DashIconify

def BlogTile(blog, show_tags=True):
    """Component for rendering a blog tile, consistent with BlogTile.jsx"""
    return html.Div([
        html.P(
            blog.get('date_posted', 'N/A'),
            className='portfolio-blog-date portfolio-timeline'
        ),
        html.A(
            html.H3(
                blog['title'],
                className='portfolio-blog-title'
            ),
            href=f"/blog/{blog['slug']}",
            className='portfolio-blog-title-link'
        ),
        html.P(
            blog['desc'],
            className='portfolio-blog-desc'
        ),
        html.Div(
            [
                html.Span(
                    f"#{tag}",
                    className='portfolio-blog-tag'
                ) for tag in blog.get('tags', [])
            ] if show_tags else [],
            className='flex-gap-xs'
        )
    ], className='portfolio-blog-card')

def ExperienceTile(work):
    """Component for rendering an experience tile, consistent with ExperienceTile.jsx"""
    return html.Div([
        html.Div([
            html.P(
                f"{work['start_date']} - {work['end_date']}",
                className='portfolio-experience-date portfolio-timeline'
            ),
            html.H3(
                f"{work['title']}, {work['company']}",
                className='portfolio-experience-title'
            ),
            html.P(
                work['roledesc'],
                className='portfolio-experience-desc'
            ),
            html.Div(
                [
                    html.Span(
                        skill,
                        className='portfolio-experience-skill'
                    ) for skill in work.get('skills', [])
                ],
                className='portfolio-experience-skills'
            )
        ], className='portfolio-experience-content')
    ], className='portfolio-experience-card')

def SocialTiles():
    """Component for rendering social media links, consistent with SocialTiles.jsx"""
    return html.Div([
        html.A(
            DashIconify(icon="lucide:github", width=18, height=18),
            href="https://github.com/adityalakhani",
            className='portfolio-social-link'
        ),
        html.A(
            DashIconify(icon="lucide:file", width=18, height=18),
            href="/Resume.pdf",
            className='portfolio-social-link'
        ),
        html.A(
            DashIconify(icon="lucide:linkedin", width=18, height=18),
            href="https://www.linkedin.com/in/lakhaniaditya/",
            className='portfolio-social-link'
        ),
        # html.A(
        #     DashIconify(icon="lucide:instagram", width=18, height=18),
        #     href="https://www.instagram.com/thecortguy/",
        #     className='portfolio-social-link'
        # ),
        # html.A(
        #     DashIconify(icon="lucide:dribbble", width=18, height=18),
        #     href="https://dribbble.com/Sarthakischauhan",
        #     className='portfolio-social-link'
        # ),
    ], className='portfolio-social-tiles')
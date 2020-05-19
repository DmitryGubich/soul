from django import template

import markdown
import wagtailmd

register = template.Library()


@register.filter(name='markdown')
def markdown_filter(value):
    return markdown.markdown(
        value,
        extensions=[
            'toc',
            'extra',
            'codehilite',
            'wagtailmd.mdx.tables',
            'wagtailmd.mdx.mdx_mathjax',
        ],
        extension_configs={
            'codehilite': [
                ('css_class', "highlight")
            ]
        },
        output_format='html5'
    )

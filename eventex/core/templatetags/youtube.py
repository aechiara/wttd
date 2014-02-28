# coding: utf-8
from django.template import (Context, Template, Node, TemplateSyntaxError, Variable, VariableDoesNotExist, Library)

TEMPLATE2 = '''
<object width="480" height="385">
    <param name="movie" value="http://www.youtube.com/v/{{ id }}" />
    <param name="allowFullScreen" value="true" />
    <param name="allowscriptaccess" value="always' />
    <embed src="http://www.youtube.com/v/{{ id }}"
        type="application/x-shockwave-flash" alowscriptaccess="always"
        allowfullscreen="true" width="480" height="385">
    </embed>
</object>
'''

TEMPLATE = '''
<iframe width="640" height="360" src="//www.youtube.com/embed/{{ id }}?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>
'''

def do_youtube(parser, token):
    try:
        tag_name, _id = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError, "%r tag requires 1 argument" % token.contents.split()[0]
    return YoutubeNode(_id)



class YoutubeNode(Node):
    def __init__(self, _id):
        self.id = Variable(_id)

    def render(self, context):
        try:
            actual_id = self.id.resolve(context)
        except VariableDoesNotExist:
            actual_id = self.id

        t = Template(TEMPLATE)
        c = Context({'id': actual_id}, autoescape=context.autoescape)
        return t.render(c)

register = Library()
register.tag('youtube', do_youtube)

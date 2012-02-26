from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from exercises import models

def menu(request, template_name='exercises/menu.html'):
    nodes = models.KhanExerciseTreeNode.tree.get(
        khan_id='math').get_descendants(include_self=False)
    return render_to_response(template_name, RequestContext(request, {
        'nodes': nodes
    }))

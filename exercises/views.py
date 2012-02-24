from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from exercises import models

def menu(request, template_name='exercises/menu.html'):
    return render_to_response(template_name, RequestContext(request, {
        'nodes': get_object_or_404(
            models.KhanExerciseTreeNode, khan_id='root').get_descendants()
    }))

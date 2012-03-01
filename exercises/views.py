from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from exercises import models

def menu(request, template_name='exercises/menu.html'):
    nodes = models.KhanExerciseTreeNode.tree.get(
        khan_id='math').get_descendants(include_self=False)
    return render_to_response(template_name, RequestContext(request, {
        'nodes': nodes
    }))

def edit_categories(request, template_name='exercises/edit_categories.html'):
    from django.forms.models import modelformset_factory

    formset_cls = modelformset_factory(
        models.KhanExerciseTreeNode, extra=0, fields=('parent',))

    nodes = models.KhanExerciseTreeNode.tree.get(
        khan_id='math').get_descendants(include_self=False)
    if request.POST:
        formset = formset_cls(request.POST, queryset=nodes)
        if formset.is_valid():
            formset.save()
    else:
        formset = formset_cls(queryset=nodes)

    # only display categories in drop-downs
    parent_queryset = models.KhanExerciseTreeNode.objects.filter(is_topic=True)
    for form in formset.forms:
        form.fields['parent'].queryset = parent_queryset

    return render_to_response(template_name, {
        'formset': formset
    })

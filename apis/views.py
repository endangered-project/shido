from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apis.serializers import ClassSerializer
from apps.models import Class


@csrf_exempt
@require_http_methods(["GET"])
def get_all_class(request):
    """
    View for return all class in JSON format.

    :param request: WSGI request from user
    :return: All class in JSON format.
    """
    return JsonResponse({
        'class': ClassSerializer(Class.objects.all(), many=True).data
    })

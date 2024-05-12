from django.http import HttpRequest, JsonResponse


def index(request: HttpRequest) -> JsonResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return JsonResponse({"data": "some data"})

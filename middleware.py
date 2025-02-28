from django.http import HttpResponseRedirect


class RedirectToAnotherPageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/":
            return HttpResponseRedirect("/admin/")
        return self.get_response(request)

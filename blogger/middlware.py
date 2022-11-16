from django.shortcuts import render


class SiteBlock:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # response = render(request, 'site_block.html')
        return response






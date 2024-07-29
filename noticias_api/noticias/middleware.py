from django.http import JsonResponse

class CustomTokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization')
        if token != 'Bearer 7939d2aefc22439bbf16da778c2c2628':
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        response = self.get_response(request)
        return response

 
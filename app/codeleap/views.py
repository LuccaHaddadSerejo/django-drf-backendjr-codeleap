from rest_framework.generics import ListCreateAPIView, \
                                    RetrieveUpdateDestroyAPIView
from .models import Codeleap
from .serializers import CodeleapSerializer


class CodeleapView(ListCreateAPIView):
    queryset = Codeleap.objects.all()
    serializer_class = CodeleapSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CodeleapDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Codeleap.objects.all()
    serializer_class = CodeleapSerializer
    lookup_url_kwarg = "codeleap_id"

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

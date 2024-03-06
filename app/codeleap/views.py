from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests

from .serializers import CodeleapSerializer
from .models import Codeleap

external_url = "https://dev.codeleap.co.uk/careers/"


class CodeleapView(APIView):
    def get(self, request) -> Response:
        response = requests.get(external_url)

        return Response(response.json(), status=response.status_code)

    def post(self, request) -> Response:
        serializer = CodeleapSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = requests.post(external_url, json=serializer.data)
        return Response(response.json(), status=response.status_code)


class CodeleapDetailView(APIView):
    def patch(self, request, element_id: int) -> Response:
        element = requests.get(f"{external_url}/{element_id}/")

        if element.status_code == 404:
            return Response(
                            {"detail": "Not found"},
                            status=status.HTTP_404_NOT_FOUND
                           )

        external_data = {
                         key: value for key, value in element.json().items()
                         if key not in ["author_ip", "id", "created_datetime"]
                        }

        # Create a dummy instance of Codeleap with the external data
        instance = Codeleap.objects.create(**external_data)

        serializer = CodeleapSerializer(
                                        instance,
                                        data=request.data,
                                        partial=True
                                       )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Delete the dummy instance of Codeleap
        instance.delete()

        response = requests.patch(
                                  f"{external_url}/{element_id}/",
                                  json=serializer.data
                                 )

        return Response(response.json(), status=response.status_code)

    def delete(self, request, element_id: int) -> Response:
        element = requests.get(f"{external_url}/{element_id}/")

        if element.status_code == 404:
            return Response(
                            {"detail": "Not found"},
                            status=status.HTTP_404_NOT_FOUND
                           )

        response = requests.delete(f"{external_url}/{element_id}/")

        return Response({}, status=response.status_code)

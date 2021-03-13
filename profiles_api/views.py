from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most constrol over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle a delete of an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a Hello Message"""
        a_viewset = [
        'Uses actions (list, creat, retrieve, update, partial_update)',
        'Automatically maps to URLs using Routers'
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get by ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Update by ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partial update by ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Remove by ID"""
        return Response({'http_method': 'DELETE'})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def index(request):
    message = 'hello from the apiiiiiiiiiiiii'
    return Response(data=message, status=status.HTTP_200_OK)

@api_view(['POST'])
def process_and_respond(request):
    message = 'You sent me this crap? ' + request.data['text']
    return Response(data=message, status=status.HTTP_200_OK)
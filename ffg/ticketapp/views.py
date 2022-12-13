from rest_framework import status, generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenVerifySerializer

from .models import Ticket, TicketAnswers
from .serializers import UserSerializer, TicketSerializer, TicketAnswerSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'data': serializer.data},
            status=status.HTTP_201_CREATED
        )

    return Response(
        {'data': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST
    )

class TicketAPIList(generics.ListAPIView):
    #queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminUser, IsAuthenticated, )

    def get_queryset(self):
        if 'userid' in self.request.GET.keys():
            queryset = Ticket.objects.filter(user_id=int(self.request.GET['userid']))

            return queryset
        else:
            queryset = Ticket.objects.all()
            
            return queryset.order_by('-time_create')

class TicketAPIAsnwersList(generics.ListAPIView):
    #queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminUser, IsAuthenticated, )

    def get_queryset(self):
        if 'id' in self.request.GET.keys():
            queryset = TicketAnswers.objects.filter(ticket_id=int(self.request.GET['id']))

            return queryset
        else:
            raise Http404

class TicketAPIUserTicketAnswer(generics.CreateAPIView):
    queryset = TicketAnswers.objects.all()
    serializer_class = TicketAnswerSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket, id=int(self.request.GET['id']))
        user_from = get_object_or_404(User, id=self.request.user.id)
        user_to = get_object_or_404(User, id=Ticket.objects.get(id = int(self.request.GET['id'])).user.id)
        return serializer.save(ticket=ticket, user_from=user_from, user_to=user_to)

class TicketAPICreate(generics.CreateAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(user=user)

class TicketAPIChangeStatus(generics.ListAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get_queryset(self):
        new_raw = Ticket.objects.get(id=int(self.request.GET['id']))
        new_raw.status = list(self.request.GET.keys())[-1]

        return new_raw.save()

        




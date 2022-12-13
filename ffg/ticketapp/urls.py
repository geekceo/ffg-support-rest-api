from django.urls import URLPattern, path, include
from django.conf import settings
from django.conf.urls.static import static
from ticketapp.views import( 
    create_user,
    TicketAPICreate,
    TicketAPIList,
    TicketAPIUserTicketAnswer,
    TicketAPIAsnwersList,
    TicketAPIChangeStatus)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/user/create', create_user, name='create_user'),
    path('api/v1/user/ticket/all_tickets', TicketAPIList.as_view(), name='all_tickets'),
    path('api/v1/user/ticket/create', TicketAPICreate.as_view(), name='create_ticket'),
    path('api/v1/user/ticket/answer', TicketAPIUserTicketAnswer.as_view(), name='answer_ticket'),
    path('api/v1/user/ticket/all_answers', TicketAPIAsnwersList.as_view(), name='all_answers_ticket'),
    path('api/v1/user/ticket/status', TicketAPIChangeStatus.as_view(), name='change_status_ticket'),
]

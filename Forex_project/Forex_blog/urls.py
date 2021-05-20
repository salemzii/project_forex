from django.urls import path
from . import views
from .views import TopicView, AddCommentView

urlpatterns = [
    path('', views.show_welcome, name='welcome_page'),
    path('<int:pk>/post', TopicView.as_view(), name='topic'),
    path('<int:pk>/comment', AddCommentView.as_view(), name='comment')
]
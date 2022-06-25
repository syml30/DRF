from django.urls import path, include
from .views import QuestionList, QuestionDetail, ChoiceList, CreateSelection, UserCreate, LoginView

urlpatterns = [
    path("questions/", QuestionList.as_view(), name="questions_list"),
    path("questions/<int:pk>", QuestionDetail.as_view(), name="questions_detail"),
    path("questions/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("questions/<int:pk>/choices/<int:choice_pk>/select/", CreateSelection.as_view(), name="create_selection"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),

]

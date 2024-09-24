from django.urls import path

from my_app.views import IndexView, NoteView, NotesCreateView, NotesUpdateView, NotesDeleteView, MakeNoteDoneView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('notes/', NoteView.as_view(), name='notes'),
    path('create', NotesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NotesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NotesDeleteView.as_view(), name='delete'),
    path('make_done/<int:pk>/', MakeNoteDoneView.as_view(), name='make_done')

]
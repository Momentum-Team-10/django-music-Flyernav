from django.shortcuts import render
from .models import music_data

# Create your views here.

def list_songs(request):
    music_data = music_data.objects.all()
    return render(request, "templates/base.html",
                  {"music_data": music_data})


# def add_songs(request):
#     if request.method == 'GET':
#         form = SongForm()
#     else:
#         form = SongForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_songs')

#     #return render(request, "contacts/add_contact.html", {"form": form})

#     def edit_songs(request, pk):
#     music_data = get_object_or_404(music_data, pk=pk)
#     if request.method == 'GET':
#         form = SongForm(instance=music_data)
#     else:
#         form = SongForm(data=request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_songs')

#     #return render(request, "contacts/edit_contact.html", {
#         "form": form,
#         "Song": music_data
#     })


# def delete_songs(request, pk):
#     music_data = get_object_or_404(music_data, pk=pk)
#     if request.method == 'POST':
#         music_data.delete()
#         return redirect(to='list_songs')

#     #return render(request, "contacts/delete_contact.html",
#                   {"music_data": music_data})
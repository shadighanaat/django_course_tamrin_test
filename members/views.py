from django.shortcuts import render, redirect

from .models import Members
from django.shortcuts import get_object_or_404
from .form import NewMembersForm
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy


# def members_list(request):
#     members = Members.objects.all().order_by('-datetime_modified')
#
#     context = {'members': members}
#
#     return render(request, 'members/members.html', context)
class MembersListView(generic.ListView):
    model = Members
    template_name = 'members/members.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Members.objects.all().order_by('-datetime_modified')


# def members_detail(request, pk):
#     members = get_object_or_404(Members, pk=pk)
#
#     return render(request, 'members/members_detail.html', {'members': members})
class MembersDetailView(generic.DetailView):
    model = Members
    template_name = 'members/members_detail.html'
    context_object_name = 'members'


# def post_create_add(request):
#     if request.method == 'POST':
#         form = NewMembersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('members_list')
#
#     else:
#         form = NewMembersForm()
#
#     return render(request, 'members/post_add.html', context={'form': form})
#
class MembersCreateView(generic.CreateView):
    form_class = NewMembersForm
    template_name = 'members/post_add.html'


# def post_update(request, pk):
#     post = get_object_or_404(Members, pk=pk)
#     form = NewMembersForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('members_list')
#
#     return render(request, 'members/post_add.html', context={'form': form})
class MembersUpdateView(generic.UpdateView):
    model = Members
    form_class = NewMembersForm
    template_name = 'members/post_add.html'


# def post_delete(request, pk):
#     post = get_object_or_404(Members, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('members_list')
#
#     return render(request, 'members/post_delete.html', context={'post': post})
class MembersDeleteView(generic.DeleteView):
    model = Members
    template_name = 'members/post_delete.html'
    success_url = reverse_lazy('members_list')

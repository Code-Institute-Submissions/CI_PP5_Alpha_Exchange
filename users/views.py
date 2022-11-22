from django.shortcuts import render


def userAccount(request):
    """ Display the user's profile. """

    template = 'users/profile.html'
    context = {}

    return render(request, template, context)
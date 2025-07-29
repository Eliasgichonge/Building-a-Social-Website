from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        # Form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # Form data is valid
            new_image = form.save(commit=False)
            # Assign current user to the image
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully.')
            return redirect(new_image.get_absolute_url())  # You can change this to your redirect target
        else:
            messages.error(request, 'There was an error with the form.')
    else:
        # Build form with data from the GET request
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'form': form})

# polls_app/views.py
from django.shortcuts import render
from .models import UserResponse
from .tasks import send_delayed_email

def submit_response(request):
    if request.method == 'POST':
        # Process the form data
        form = UserResponseForm(request.POST)
        if form.is_valid():
            user_response = form.save()

            # Send email notification as a delayed task
            subject = 'Poll Response Received'
            message = f'Thank you for participating in the poll. Your response has been recorded.'
            from_email = 'poojithag0393@gmail.com'
            recipient_list = [user_response.email]

            send_delayed_email.apply_async(
                (subject, message, from_email, recipient_list),
                countdown=5  # Specify the delay in seconds (e.g., 10 seconds)
            )

            return render(request, 'polls_app/success.html')
    else:
        form = UserResponseForm()

    return render(request, 'polls_app/response_form.html', {'form': form})

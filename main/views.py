from django.contrib.auth.decorators import login_required
from wikipedia.exceptions import DisambiguationError, PageError
from requests.exceptions import RequestException
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from requests.exceptions import RequestException
from datetime import datetime
import base64
import json
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
from .models import Learner, Note
from .forms import NoteForm, Registration  # registration form
from wikipedia.exceptions import DisambiguationError, PageError
from requests.exceptions import RequestException  # wikipedia connection 
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)  #Registration form
        if form.is_valid():
            user = form.save()  # Saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('login')  # Redirect to login page after registration
    else:
        form = Registration()  #Registration form
    return render(request, 'register.html', {'form': form})
      


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    return render(request, 'login.html', {'error_message': error_message})






def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return render(request, 'edit_note.html', {
                'form': form,
                'message': 'Note updated successfully!'
            })
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form})




def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id) 
    return render(request, 'note_detail.html', {'note': note})


# View to list all notes
def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})
    notes = Note.objects.all()

# View to add a new note
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')  # Redirect to the list page
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})

def view_notes(request):
    notes = Note.objects.all()  # Retrieve all notes
    return render(request, 'view_notes.html', {'notes': notes})


# View to delete a note
def delete_note(request, note_id):
    # Get the note object by its ID or return 404 if not found
    note = get_object_or_404(Note, id=note_id)

    # Delete the note
    note.delete()

    # Redirect the user back to the notes page (or wherever you want to send them)
    return redirect('view_notes')


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Associate the note with the currently logged-in user
            note.save()
            return redirect('note_list')  # Redirect to the notes list or another page
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})

def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'note_detail.html', {'note': note})







# Dashboard Page (Requires Login)      how the hell is this not working
@login_required
def dashboard(request):
    return render(request, 'support.html')


# Home Page (Requires Login)
@login_required
def home(request):
    return render(request, 'home.html')


# About Page
def about(request):
    return render(request, 'about.html')

def attempts(request):
    return render(request, 'attempts.html')


# Courses Page (Requires Login)
@login_required
def courses(request):
    user_xp = 150
    total_xp = 500
    user_xp_percentage = (user_xp / total_xp) * 100
    return render(request, 'courses.html', {
        'user_xp': user_xp,
        'total_xp': total_xp,
        'user_xp_percentage': user_xp_percentage
    })



# Contact Page
def contact(request):
    return render(request, 'contact.html')


# Process Contact Form Submission
def submit_contact(request):
    if request.method == 'POST':
        # Example form processing logic
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # TODO: Add logic to store contact form in the database or send an email
        return HttpResponse("Form submitted successfully! Thank you for reaching out.")
    return HttpResponse("Invalid request.")


# Support Page (Requires Login)
@login_required
def support(request):
    return render(request, 'support.html')


def view_notes(request):
    notes = Note.objects.filter(user=request.user) 
    return render(request, 'view_notes.html', {'notes': notes})


# Wikipedia Page

def wikipedia_page(request):
    topic = request.GET.get('topic', 'EMOBILIS')  # Default topic if none provided
    summary = ""
    page_url = None

    try:
        # Fetch the summary from Wikipedia
        summary = wikipedia.summary(topic, sentences=13)  # Removed 'timeout'
        page_url = wikipedia.page(topic).url  # Get the page URL
    except DisambiguationError as e:
        # Handle ambiguous topics
        summary = f"Too many results for '{topic}'. Try being more specific."
    except PageError:
        # Handle cases where the page doesn't exist
        summary = f"No results found for '{topic}'. Please try again."
    except RequestException:
        # Handle connection timeout and other request-related errors
        summary = "Could not connect to Wikipedia. Please check your internet connection and try again."
    except Exception as e:
        # Handle any other exceptions
        summary = f"An error occurred: {str(e)}"

    # Pass the data to the template
    context = {
        'topic': topic,
        'summary': summary,
        'page_url': page_url,
    }
    return render(request, 'wikipedia_page.html', context)




# User Login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')


# Learners Page
def learners_page(request):
    learners = Learner.objects.all()
    return render(request, 'learners_page.html', {'learners': learners})



def forgot_password(request):
    return render(request, 'forgot-password.html')


# Donation Page
def donate_view(request):
    return render(request, 'donate.html')

def libraries(request):
    return render(request, 'libraries.html')


# Process M-Pesa STK Push
@csrf_exempt
def process_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        phone_number = request.POST.get('phone_number')
        
        

        # M-Pesa API Details
        access_token = "REPLACE_WITH_YOUR_ACCESS_TOKEN"  # Generate dynamically
        business_shortcode = "174379"  # Default sandbox shortcode
        passkey = "YOUR_PASSKEY"
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(f"{business_shortcode}{passkey}{timestamp}".encode()).decode()
        
        

        # API Endpoint
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {
            "BusinessShortCode": business_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),
            "PartyA": phone_number,
            "PartyB": business_shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://example.com/mpesa_callback/",
            "AccountReference": "EduBridge",
            "TransactionDesc": "Contribution for EduBridge"
        }

        # Send API request
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()

        # Handle response
        if response_data.get('ResponseCode') == '0':
            return JsonResponse({'status': 'success', 'message': 'Payment initiated successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Payment initiation failed. Please try again.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# M-Pesa Callback
@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        transaction_data = json.loads(request.body)

        if transaction_data.get('Body', {}).get('stkCallback', {}).get('ResultCode') == 0:
            return JsonResponse({'status': 'success', 'message': 'Payment successful!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Payment failed.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid callback.'})




#lessons under web development
def dev(request):
    return render(request, 'dev.html')

def lesson1(request):
    return render(request, 'lesson1.html')

def lesson2(request):
    return render(request, 'lesson2.html')

def lesson3(request):
    return render(request, 'lesson3.html')

def lesson4(request):
    return render(request, 'lesson4.html')

def lesson5(request):
    return render(request, 'lesson5.html')

def lesson6(request):
    return render(request, 'lesson6.html')

def lesson7(request):
    return render(request, 'lesson7.html')

def lesson8(request):
    return render(request, 'lesson8.html')

def lesson9(request):
    return render(request, 'lesson9.html')

def lesson10(request):
    return render(request, 'lesson10.html')

def lesson11(request):
    return render(request, 'lesson11.html')

def lesson12(request):
    return render(request, 'lesson12.html')

def lesson13(request):
    return render(request, 'lesson13.html')

def lesson14(request):
    return render(request, 'lesson14.html')

def lesson15(request):
    return render(request, 'lesson15.html')

def assessment(request):
    return render(request, 'assessment.html')

def progress(request):
    return render(request, 'progress.html')


from django.shortcuts import redirect

def quiz_submission(request):
    if request.method == 'POST':
        # Process quiz answers here...
        return redirect('attempts')  # Redirect to the 'attempts' page





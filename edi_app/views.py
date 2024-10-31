from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EDIMessage
from .utils import validate_edifact_message

from .utils import parse_edifact_message
def upload_edi(request):
    if request.method == "POST":
        sender = request.POST.get("sender")
        receiver = request.POST.get("receiver")
        document_type = request.POST.get("document_type")
        raw_message = request.POST.get("document_data")

        # EDIFACT mesajını çözümleme ve doğrulama
        parsed_message = parse_edifact_message(raw_message)
        is_valid, missing_segments = validate_edifact_message(parsed_message)

        if not is_valid:
            return render(request, "upload_edi.html", {
                "error": f"Invalid EDI Message Missing segments: {', '.join(missing_segments)}"
            })

        # Veritabanına kaydet
        edi_message = EDIMessage.objects.create(
            sender=sender,
            receiver=receiver,
            document_type=document_type,
            document_data=str(parsed_message)
        )
        return render(request, "upload_edi.html", {
            "success": f"EDI Message loaded: {edi_message}"
        })
    
    return render(request, "upload_edi.html")

def home(request):
    return render(request, 'base.html')

# edi_app/views.py
def list_edi_messages(request):
    messages = EDIMessage.objects.all()
    return render(request, 'list_edi.html', {'messages': messages})


# edi_app/views.py
from .forms import EDIMessagesForm

def create_edi_message(request):
    if request.method == 'POST':
        form = EDIMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_edi_messages') 
    else:
        form = EDIMessagesForm()
    return render(request, 'create_edi_messages.html', {'form': form})

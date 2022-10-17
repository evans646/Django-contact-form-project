from django.shortcuts import render
from .form import ContactForm

#index view
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        created_contact_pk = None
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            created_contact = filled_form.save()
            created_contact_pk = created_contact.id
            note = 'Thanks for contacting me %s,  I will reach out back to you soon'%(filled_form.cleaned_data['name'])
            print( created_contact_pk)
            filled_form = ContactForm()
        else:
            fail_note = 'Message was not sent, please try again'
        return render(request, 'forms/index.html', {'contactform':filled_form, 'note':note,'created_contact_pk':created_contact_pk})
    else:
        form =  ContactForm()
        return  render(request, 'forms/index.html', {'contactform':form})



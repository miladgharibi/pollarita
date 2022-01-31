from .forms import CreatePollForm

def poll(request):
        return {'poll_creation_form':CreatePollForm()}
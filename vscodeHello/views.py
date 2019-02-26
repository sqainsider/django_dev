from datetime import datetime

from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage


from hello.forms import ContactForm
from hello.models import Contact


# def home(request):
#     return HttpResponse("Hello, My First Django Project!")

# def home(request):
#     return render(request, "hello/home.html")


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")

        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})


def contact_entry(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            entry = form.save(commit=False)
            entry.timestamp_date = datetime.now()
            entry.save()
            return redirect("contact_entry")

        else:
            return render(request, "hello/contact_entry.html", {"form": form})
    else:
        return render(request, "hello/contact_entry.html", {"form": form})


# def hello_there(request, name):

#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # # Filter the name argument to letters only using regular expressions. URL arguments
#     # # can contain arbitrary text, so we restrict to safe characters only.
#     # match_object = re.match("[a-zA-Z]+", name)

#     # if match_object:
#     #     clean_name = match_object.group(0)
#     # else:
#     #     clean_name = "Friend"

#     # content = "Hello there, " + clean_name + "! It's " + formatted_now
#     # return HttpResponse(content)

#     # now = datetime.now()
#     # formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
#     content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

#     return render(
#         request,
#         'hello/hello_there.html',
#         {
#             'title': 'Hello, Django',
#             'content': content,
#         )
#     }


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name,
                                            "date": datetime.now()}
    )

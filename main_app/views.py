from django.shortcuts import render
from .models import *
from .forms import StatusForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


# Create your views here.
def profile(request):
    stats = Status.objects.all().order_by('-time')[:5]
    stati = []
    task_cats = Category.objects.all()
    for stat in stats:
        link, _ = text_parser(str(stat.text))
        stati.append({"text":stat.text, "time":stat.time, "link":link['hits']})
    form = StatusForm()


    return render(request, 'profile.html', {'statuses': stati, 'task_category': task_cats, "form":form})

# Create your views here.
def user_home(request):
    stati = []
    stats = Status.objects.all().order_by('-time')[:10]
    for stat in stats:
        link, cat = text_parser(str(stat.text))
        stati.append({"text":stat.text, "time":stat.time, "link":link['hits']})

    return render(request, 'user_home.html', {'statuses': stati})

def post_status(request):
    form = StatusForm(request.POST)
    if form.is_valid():
        stat = Status(text = form.cleaned_data['text'])
        stat.save()
        _, cat = text_parser(str(stat.text))
        categories = cat['category']

        for cate in Category.objects.all():
            print(cate.category)
            if cate.category in categories:
                cate.priority = 1
            else:
                cate.priority = cate.priority+1
            print(cate.priority)
            cate.save()

    return HttpResponseRedirect('/profile/')

# Create your views here.
def cantask_close_relatives(request):
   # Get a list of tasks by category
    allCats = Category.objects.all().order_by('priority')
    cats = []
    for cate in allCats:
        task = Task.objects.filter(category=cate)
        cats.append((cate.category, task))

    return render(request, 'cantasks.html', {'cats':cats})


# Create your views here.
def cantask_relatives(request):
      # Get a list of tasks by category
    allCats = Category.objects.filter(trust_level__in=['Relatives', 'All']).order_by('priority')
    cats = []
    for cate in allCats:
        task = Task.objects.filter(category=cate)
        cats.append((cate.category, task))


    return render(request, 'cantasks.html', {'cats':cats})


# Create your views here.
def cantask_network(request):
    # Get a list of tasks by category
    allCats = Category.objects.filter(trust_level='All').order_by('priority')
    cats = []
    for cate in allCats:
        task = Task.objects.filter(category=cate)
        cats.append((cate.category, task))


    return render(request, 'cantasks.html', {'cats':cats})


def parse_text(text_string):
    """Function docs string"""
    user_dict = {}
    punctuation = ['.', ',', '!', '?', ':', ';']
    for punct in punctuation:
        text_string = text_string.replace(punct, ' ')
    string_list = text_string.split(' ')
    bigram_list = get_n_grams(string_list, 2)
    merged_list = string_list + bigram_list
    for s in merged_list:
        user_dict[s.lower()] = ''

    return user_dict

def get_n_grams(words, n):
    """Build an ngram"""
    n_grams = []
    for i in range(0, len(words)-n+1):
        n_grams.append(' '.join(words[i:(i+n)]))
    return n_grams

def text_parser(text):

    small_dictionary = parse_text(str(text))

    big_dictionary = {'chemotherapy': ('https://www.cancer.dk/hjaelp-viden/kraeftbehandling/behandlingsformer/kemoterapi/', ['Transportation', 'Childcare', 'Social']),
                      'lung cancer': ('http://www-dep.iarc.fr/NORDCAN/english/StatsFact.asp?cancer=180&country=208', ['Social', 'Donation']),
                      'treatment': ('https://www.cancer.dk/hjaelp-viden/kraeftbehandling/',
                                    ['Social', 'Transportation', 'Childcare']),
                      'home': ('http://www.example.com', ['Household']),
                      'family': ('http://www.example.com',['Childcare', 'Household']),
                      'donate': ('https://www.cancer.dk/stoet-os/',
                                 ['Donation']),
                      'breast cancer': ('http://www-dep.iarc.fr/NORDCAN/english/StatsFact.asp?cancer=200&country=208',
                                        ['Social', 'Donation']),
                      'immunotherapy': ('https://www.cancer.dk/hjaelp-viden/kraeftbehandling/behandlingsformer/immunterapi/',
                                        ['Transportation', 'Childcare', 'Social']),
                      'radiotherapy': ('https://www.cancer.dk/hjaelp-viden/kraeftbehandling/behandlingsformer/straalebehandling/',
                                       ['Transportation', 'Childcare', 'Social']),
                      'kids': ('http://www.example.com', ['Childcare']),
                      'dog': ('http://www.example.com', ['Petcare']),
                      'cat': ('http://www.example.com', ['Petcare']),
                      'screening': ('https://www.cancer.dk/hjaelp-viden/undersoegelser-for-kraeft/', ['Social', 'Transportation'])}

    final_dict = {'hits': {}}
    cats = {'category': set()}
    for key in small_dictionary:
        if key in big_dictionary:
            final_dict['hits'][key] = big_dictionary[key][0]
            cats['category'].update(big_dictionary[key][1])

    return final_dict, cats


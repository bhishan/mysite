from django.shortcuts import render, redirect
import mechanize
# Create your views here.
kwd = ''
domain = ''

def create_search(request):
    global kwd
    global domain
    if request.method == 'POST':
        kwd = request.POST['keyword']
        domain = request.POST['domain_name']
        print "inside post"
        return redirect('/')
        print "after redirect"
    return render(request,'archive.html',{'keyword':kwd,'position_in_search':mypositioningoogle(kwd, domain)})


def mypositioningoogle(keyword, domain_name):
    if keyword == '' or domain_name == '':
        return ''
    pos_in_search = 0
    found_alert = 0
    br = mechanize.Browser() #initiating a browser

    br.set_handle_robots(False) #we're acting like we're not a bot/robot

#user aget
    br.addheaders = [("User-agent","Mozilla/5.0")]
    keyword = str(keyword)
    domain_name = "http://" + str(domain_name)

    qe= keyword.replace(' ','+')
    counter = 0

    for i in range(0,10):
        google_url = br.open("https://www.google.com/search?q=" + qe + "&start=" + str(counter))
        search_keyword = google_url.read()
        if domain_name in search_keyword:
            found_alert = 1
            break
        counter+=10

    if found_alert:
        pos_in_search = i+1
        if pos_in_search <= 4:
            return "Congratulations!! Your site is seen in page " + str(pos_in_search) + " of google search result for the keyword"
        else:
            return "Your site is seen in page " + str(pos_in_search) + " of google search result for the keyword"
    else:
        return "Your site is not within first 10 pages of google search result for the keyword"
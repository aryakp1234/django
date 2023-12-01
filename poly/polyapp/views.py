from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1><b> Welcome to GPTC periye</b></h1><p>Government Polytechnic, Kasaragod, one among the premier institutes of excellence under the government of Kerala got established in 1988 and it is located at Periye. This institute offers various diploma programs. It has an affiliation with the State Board of Technical Education, Kerala. The admission process only accepts Kerala Polytechnic exam scores for both the 1st and 2nd year admissions.</p>')


def about(request):
    return HttpResponse('<h1><b> About Us </b></h1> <p>To be an institute of global repute, moulding socially committed technicians and entrepreneurs bringing sustainable development.</p> <p><b>Our Mission</b><br>1. Provide value based quality technical education and training using state of the art infrastructure, tools and methodologies.<br>2. Collaborate with industries and academic institutions, bridging the gap between curriculum and latest industrial practices.<br>3. Promote co and extra- curricular activities, fostering leadership qualities, problem solving skills and team spirit.<br>4. Create an ambience for career building, encourage life-long learning leading to self-actualization.')


def contact(request):
    return HttpResponse('<h1> <b>Contact Us </b> </h1><p>Government Polytechnic College Periye P.O. , Kasaragod 671320</p><p>Call Us 04672-234 020</p><p>Mail Us mail@gpckasaragod.ac.in</p>')

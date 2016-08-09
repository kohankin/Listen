		
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Context, RequestContext

import os
import youtube_dl

# Create your views here.


def index(request):

    var = 'hello'
    directory = os.path.join(os.path.expanduser('~'), '/home/djangosites/static/') # path to download folder


    if 'play' in request.GET and request.GET['play']:    

        try:   
  	    var = 'good'
            play_url = request.GET['play']
	    
            ydl_opts = {'verbose': True,
			'extract-audio': True,
			'audio-format': mp3,
			'outtmpl': os.path.join(directory, '%(id)s.%(ext)s'),
                        'nocheckcertificate': True,
			
                        }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#		link = ydl.list_formats()

#                ydl.download([play_url])
#		link = 'yes'
#		link = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'}).extract_info(play_url, download=False)
		link = ydl.extract_info(play_url, download=True)

#		link = 'no'
	

    
	            
        except:
            var = 'except'  
	    link = 'error'
		
    else:
	play_url = 'Insert URL...'
        var = 'else'
        ydl_opts = '' 
	link = 'link'

    return render(request, 'listen/index.html', {'var': var,
						 'play_url': play_url,
						 'link':  link,
								},
                            context_instance=RequestContext(request))






# encoding: utf-8		
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Context, RequestContext

import os
import pafy
from pydub import AudioSegment

# Create your views here.


def index(request):

    var = ''
    directory = os.path.join(os.path.expanduser('~'), '/home/djangosites/static/') # path to download folder
    link = ''
    thumb_link = '' 

    if 'play' in request.GET and request.GET['play']:    

        try:   
  	    var = ''

            play_url = request.GET['play']



            ### get audio from video

            video = pafy.new(play_url)

            
            name =  video.videoid
            source_name = name + '.' + video.getbestaudio().extension

            video.getbestaudio().download(filepath=directory + source_name)

	    thumb_link = video.thumb
	    
            
	    ### convert to mp3

            link = name + '.' + 'mp3'
	    
            AudioSegment.from_file(directory + source_name).export(directory + link, format="mp3")

	    ### delete sorc file

	    os.remove(directory + source_name)

		            
        except:

            var = 'except'  
	    
           



		
    else:
	play_url = 'Insert URL...'
 

    return render(request, 'listen/index.html', {'var': var,
						 'play_url': play_url,
						 'link':  link,
						 'thumb_link': thumb_link,
								},
                            context_instance=RequestContext(request))






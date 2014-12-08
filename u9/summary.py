#!/usr/bin/python
import sys, re
reload(sys)
sys.setdefaultencoding("utf-8")
import os
direc = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "scripts/")
sys.path.append(direc)

def summarize(template):
    print 
    aftershock = 'were' if template['aftershock'] else 'were not'
    tsunami = 'a' if template['tsunami'] else 'no'
    landslide = 'are' if template['landslide'] else 'are not'

    summary = 'On {0} {9}, {10} at {1}, a {2} magnitude earthquake struck {3}. The epicenter of the quake was \
located at {4}. There {5} aftershocks that followed the earthquake and {6} tsunami was caused by \
the earthquake. There {7} reports of landslides due to this earthquake. A total of {8} deaths \
occurred.'.format(template['date'][0], template['time'], \
            template['magnitude'], template['location'], template['epicentre'], aftershock, tsunami, landslide,\
            int(template['deaths']), template['date'][1], template['date'][2])
    print summary
    return summary

from __future__ import unicode_literals
from hazm import *
import langdetect
def normal(tweet):
 normalizer = Normalizer()
 tw=normalizer.normalize(tweet)
 return tw
def detectlang(tweet):
    f=langdetect.detect(tweet)
    return f
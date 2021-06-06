"""
Random useless websites

Quota: 5%
"""

from random import randrange

from .base import Source


db = '''
https://coronavirus-ninja.com/
https://theuselessweb.site/lookadeadfly/
http://www.talktomyass.org/
https://jacksonpollock.org/
http://www.rrrgggbbb.com/
https://chrismckenzie.com/
http://theendofinternet.com/
https://cat-bounce.com/
https://theuselessweb.site/broof/
https://www.screaminggoatpiano.com/#
https://findtheinvisiblecow.com/
http://ninjaflex.com/
https://www.hackertyper.com/
https://shamebell.com/
https://thezen.zone/
https://theuselessweb.site/8bitdance/
http://randomcolour.com/
http://drawing.garden/
http://www.partridgegetslucky.com/
http://www.muchbetterthanthis.com/
http://www.yesnoif.com/
https://imaninja.com/
https://pointerpointer.com/
http://hasthelargehadroncolliderdestroyedtheworldyet.com/
https://potatoortomato.com/
http://www.ismycomputeron.com/
https://crouton.net/
https://loopedforinfinity.com/
https://strobe.cool/
https://zoom.earth/
https://webcamtoy.com/
https://bouncyballs.org/
https://neave.tv/
https://playtictactoe.org/
https://corgiorgy.com/
http://scroll-o-meter.club/
http://www.crossdivisions.com/
http://wutdafuk.com/
https://remoji.com/
http://www.patience-is-a-virtue.org/
http://unicodesnowmanforyou.com/
http://isitwhite.com/
https://pixelsfighting.com/
http://tencents.info/
http://chillestmonkey.com/
https://longdogechallenge.com/
http://heeeeeeeey.com/
http://corndog.io/
https://mondrianandme.com/
https://puginarug.com
https://alwaysjudgeabookbyitscover.com
https://thatsthefinger.com/
https://cant-not-tweet-this.com/
http://eelslap.com/
http://www.staggeringbeauty.com/
http://burymewithmymoney.com/
https://smashthewalls.com/
http://endless.horse/
https://www.trypap.com/
http://www.republiquedesmangues.fr/
http://www.movenowthinklater.com/
http://beesbeesbees.com/
http://www.koalastothemax.com/
http://www.everydayim.com/
http://ihasabucket.com/
http://corndogoncorndog.com/
http://www.hackertyper.com/
http://www.ismycomputeron.com/
http://www.nullingthevoid.com/
http://lacquerlacquer.com
http://iamawesome.com/
https://strobe.cool/
http://www.pleaselike.com/
http://crouton.net/
http://corgiorgy.com/
http://www.wutdafuk.com/
http://unicodesnowmanforyou.com/
http://chillestmonkey.com/
http://scroll-o-meter.club/
http://www.crossdivisions.com/
http://tencents.info/
https://boringboringboring.com/
http://www.patience-is-a-virtue.org/
http://pixelsfighting.com/
http://isitwhite.com/
https://existentialcrisis.com/
http://onemillionlols.com/
http://www.omfgdogs.com/
http://oct82.com/
http://chihuahuaspin.com/
http://www.blankwindows.com/
http://dogs.are.the.most.moe/
http://tunnelsnakes.com/
http://www.trashloop.com/
http://www.ascii-middle-finger.com/
http://spaceis.cool/
http://www.donothingfor2minutes.com/
http://buildshruggie.com/
http://buzzybuzz.biz/
http://yeahlemons.com/
http://wowenwilsonquiz.com
https://thepigeon.org/
http://notdayoftheweek.com/
http://www.amialright.com/
http://nooooooooooooooo.com/
https://greatbignothing.com/
https://zoomquilt.org/
https://dadlaughbutton.com/
https://www.bouncingdvdlogo.com/
http://papertoilet.com/
https://www.window-swap.com/Window
'''


class UselessWebsite(Source):

    def __init__(self):
        self.queue = list(filter(lambda x: x, db.split("\n")))
        self.done = []

    def quota(self):
        return 0.05

    def get(self):
        if not self.queue:
            self.queue = self.done.copy()
            self.done = []

        idx = randrange(len(self.queue))
        website = self.queue.pop(idx)
        self.done.append(website)
        return {
            "type": "website",
            "src": website,
            "content": "",
            "title": "Useless website @%s" % website
        }

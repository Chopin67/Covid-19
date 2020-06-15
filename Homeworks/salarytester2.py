import re
import urllib.request

page = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/')

for line in page:
    text = line.decode('utf-8').strip()
   # print(text)




    def name_to_URL(name):
        fullname = name
        if ',' in name:
            name = name.split(",")
            firstname = str(name[1]).strip()
            lastname = str(name[0])
            fullname = firstname.lower() + '-' + lastname.lower()
            name = fullname
            return fullname
        elif " " in name:

            name = name.split(" ")
            firstname = str(name[0]).strip()
            lastname = str(name[1])
            fullname = firstname.lower() + '-' + lastname.lower()

            if len(name) > 2:
                thirdname = str(name[2])
                fourthname = str(name[3])
                fullname = fullname + '-' + thirdname.lower() + '-' + fourthname.lower()
                name = fullname
            return fullname
        else:
            return fullname


    def report(name):
        name = name_to_URL(name)
        #print(name)
        job = 0
        money = 0
        rank = 0
        try:
            page = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/uva2016/' + name)
            for line in page:
                text = line.decode('utf-8').strip()
                #print(text)
                findjob = re.compile('(<span class="small text-muted" id="personjob">)(.+)(<)')
                findmoney = re.compile('(total gross pay:)(.+)(["])')
                findrank = re.compile('(<tr><td>University of Virginia rank</td><td>)([0-9]*,?[0-9]*)')

                for j in findjob.finditer(text):
                        job = j.group(2)
                        #print(job)
                        if "&amp;" in str(job):
                            job = job.replace("&amp;", "&")

                        elif "&lt;" in str(job):
                            job = job.replace("&lt;", "<")
                        elif "&gt;" in str(job):
                            job = job.replace("&gt;",">")
                        #print(job)
                for m in findmoney.finditer(text):
                         bmoney = str(m.group(2))
                         money = float(bmoney.replace(',','').replace('$',''))
                         #print(money)
                #print(findrank.search(text))

                for r in findrank.finditer(text):


                        #print(r)
                        brank = str(r.group(2))
                        rank = int(brank.replace(',', ''))








            return job, money, rank

        except:

            job = None
            rank = 0
            money = 0
            return job, money, rank





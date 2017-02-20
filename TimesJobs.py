from bs4 import BeautifulSoup
import requests

def souping(url):
    sc=requests.get(url)
    plain_text=sc.text
    soup=BeautifulSoup(plain_text,'html.parser')
    return soup
    

def times_spider(title):
    pages=1
    url='http://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords='+str(title.replace(" ","%20"))+'&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0'+str(title.replace(" ","%20"))+'0DQT0&pDate=I&sequence='+str(pages)+'&startPage=1'
    soup=souping(url)
    num=int(soup.find('span',{'id':'totolResultCountsId'}).text)
    num=num/25   
    count=0
    while pages<=num:   
        url='http://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords='+str(title.replace(" ","%20"))+'&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=0DQT0'+str(title.replace(" ","%20"))+'0DQT0&pDate=I&sequence='+str(pages)+'&startPage=1'
        soup=souping(url)
        for header_tag in soup.find_all('header',{'class':'clearfix'}):
            for tag in header_tag.find_all('h2'):
                if title in tag.text.lower():
                    link =tag.find('a')
                    url2=link.get('href')
                    skillurl='http://www.timesjobs.com'+str(url2)
                    skill_jd_spider(skillurl,title)
                    count+=1
                    print(count)

        pages+=1
        
    print(title+"  = "+str(count))
                


def skill_jd_spider(skillurl,title):
    soup=souping(skillurl)
    skills=""
    for tag in soup.find_all('section',{'class':'jd-skills clearfix'}):
        skills+=tag.text
    f=open(title+" skills.txt","a+")
    f.write(skills)
    f.close
    for jd in soup.find_all('section',{'class':'job-discription'}):
        with open(title+" JD.txt", 'a+', encoding='utf-8') as f:
            print(jd.text, file=f)
        f.close
        

def main():
    title=["software engineer","data scientist","software testing","web designer","software tester","python developer","technical support","android developer","network administrator","java developer"]
    for t in title:
        times_spider(t)      
            
main()

# coding: utf-8

# In[35]:



a1={('آبتین','PERSON'),('دایی','PERSON'),('علی','PERSON'),('آبتین','PERSON'),('آذین','PERSON'),('آرش','PERSON'),
   ('آریانا','PERSON'),('آرتین','PERSON'),('آرشام','PERSON'),
   ('آراز','PERSON'),('آرمين','PERSON'),('آرش','PERSON'),('آزاد','PERSON'),('آريان','PERSON'),('آراد','PERSON'),
   ('آروين','PERSON'),('آرتا','PERSON'),('آريا','PERSON'),('آريو','PERSON'),('آرتان','PERSON'),('ارشيا','PERSON'),
   ('دارا','PERSON'),('اشکان','PERSON'),('الوند','PERSON'),('ايرج','PERSON'),('ارژنگ','PERSON'),('اشکبوس','PERSON'),
   ('دادويه','PERSON'),('اژدر','PERSON'),('انوشيروان','PERSON'),('اشک','PERSON'),('آرشام','PERSON'),('اسفنديار','PERSON'),
 ('دانو','PERSON'),('افشين','PERSON'),('اورمزد','PERSON'),('بابک','PERSON'),('بامشاد','PERSON'),('بهرام','PERSON'),
    ('داريوش','PERSON'),('بهراد','PERSON'),('بهنام','PERSON'),('برومند','PERSON'),('باربد','PERSON'),('برديا','PERSON'),
      ('دادمهر','PERSON'),('بهمن','PERSON'),('بهرنگ','PERSON'),('برسام','PERSON'),('برزين','PERSON'),('بزرگمهر','PERSON'),
      ('دانوش','PERSON'),('بهمنش','PERSON'),('بهزاد','PERSON'),('برزو ','PERSON'),('بهداد','PERSON'),('بهروز','PERSON'),
      ('داراب','PERSON'),('به‌آيين','PERSON'),('بيژن','PERSON'),('برنا','PERSON'),('بهبد','PERSON'),('تيرداد','PERSON'),
      ('دياکو','PERSON'),('بهشاد','PERSON'),('برزن','PERSON'),('برسام','PERSON'),('برزين','PERSON'),('بزرگمهر','PERSON'),
     ('رادين','PERSON'),('تهماسب','PERSON'),('تهمورث','PERSON'),('تابان','PERSON'),('تهمتن','PERSON'),('تورج','PERSON'),
   ('رستان','PERSON'),('جاماسب','PERSON'),('جاويد','PERSON'),('جهانگير','PERSON'),('جهانگير','PERSON'),('جمشيد','PERSON'),
    ('رامين','PERSON'),('جهان‌بخش','PERSON'),('جهاندار','PERSON'),('چنگيز','PERSON'),('چيا ','PERSON'),('خداداد','PERSON'),
     ('رامان','PERSON'),('خدابخش','PERSON'),('خسرو','PERSON'),('خوبيار','PERSON'),('خدايار','PERSON'),('خشايار','PERSON'),
    ('آيت الله','PERSON'),('هاشمي','PERSON'),('رفسنجاني','PERSON'),
     ('رها','PERSON'),('رستم','PERSON'),('رامبد','PERSON'),('روزبه','PERSON'),('رايان','PERSON'),('رهام','PERSON'),
     ('سالار','PERSON'),('ريونيز','PERSON'),('رخشان','PERSON'),('رادمان','PERSON'),('رايکا','PERSON'),('راد','PERSON'),
         ('سامان','PERSON'),('ريکا','PERSON'),('زال','PERSON'),('زاوش','PERSON'),('زند','PERSON'),('زرمهر','PERSON'),
       ('پروفسور','PERSON') ,('دکتر','PERSON') ,('آقا','PERSON' ),('خانم','PERSON') ,('مشاور','PERSON') ,('مهندس','PERSON') ,
('بيماري','SICKNESS' ),('هپاتيت','SICKNESS' ),('ايدز','SICKNESS' ),('سندرم','SICKNESS' ),('سرطان','SICKNESS' ),
     ('سيستان-و-بلوچستان','LOCATION'),('مرکز','LOCATION'),('کرانه-باختري','LOCATION'),('مجارستان','LOCATION'),
               ('استاد','PERSON'), ('تقوي','PERSON'),('قلي','PERSON'),
   ('سپهر','PERSON'),('سورنا','PERSON'),('سهراب','PERSON'),('سياوش','PERSON'),('ساسان','PERSON'),('سام','PERSON'),
    ('سپنتا','PERSON'),('سهند','PERSON'),('سيروس','PERSON'),('سروش','PERSON'),('سورن','PERSON'),('سوشيانس','PERSON'),
    ('سيامک','PERSON'),('سينا','PERSON'),('شادمهر','PERSON'),('شايا','PERSON'),('شهرام','PERSON'),('شهريار','PERSON'),
     ('شهبد','PERSON'),('شيروان','PERSON'),('شروين','PERSON'),('شايان','PERSON'),('شاهکام','PERSON'),('شهروز','PERSON'),
      ('شاهرخ','PERSON'),('شهراد','PERSON'),('شيرزاد','PERSON'),('شاهين','PERSON'),('شهاب','PERSON'),('شيرنگ','PERSON'),
      ('شاپور','PERSON'),('شهرداد','PERSON'),('شهيار','PERSON'),('فرزان','PERSON'),('فرزام','PERSON'),('فرهاد','PERSON'),
     ('فيروز','PERSON'),('فربد','PERSON'),('فرسا','PERSON'),('فرزين','PERSON'),('فرنام','PERSON'),('فرشاد','PERSON'),
    
    ( 'آقايان','PERSON'),('خانم','PERSON'),('جنابان','PERSON'),('آقاي','PERSON'),('جناب','PERSON'),('خانم','PERSON'),
    ( 'سرکار','PERSON'),('سلطان','PERSON'),('سرتيپ','PERSON'),('سرهنگ','PERSON'),('سردار','PERSON'),('سرگرد','PERSON'),
      ('سروان','PERSON'),('دريادار','PERSON'),('گروهبان','PERSON'),('ژنرال','PERSON'),('شهيد','PERSON'),('مرحوم','PERSON'),
       ('مرحومه','PERSON'),('بابا','PERSON'),('مامان','PERSON'),('شادروان','PERSON'),('علامه','PERSON'),('امام','PERSON'),
        ('آيت','PERSON'),('حضرت','PERSON'),('کربلايي','PERSON'),('حاج','PERSON'),('دايي','PERSON'),('خاله','PERSON'),
     ('زنجاني','PERSON'),('مقام','PERSON'),('معظم','PERSON'),('رهبري','PERSON'),('خردبين','PERSON'),('عمه','PERSON'),
        ('آذربايجاي','LOCATION'),('غربي','LOCATION'),('قفقاز','LOCATION'),('تبت','LOCATION'),('قره','LOCATION'),
          ('باغ','LOCATION'),('آسيا','LOCATION'),('اروپا','LOCATION'),('اردبيل','LOCATION'),('آمريکا','LOCATION'),
              ('جنوبي','LOCATION'),('شمالي','LOCATION'),('جنوب','LOCATION'),('شرق','LOCATION'),('غرب','LOCATION'),
              ('شمالي','LOCATION'),('غرب','LOCATION'),('اوراسيا','LOCATION'),('افريقا','LOCATION'),('خاورميانه','LOCATION'),
              ('خاوردور','LOCATION'),('جمهوري','LOCATION'),('کنگو','LOCATION'),('آرژانتين','LOCATION'),('مرکز','LOCATION'),
              ('مرکزي','LOCATION'),('آلباني','LOCATION'),('آلمان','LOCATION'),('آندورا','LOCATION'),('آنگولا','LOCATION'),
              ('اتريش','LOCATION'),('اتيوپي','LOCATION'),('اردن','LOCATION'),('ارمنستان','LOCATION'),    
   ('اروگوئه'),('LOCATION'),
              ('ازبکستان','LOCATION'),('اسپانيا','LOCATION'),('استراليا','LOCATION'),('استوني','LOCATION'),('اسرائيل','LOCATION'),
              
              ('غزّه','LOCATION'),('غزه','LOCATION'),('اسلواکي','LOCATION'),('اسلووني','LOCATION'),('افغانستان','LOCATION'),
              ('الجزاير','LOCATION'),('امارات','LOCATION'),('متحده','LOCATION'),('عربي','LOCATION'),('اندونزي','LOCATION'),
              ('اوکراين','LOCATION'),('اسپانيا','LOCATION'),('ايالات','LOCATION'),('متحده','LOCATION'),('ايتاليا','LOCATION'),
              ('ايرلند','LOCATION'),('باهاما','LOCATION'),('بحرين','LOCATION'),('برزيل','LOCATION'),('بريتانيا','LOCATION'),
              ('انگلستان','LOCATION'),('بلاروس','LOCATION'),('بلژيک','LOCATION'),('بلغارستان','LOCATION'),('بنگلادش','LOCATION'),
              ('بورکينافاسو','LOCATION'),('بوسني','LOCATION'),('هزرگوين','LOCATION'),('بوليوي','LOCATION'),('بوتان','LOCATION'),
              ('پاناما','LOCATION'),('پرتغال','LOCATION'),('پرو','LOCATION'),('پاکستان','LOCATION'),('تايلند','LOCATION'),
              ('چين','LOCATION'),('ترکمنستان','LOCATION'),('ترکيه','LOCATION'),('توباگو','LOCATION'),('تونس','LOCATION'),
              ('چک','LOCATION'),('دومينيکن','LOCATION'),('جيبوتي','LOCATION'),('دانمارک','LOCATION'),('چاد','LOCATION'),
              ('روسيه','LOCATION'),('شوري','LOCATION'),('استراليا','LOCATION'),('زامبيا','LOCATION'),('نيوزيلند','LOCATION'),
              ('زلاندنو','LOCATION'),('ژاپن','LOCATION'),('سودان','LOCATION'),('سوريه','LOCATION'),('سنگال','LOCATION'),
              ('سوئد','LOCATION'),('سوئيس','LOCATION'),('سومالي','LOCATION'),('استوني','LOCATION'),('شيلي','LOCATION'),
              ('عربستان','LOCATION'),('عمان','LOCATION'),('فرانسه','LOCATION'),('استوني','LOCATION'),('فلسطين','LOCATION'),
              ('فنلاند','LOCATION'),('فيليپين','LOCATION'),('قبرس','LOCATION'),('قرقيزستان','LOCATION'),('قطر','LOCATION'),
              
               ('کامرون','LOCATION'),('کانادا','LOCATION'),('کامبوج','LOCATION'),('کره','LOCATION'),('کرواسي','LOCATION'),
               ('کاستاريکا','LOCATION'),('کلمبيا','LOCATION'),('کوبا','LOCATION'),('کويت','LOCATION'),('گرجستان','LOCATION'),
               ('گرنادا','LOCATION'),('گينه','LOCATION'),('لبنان','LOCATION'),('لهستان','LOCATION'),('ليبريا','LOCATION'),
               ('ليبي','LOCATION'),('مالديو','LOCATION'),('مالي','LOCATION'),('ليختن‌اشتاين','LOCATION'),('مالزي','LOCATION'),
               ('مجارستان','LOCATION'),('مراکش','LOCATION'),('مصر','LOCATION'),('مغولستان','LOCATION'),('مقدونيه','LOCATION'),
               ('مکزيک','LOCATION'),('موريتاني','LOCATION'),('مولداوي','LOCATION'),('موناکو','LOCATION'),('ناميبيا','LOCATION'),
               ('نپال','LOCATION'),('نروژ','LOCATION'),('نيجر','LOCATION'),('واتيکان','LOCATION'),('ويتنام','LOCATION'),
               ('هلند','LOCATION'),('هند','LOCATION'),('هندوراس','LOCATION'),('يمن','LOCATION'),('يونان','LOCATION'),
               ('باغ','LOCATION'),('ارم','LOCATION'),('شهربازي','LOCATION'),('سد','LOCATION'),('خانه','LOCATION'),
               ('پل','LOCATION'),('رودخانه','LOCATION'),('رود','LOCATION'),('قاره','LOCATION'),('کشور','LOCATION'),
               ('اقيانوس','LOCATION'),('قلعه','LOCATION'),('کوه','LOCATION'),('دامنه','LOCATION'),('کوهپايه','LOCATION'),
              ('جواد','PERSON') ,('ظريف','PERSON') ,('باراک','PERSON') ,('اوباما','PERSON') ,('امام','PERSON') ,('خميني','PERSON') ,
              ('خامنه‌اي','PERSON' ),('زلاتان‌ابراهيمويچ','PERSON') ,('محمود‌احمدي','PERSON') ,('جورج‌','PERSON') ,('کمال الملک ','PERSON') ,'زلاتان','PERSON' ,
              ('مارک تواين','PERSON') ,('سيمين بهبهاني','PERSON') ,('زلاتان','PERSON' ),('زلاتان','PERSON' ),('زلاتان','PERSON') ,
              ('آدلف‌ هيتلر','PERSON' ),
              ('Canada','LOCATION'),
    ('شرقي','LOCATION'),  ('آذربايجان','LOCATION'), ( 'وين','LOCATION'),  ('سالزبورگ','LOCATION'),  ('گراتس','LOCATION'),
   ('کشور','LOCATION'),
         ('لينتز','LOCATION'),  ('آديس-آبابا','LOCATION'),  ('بوئنوس-آيرس','LOCATION'),  ('باهيابلانکا','LOCATION'),  
   ('روزاريو','LOCATION'),  ('کشور','LOCATION'), 
   ('مندوزا','LOCATION'),  ('پارانا','LOCATION'),  ('کوردوبا','LOCATION'),  ('کورينتس','LOCATION'),  ('رزيستنسيا','LOCATION'),
   ('ايروان','LOCATION'),
    ('ريورا','LOCATION'),  ('مادريد','LOCATION'),  ('بارسلون','LOCATION'),  ('بيلبائو','LOCATION'),  ('تاشکند','LOCATION'),
   ('پامپلونا','LOCATION'),
    ('زاراگوزا','LOCATION'),  ('سويل','LOCATION'),  ('کوردوبا','LOCATION'), ( 'مايورکا','LOCATION'),  ('والنسيا','LOCATION'), 
   ('وايادوليد','LOCATION'),('مهران','PERSON'),('مدیری','PERSON'),
     ('سيدني','LOCATION'),  ('ملبورن','LOCATION'),  ('اورشليم','LOCATION'), ('ژوهانسبورگ','LOCATION'),  ('قندهار','LOCATION'),
   ('کابل','LOCATION'),
     ('زلاتان','PERSON' ),('ابراهيمويچ','PERSON' ),('حسن','PERSON') ,('روحاني','PERSON') ,('محمود','PERSON' ),('احمدي','PERSON') ,
   ('نژاد','PERSON') ,
   ('مجلس','ORG'), ('دولت','ORG'), ('سيدني','ORG'), ('صداوسيما','ORG'), ('دستگاه-قضايي','ORG'), ('دستگاه','ORG'), 
   ('سازمان محيط زيست کشور','ORG'),
   ( 'شوراي','ORG'),  ('شورا','ORG'),  ('اسلامي','ORG'), ('باشگاه','ORG'), ('راه آهن','ORG'), ('پرسپوليس','ORG'),('تيم','ORG'),
    ('کشور','LOCATION'), ('قاره','LOCATION'), ('جزيره','LOCATION'), ('استان','LOCATION'), ('شهر','LOCATION'), 
   ('روستا','LOCATION'), ('ناحيه','LOCATION'),
    ('فهام','PERSON'),('اميد','PERSON'),('ارس','PERSON'),('افراسياب','PERSON'),('انوش','PERSON'),('اردشير','PERSON'),
       ('حسين','PERSON'), ('آريامنش','PERSON'),('آترين','PERSON'),('آرام','PERSON'),('آرمان','PERSON'),('آريوبرزن','PERSON'),
                                                                   ('آريامهر','PERSON'),
 ('اصلاحي','PERSON') ,('زهرا','PERSON') , ('رضا','PERSON'), ('بردسکن','LOCATION'), ('تهران','LOCATION'), ('ايران','LOCATION'),
                 ('مشهد','LOCATION') , ('علي','PERSON'), ('آنفولانزا','SICKNESS') ,('سرطان','SICKNESS'),('تبریز','LOCATION')
                                                              } 
import sys
import io
o=[]
o1=[]
o2=[]
import json

searchTerm='N'
s1='Ne'
s2='AJe'
output_list = []
a1=tuple(a1)
id1=0
import codecs
import os
from shutil import copyfile

from shutil import copyfile



copyfile(os.path.join( '%s\\TabText\\libs\\'%  os.environ['APPDATA'] +'outpos2.txt'), 'outpos2.txt')

in1='outpos2.txt'
f = codecs.open(in1, 'r', 'UTF-8')

import datetime

dat1 = str( datetime.datetime.now() )
sub1={}
sub1['Description']=None
sub1['FileName']=in1
sub1['RunDate']=dat1
for line in f:
    tu=tuple(line.split(','))
   
    sub_dict = {}
    sub_dict['id'] = id1
    a=str(tu[1].replace(')',''))
    sub_dict['Token'] = tu[0]
    
    sub_dict['POS-Tagg'] =a
    sub_dict['Type'] = 'Persian' 
    sub_dict['NER']='OO'
    if searchTerm in sub_dict['POS-Tagg'] or s1 in sub_dict['POS-Tagg'] or s2 in sub_dict['POS-Tagg']:    
        o.append(sub_dict['Token'])
        o2.append(sub_dict['id'])
        str(o)
        
        for s in o:
            for j in a1:
                if j[0] in str(s):    
                    sub_dict['NER'] = j[1]
  
    output_list.append(sub_dict) 
    id1=id1+10
import json
import sys
kol=[]
kol.append(sub1)
kol.append(output_list)
with io.open('data_struct2.json', 'w', encoding='utf8') as json_file:
                json.dump(kol, json_file,indent=4, ensure_ascii=False)
filename = 'data_struct2.json'
with  open(filename,'r',encoding='utf-8') as f1:
    with open(sys.argv[2],'w',encoding='utf-8') as f2:
        for line in f1:
            f2.write(line.replace('"NER": "ر"','"NER": "OO"'))
        for line in f1:
            f2.write(line.replace('"NER": "ل"','"NER": "OO"'))    
              
f1.close()
f2.close()




# In[30]:






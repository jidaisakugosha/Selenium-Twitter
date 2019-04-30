#!/bin/sh
username=$1
password=$2
da=$( date | awk '{ print $2 $3}') ; \
da1=$(echo $da | awk -F'月'  '{print $1}') && \
da2=$(echo $da | awk -F'月'  '{print $2}' | awk -F'日'  '{print $1}') && \
echo ${da1}月${da2}日
python3 ~/Downloads/Selenium-Twitter/program.py "７時になりました。"$da"の休講情報をお知らせします。" $username $password &&  \
rm -f index.html && wget http://www.c.u-tokyo.ac.jp/zenki/classes/cancel/index.html && \
cat index.html | grep -n  ${da1}月${da2}日 | awk -F':' '{print $1}' | \
xargs -I@  awk 'NR=='@'+1||NR=='@'+2||NR=='@'+3||NR=='@'+4 {print $0}' index.html  | \
awk -F'>' '{print $2}' | awk -F'<' '{print $1}' | xargs -I@ echo @ | xargs -L 4 |xargs -I@   python3 ~/Downloads/Selenium-Twitter/program.py "$da @" $username $password  && \
python3 ~/Downloads/Selenium-Twitter/program.py $da"の休講情報は以上です。"  $username $password



LOG=/var/log/ssd_trim.log
echo "*** $(date -R) ***" >> $LOG
fstrim -v / >> $LOG
fstrim -v /home >> $LOG

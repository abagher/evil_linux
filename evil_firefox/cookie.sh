#echo "Delivering a fresh batch of cookies!" | mutt -a /home/saurabh/.kde/share/apps/kcookiejar/cookies -s "Fresh delivery of cookies!" ssingh02@bu.edu
python sql.py > cookies.txt
echo 'Here is a fresh batch of tasty session cookies!' | mailx -s 'Fresh batch of cookies!' -A /home/saurabh/cookies.txt ssingh02@bu.edu

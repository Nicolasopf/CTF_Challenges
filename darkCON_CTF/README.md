# CTF darkCON Feb 22, Writeup OSINT The Reporter

"Miss Lola beck has something on her social media account. You are Agent P. find the secret." Hint : username l.beck

With the hint of the username, I did at first a check with sherlock (Sherlock is a tool to search for accounts that have X username in many websites.), just to see if I can see something.

So, running sherlock we get this:
```
└─$ python3 sherlock l.beck                                                               2 ⨯
[*] Checking username l.beck on:
[+] About.me: https://about.me/l.beck        # WE HAVE INTEREST IN THIS                                                 
[+] AllTrails: https://www.alltrails.com/members/l.beck                                       
[+] Apple Discussions: https://discussions.apple.com/profile/l.beck                           
[+] Duolingo: https://www.duolingo.com/profile/l.beck                                         
[+] Euw: https://euw.op.gg/summoner/userName=l.beck                                           
[+] EyeEm: https://www.eyeem.com/u/l.beck                                                     
[+] Facebook: https://www.facebook.com/l.beck                                                 
[+] FortniteTracker: https://fortnitetracker.com/profile/all/l.beck       # AND IN A NORMAL CASE, ALSO IN THIS                    
[+] HackerRank: https://hackerrank.com/l.beck                                                 
[+] ICQ: https://icq.im/l.beck                                                                
[+] Kik: https://kik.me/l.beck                                                                
[+] NameMC (Minecraft.net skins): https://namemc.com/profile/l.beck
```

The about.me is very interesting https://about.me/l.beck
We get in her description:

```
Hi, I am Lola.
Experiences
* Freelancer,
* Reporter.
Recent News:
" Teen Detained For Cyber Crime At Coffee Shop Chain. "
I have managed to get this text:
725f37626f6e6e6965
```

We can see an interesting text that he get, and it seems that is HEX (Because there is only digits and letters from A-F)
We can decode it at https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')

As you can see, you get r_7bonnie, at first moment i thought it was some kind of password, so I tried to login in facebook and twitter with the username.
I failed, so I tried to search it in google, if you do it, you will see a reddit user with that username.
Let's see what is she posting.

An interesting post from her, is this https://www.reddit.com/user/r_7bonnie/comments/lmrxae/here_get_something_you_want/
We can see a short video / images flash. We can replay the video and see there is a kind of QR code, so I tried to capture it with my cellphone, but that not worked.

So, I tried https://ezgif.com/video-to-jpg to get all the images from the video, I downloaded the QR image and did scan it from a website.
I used https://www.codigos-qr.com/lector-qr-online/ and after you upload the QR, you will get the flag.

darkCON{os1nst_1s_nic3}

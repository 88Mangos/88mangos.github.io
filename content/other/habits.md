---
title: "Phone Shortcuts and Automations"
date: 2026-05-13
updated: 2026-05-13
ShowToc: true
TocOpen: true  # Optional: Keep it open by default
---

I've recently deleted YouTube and Instagram, and now only use them on my computer. As a result I have been picking up my phone and then doing nothing a lot more, so I figure I'd try to automate away as many things as I can to reduce the number of things I need to do on my phone.

I categorize these automations and shortcuts into three types:
1. Settings, i.e., things you can do in the Settings app in iOS 26
2. App Automatic Notifications, i.e., things that apps let you do
3. Shortcuts/Automations, i.e., things in the Shortcuts app.

The productivity apps that I use (and follow) are:
1. Habo [[GitHub Link]](https://github.com/xpavle00/Habo)
2. Data Jar [[Link]](https://datajar.app/)
3. Focus Friend [[Link]](https://www.yourfocusfriend.com/)
4. Default Apple Shortcuts App


# Settings Automations
1. Night shift (warm colors) auto scheduled from 9 PM to 7 AM. Just to reduce eye strain or smth like that.

# App Automatic Notifications
1. Habo prompts me to check my habits every night.

# Shortcuts/Automations

## Automatically prompt me for my daily Snapstreak and Duolingo streaks.
At 12 AM, I have an automation to reset the snap and Duolingo streak booleans in Data Jar. 

Then, I have automations that run whenever I close Snapchat/Duolingo:
1. [Data Jar] Get Value for Habits.duolingo/snapstreak
2. If [select var from prev thing], stop this shortcut
3. End If
4. Choose from Menu: "Did you extend your streak?"
  - Yes: 
    - Text "True", 
    - [Data Jar] Set Value for Habits.duolingo/snapstreak to the Text above 
  - No:
  - End Menu

While building this, I was prompting Google Gemini to figure out how to make these shortcuts (in fact, Gemini told me about Data Jar) and I found out that Duolingo has APIs for all users at `https://www.duolingo.com/users/[YOUR USERNAME HERE]`. Thankfully, it seems like you have to be logged in to access the data, which is a mountain of JSON.

## Study 
I use Focus Friend because I like the little bean and the house, and also because Hank Green is pretty cool (grew up watching Crash Course).

So the gist is I saw this Instagram Reel [[Link]](https://www.instagram.com/p/DNG56h7xvHF/?img_index=1) talking about how chillin for a bit before you study makes you better somehow. So I made a shortcut that's on my home screen:
1. Show alert "Close your eyes and breathe"
2. wait for 120 seconds
3. Vibrate the device
4. turn on Personal Focus mode to silence a lot of notifs while I'm locked in
5. open Focus Friend

## Bored?
To give me something to click on when I'm truly bored, the shortcut does the following:
1. [Data Jar] Get Value for Habits.snapstreak
2. If not snapstreak, Show alert "Send a snap!" and open Snapchat
3. [Data Jar] Get Value for Habits.duolingo
4. If not snapstreak, Show alert "Do some Duolingo!" and open Duolingo
5. Choose from Menu: Practice Something!
- play cryptograms (c.f. Codebusters, Science Olympiad days)
- Open the relevant note to practice things that I want to learn

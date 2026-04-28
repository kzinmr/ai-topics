---
title: "Using Signal groups for activism"
url: "https://micahflee.com/using-signal-groups-for-activism/"
fetched_at: 2026-04-28T07:02:43.766816+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Using Signal groups for activism

Source: https://micahflee.com/using-signal-groups-for-activism/

Things are heating up. Millions of people are taking to the streets against Trump's rising authoritarianism. Communities around the US are organizing to defend against ICE raids, to protest Israeli genocide, for mutual aid, and for other forms of fighting fascism. Signal can help people safely organize in all of these contexts.
Signal groups, in particular, are more powerful than you might be aware of, even if you already use them all the time. In this post I'll show you how to:
Turn an in-person meeting into a Signal group using QR codes
Manage large semi-public groups while still vetting new members
Make announcement-only groups, perfect for volunteer networks rapidly responding to things like ICE raids
Why Signal?
When police, federal agencies, or fascists in Congress launch an investigate into activists that they want to crush, one of their primary tools for learning exactly who everyone involved is, what their roles are, and what their plans are, are
data requests
.
Police can send data requests to companies like Google, Apple, Meta, and even Signal, demanding that these organizations hand over user data. Even when companies try to legally challenge these requests (and they mostly don't even try), they're generally forced to comply anyway. For example, check out Proton's transparency report: Proton
handed user data
to governments over 10,000 times in 2024.
Given this, activists use and trust Signal over other messaging apps for a few reasons:
Signal is encrypted.
If police send data requests to Signal, they can't hand over your conversations. But if police send data requests to your cell phone carrier, or Instagram, Bluesky, or your favorite Mastodon server, they
can and likely will
hand over your DMs. (If you use Twitter DMs not only will they share your messages with the police, Elon Musk might personally share them with neo-Nazis too.)
Signal can't access user metadata.
It's not just that Signal promises not to keep logs. They've literally engineered their service to cryptographically prevent themselves from having access to metadata, even if they wanted to. Signal doesn't know what groups you're in, or even what Signal groups exist on the platform. They don't know the names or membership of any Signal group. They can't even access your profile picture or name. All of this is stored on user devices and shared directly from user to user. On the other hand, if WhatsApp gets a data request, Meta will turn over details about everyone in your group, exactly who sends messages to who, and when, because WhatsApp collects all of this.
Signal doesn't share your phone number with other members of the groups you're in
(by default). This makes it considerably safer to join large activist groups where you don't know or trust everyone involved, and where there might be an infiltrator. If you join a large WhatsApp group, anyone in that group will have everyone else's phone number, and they can use that to learn far more about everyone's identities.
Signal is easy to use.
It's as easy as any of the commercial apps. Only unlike the commercial apps, Signal is free, open source, non-profit, and significantly more private. You just install the app, register an account, and you can start messaging privately, and join Signal groups, right away.
Like all the other companies, governments requests user data from Signal too. Signal fights them in court, with help from the ACLU. If they're forced to comply anyway, they hand over only a tiny amount of data, because it's all they have access to: the timestamp for when the Signal account was registered, and when it last logged in. That's it.
💡
Signal publishes details about data requests on the
bigbrother page
of their website, if you're interested in the details.
There are ways to communicate that are potentially more secure and private than Signal, like that don't require a phone number, or that force your traffic over Tor, or that aren't managed by central servers hosted in big public cloud providers, etc. However, none of them are as user friendly as Signal.
For large and diverse mass movements, especially with people who are young and old, who maybe don't have access to computers and only have their phone, and who have no time or patience for a learning curve, Signal is a really good option. If the chat platform isn't easy for everyone to use, then many people will just not use it, and fallback to Instagram DMs or whatever is most comfortable.
While trying to get people to figure out how to have encrypted chats on your self-hosted Matrix server or whatever might be appropriate in some circumstances, a Signal group is a million times simpler for most people.
Permissions and group links
By default, the person who created a Signal group is the admin and everyone else in the group is just a member. Everyone can add new members, edit the name and avatar of the group, send messages, and set disappearing messages, but only the admin can kick someone out of the group.
But Signal groups support so much more: specifically, group links and permissions.
If you're the admin of a Signal group, tap the name of the group to get to group settings. From here, you'll see links for
Group Link
,
Requests & Invites
, and
Permissions
.
Group Link is disabled by default. If you enable it, it looks like this:
Group Link settings in Signal
Now, people can load that
https://signal.group/
URL to join your group. You can make completely public Signal groups if you want – they support up to 1,000 people.
However, for most organizing where you don't want a public group, you should turn on
Require Admin Approval
. Now whenever someone joins the group, you get the chance to decide if you want to let them in before they join.
If you click the
Share
button, you can choose
QR Code
, which displays the group link as a QR code on your phone's screen. I'll go over this more below.
Back in the group settings, look at
Requests & Invites
, you'll see a list of everyone who has tried to join your group and is waiting to be approved. You can approve them or deny them here. You can also see who you (or other members of your group) have invited to join.
Back in the group settings, look at
Permissions
. Here's what it looks like:
Editing group permissions in Signal
Signal groups have two roles: admins and everyone else. You can decide what everyone can do versus what only admins can do. By default, all members can do everything.
What settings you should choose depends on what you're doing. As you'll see, these simple settings turn out to be surprisingly versatile.
Turning an in-person meeting into a Signal group with QR codes
Let's say a group of people in your community meets in person around some issue (like, say, local Jews who want to stop Israel's genocide in Gaza). You meet new people and discuss future projects, and maybe set a date for the next meeting. But what if you want to keep the group in communication between meetings?
Here's what you should do:
Ask everyone who isn't already a Signal user to install Signal and register an account.
Create a new Signal group. Make sure to turn on disappearing messages.
Go to the group settings >
Group Link
, and turn on
Group Link
.
In group settings >
Group Link
, choose
Share
>
QR Code
. A QR code with the group link will be displayed on your phone.
Have everyone open the default Camera apps on their phone, point it at your QR code, and tap the link. This will add them to the group.
After everyone has joined the group, go to group settings >
Group Link
, and this time turn on
Require Admin Approval
. Now, if anyone else joins the group link, you need to actively approve them.
Depending on your group, you might also want to adjust the permissions, from group settings >
Permissions
. Like, you may wish to restrict it so only admins can add new members, and maybe make a few other people admins.
And that's it. You now have a Signal group from an in-person meeting so you can keep in touch between meetings!
If police send a data request to Signal demanding user data for anyone in the group, Signal will not have any data to give them. They won't even know the group exists, much less its name and membership.
💡
True story: I followed these exact steps at a local meeting of Jews who want to stop Israel's genocide of Palestinians in Gaza, and now we have a Signal group.
Semi-public group chats, but with vetting
I'm in a Signal group with about 500 people from around the world that focuses on digital rights. I've known some people in the group for years, but others I've never met. Still, it's a safe place to discuss human rights tech issues without worrying about infiltration by fascists.
The rules include, "Be cool and be kind, or be kicked out," and "New members need to be vouched for by an existing member." There are five admins. If I have a friend who I think would be good to add to the group, I can invite them, and then vouch for them in the group, and one of the admins can let them in. If someone tries joining and no one vouches for them, they don't get let in.
Signal groups make it possible to have semi-public, but still incredibly private, spaces like this. If we want to grow movements, we need to welcome many, many more people. Everyone isn't going to know and trust everyone else, so a simple rule like "you need an existing member to vouch for you" is a great way to keep out the riff-raff. You can always choose to make more strict rules if you want, like requiring two people to vouch for new members.
Here's how to make a Signal group semi-public, but with vetting:
Go to group settings, and right beneath the group name, tap the description. Write a description that describes your group and what the rules for membership are.
Go to group settings >
Group Link
. Turn on
Group Link
, and also turn on
Require Admin Approval
.
Go to group settings >
Permissions
. Change Add Members and Edit Group Info to
Only Admins
, but keep Send Messages to
All Members
.
Go to group settings, and pick some other members of the group to make admins. It's good to have more than one admin, to share the responsibilities of moderation and letting new members in after they've been vouched for.
What's cool about this being a Signal group as opposed to something like a Discord server is that it's all private, and it can't be shared with law enforcement.
Signal's servers have no way of knowing who is in the group, or even that the group exists, much less what people are saying. When someone sends a message to the group, from the perspective of the server, it's just 500 encrypted text messages moving through its service.
💡
True story: It hasn't really been active lately, but I made a semi-public Signal group like this for discussing the
Paramilitary Leaks dataset
.
Announcement-only lists, perfect for rapid response networks
I volunteer with a regional rapid response network that aims to protect our communities from ICE kidnappings. It's built around an announcement-only Signal group which has hundreds of volunteers in it. Before joining the Signal group, you need to take a training where you learn how to do immigration enforcement cop watching.
When people see what looks like unmarked law enforcement vehicles, or chuds with face masks, or a police checkpoint, they understandably get scared. It's common for them to post to social media that they think they saw ICE in a specific neighborhood, and this gets shared widely. The problem is, the majority of the time it's not actually ICE, and spreading unverified rumors encourages already scared people to panic. It also doesn't do anything to give legal support to the people targeted by ICE.
Instead, my regional group runs an ICE hotline phone number. If you think you saw ICE, DHS, or other federal activity, you call or text this phone number with details of what you saw and where. (Since we're relying on the public to report ICE sightings, this is just a normal phone number accepting SMS messages and voice calls.)
Admins of the Signal group monitor the hotline number all day. When a report comes in, an admin sends it to the announcement Signal group. Members of the group don't have permissions to post messages, but we can use emoji. When an admin someone writes a message like, "Caller reported ICE at Walmart in [insert town name]," the volunteers can respond with 👍 if they can go check it out and 👎 if they can't.
While volunteering to confirm an ICE sighting, you communicate via Signal with the admin who posted the message. If you confirm it's actually an immigration action, the rapid response network will share the verified info with local communities using social media, and they might post in the announcement Signal group requesting reinforcements.
Here's how to create an announcement-only Signal group:
Go to group settings >
Group Link
. Turn on
Group Link
, and also turn on
Require Admin Approval
.
Go to group settings >
Permissions
. Change Add Members, Edit Group Info, and Send Messages to
Only Admins
.
Go to group settings, and pick whoever should be authorized to send messages to the group and make them admins.
That's it. I'm in an announcement group specifically for rapid response to ICE raids, but there are many other use cases too.
For example, check out
Sunbird
, an announcement-only Signal group for organizing Palestine solidarity actions in Austin, Texas. "Our intention is to serve as an anonymous, real-time announcement and coordination platform to foster greater participation and activity from everyone who is involved in the struggle for the liberation of Palestine," a Sunbird organizer
told
CrimethInc.
The Sunbird collective created a dedicated anonymous Signal account to admin the group (well, groups – they quickly exceeded the 1,000 member limit and had to make multiple Signal groups). Members of the community can send messages to the Sunbird account, which vets them and anonymously forwards them to the larger announcement groups.
I'm hoping this post encourages people to organize in safer ways, and to utilize Signal's incredible versatility to organize locally to fight fascism. Stay safe.
Sign up for micahflee
Hi, I'm Micah. I'm a coder, a journalist, and I help people stay private and secure.
No spam. Unsubscribe anytime.

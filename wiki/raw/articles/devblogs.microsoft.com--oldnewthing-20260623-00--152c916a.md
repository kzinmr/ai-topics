---
title: "Microspeak elaborated: Isn't escrow just a release candidate by another name?"
url: "https://devblogs.microsoft.com/oldnewthing/20260623-00/?p=112462"
fetched_at: 2026-06-25T07:01:40.031951+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Microspeak elaborated: Isn't escrow just a release candidate by another name?

Source: https://devblogs.microsoft.com/oldnewthing/20260623-00/?p=112462

I had earlier introduced the Microspeak term
escrow
to refer to the declaration that a particular build of the product is going to be the one that ships to customers if it meets certain quality and reliability targets.
Some people wondered, “Isn’t that just a release candidate? Why do you Microsoft people have to make up new names for things that already have perfectly good names?”
Yes, the Microspeak term
escrow
corresponds to what most people call a
release candidate
, but we don’t call it a release candidate because that name is used for some other purpose.
I wrote about this quite some time ago, but it was for the now-defunct
TechNet Magazine
, not for the blog, which means that it doesn’t show up in a blog search.
Here’s the final draft of that column. Now that I’ve put it on the blog, people can find it more easily.
Back in the old days of Windows, prerelease versions of the product followed a fairly standard progression. First up were the alpha releases, which were used internally and possibly shared with software partners outside of the Windows product team. Actually, to be quite honest, I never remember them being called alpha releases—they just were just called something boring like internal prerelease or simply named after the build number or project milestone that produced them. For example, Windows 95 prereleases went by names such as Build 81 and M3.
After alpha releases, there naturally come beta releases, which were sent to a somewhat broader audience. One major difference between alpha and beta releases is that beta releases include people who aren’t software developers, such as end users who like testing prerelease software and corporations who want a head start on evaluating the new operating system to determine the compatibility of the new product not only with their critical in-house applications but also with their corporate network, standard hardware configurations, and system management tools.
Finally, you had release candidates. These were, as the name suggests, versions of the code that were candidates for final release. In other words, “If everything goes well, we’re shipping this puppy.” If some horrific bug was found that invalidated this expectation, then as soon as the bug was fixed, a new release candidate build was
spun up
, and the test cycle restarted. Windows 95 shipped its sixth release candidate.
I’m told that the Windows NT folks followed the same release naming pattern, but they ran into a problem: corporations didn’t bother testing their critical applications against beta releases of Windows NT. The logic generally went something like this: “Why bother? It’s just a beta. Betas are for fanboys. It’ll all be different in the final version anyway. Any testing we do now would just be a waste of time.” Similarly, software companies paid no attention to issues found during the beta testing of Windows NT. “We don’t support beta operating systems,” they would respond.
These companies would start testing in earnest once the actual release candidate builds came out. And they’d inevitable find a bunch of problems. Some were problems the companies could address on their own while other issues were more complex and had to do with Windows NT not being “compatible enough” with the previous version of the OS. Some problems were comparatively minor issues with the way a particular project feature worked, and some could be fixed in a short period of time. Meanwhile, other problems were so serious that the release management team agreed that it was necessary to delay the product’s release so the product team could resolve the problem.
These release candidate builds also generated a lot of suggestions. We received feedback such as, “we think the UI would look better if you arranged the buttons this way” and “rephrasing this message would be less confusing for our employees.” Those would have been great suggestions had they only arrived during the beta phase, but by the time the first release candidate is rolled out, it’s far too late to make changes to the visuals. The documentation and help files have already been written, the product has been translated into dozens of languages, and the screenshots for the manual and product box have already been laid out, tuned, color-separated, and printed. All that work isn’t going to be thrown out and redone just to move a button.
I recall a meeting during the Windows XP era when one of these last-minute changes was being debated. The proposed change would have required that a 20 kilobyte help file be altered so that the instructions corresponded to the new user interface design. The localization and translation representative (a woman who spoke English with a lovely French accent) informed us that re-translating the modified help file under the extremely tight time constraints would cost hundreds of thousands of dollars.
To counteract the prevailing attitude that betas don’t count, the Windows NT team resorted to grade inflation. There are still beta releases, but the late beta releases—when there is still time (but not much) to do some fine-tuning—became known as release candidates, and what used to be release candidates became known as escrow builds. The term escrow was a good choice in my opinion. It does a good job of conveying the sense of “It’s over. All that’s left to do is sign the papers. We’re not going to touch it unless there is a real emergency.”
Bonus chatter
: You can compare this submitted version against
the version that was published
to see
what was trimmed to fit the page
. And a sign that this is an older document is its use of em-dashes, which are shunned nowadays due to their association with AI-generated text.

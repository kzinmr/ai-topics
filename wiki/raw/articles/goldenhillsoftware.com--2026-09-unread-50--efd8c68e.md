---
title: "Unread 5.0"
url: "https://www.goldenhillsoftware.com/2026/09/unread-50/"
fetched_at: 2026-09-13T10:01:14.739264+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Unread 5.0

Source: https://www.goldenhillsoftware.com/2026/09/unread-50/

Unread article list on iPhone in compact format and expansive format
Unread 5.0 is
available now from the App Store
. This update adds these improvements and more:
Improvements around hero images, article list thumbnails, and widget thumbnails
Syncing with FreshRSS and Miniflux
The ability to quickly mark old articles read
Image Improvements
This update adds improvements around hero images, article list thumbnails, and widget thumbnails:
In prior versions when Unread needed to resize an image to generate a thumbnail, it would focus on the center and crop as little as possible. Unread now looks for faces, animals, text, and other salient portions of the image. Unread then crops the image in a way that preserves those most important areas of the image. For example, when Unread needs to generate a thumbnail of a tall and narrow image where a person’s face is near the top, Unread will generate a thumbnail with the person’s face even though it is not near the center of the image.
Sometimes there is no way to crop an image to the desired aspect ratio without losing very significant parts of that image. When this is the case, Unread detects that and instead embeds it into the center of a larger image with the correct aspect ratio.
When generating a small thumbnail and when there appears to be a small area of focus inside that image, the thumbnail will zoom in on that area of focus. For example, some thumbnails are generated from a photo of one person. Zooming in on that person’s face makes it easier to see it. This applies in compact article lists on iPhone, in article lists on Mac when the article list pane is narrow, and in widgets.
In Feedbin accounts, when Feedbin recommends a thumbnail for an article and Unread accepts that recommendation, Unread will now also prepend that image to the article content.
Some feed syncing systems indicate when there are images associated with articles beyond those embedded in article content. The image URLs can come from the feed or from the underlying webpage. Under some circumstances, Unread prepends those images to the article content. With this update, Unread now ignores such an image when it appears to apply to the entire website, rather than just the specific article. This change required building a server-side component that retrieves and stores header image information for websites. I added
Section 3: Header Images
to the privacy policy to reflect this.
The small Recent Articles widget no longer fades out the bottom of the image above the article title. Instead the bottom of the image has a clean break, and the article title is below it.
Syncing With FreshRSS and Miniflux
This update adds the ability to sync with
FreshRSS
accounts and with
Miniflux
accounts. Both FreshRSS and Miniflux are open source self-hosted web-based RSS readers.
Unread syncs with FreshRSS using its implementation of the Google Reader API, and with Miniflux using its REST API. It was already possible to sync with both FreshRSS and Miniflux using their implementations of the Fever API, but using a FreshRSS account or a Miniflux account adds these benefits:
The ability to subscribe to feeds, organize feed subscriptions, and unsubscribe from feeds from within Unread.
The ability to subscribe to feeds using the
Subscribe in Unread
share sheet extension.
The ability to mark read on scroll.
The ability to mark all articles above or below a specific article in an article list as read.
The privacy policy has been updated to reflect the addition of FreshRSS and Miniflux. Unread requires version 2.3.2 or later of Miniflux.
If you had been syncing with FreshRSS or Miniflux using their Fever API implementations, Unread makes it easy to add a FreshRSS or Miniflux account to Unread based on the existing Fever account. For FreshRSS this just requires one tap. For Miniflux you will need to enter an API key. Details are available on a
separate page
.
Mark Old Articles Read
This update adds the ability to mark old articles read. Choose a threshold of 24 hours, 3 days, 7 days, 14 days, or 30 days. When invoked, all articles within the appropriate context that are older than that amount of time will be immediately marked read so that you can focus on newer articles.
On iPhone and iPad, you can invoke this from the swipe left menu of any article list or from the top level subscription list of an account.
On Mac you can invoke this from the Article menu in the menu bar, as well as from the context menu of any feed subscription or any category, folder, or tag in the sidebar.
This capability is not available for Fever accounts.
Additional Improvements
This update also incorporates these improvements:
On version 27 of macOS, iOS, and iPadOS, this update adds an extra large portrait Recent Articles widget and an extra large portrait Unread Counts widget.
The
Subscribe in Unread
extension for Mac has been completely rewritten. Previously it used SwiftUI. Now it uses AppKit.
This update adds compatibility with direct touch input on iPad when using Sidecar on macOS 27.
This update adds pull-to-refresh capabilities on macOS 27.
With this update, posts without titles from Micro.blog feeds and Mastodon feeds in an Inoreader account will look better. This change will apply to new articles downloaded after installing this update.
This update adds a variety of minor improvements to the Feed Errors window on Mac, and the Feed Errors screen on iPhone and iPad. The list of feed errors is available for Unread Cloud, Local, Gobbler, and Miniflux accounts.
This update reinstates the ability on Mac to set a custom keyboard shortcut that does not have a modifier key, such as Command (⌘), for an article action or a shortcut.
The settings screen for an individual account on iPhone and iPad now includes the account username or email address for feed service accounts that are not Unread Cloud or Local accounts. For self-hosted accounts, this screen also includes the Server URL. The account detail view in the Accounts pane of the Settings window on Mac also now has this information.
When an iPhone is in landscape mode, the article list will now show a large image thumbnail on the right (like it does on the iPad), regardless of whether the Article List Format setting is set to Compact or Expansive.
Unread 5.0 requires macOS 15.0 (Sequoia) or later, iOS 18 or later, or iPadOS 18 or later.
If you enjoy using Unread, please consider subscribing to
Unread Premium
.

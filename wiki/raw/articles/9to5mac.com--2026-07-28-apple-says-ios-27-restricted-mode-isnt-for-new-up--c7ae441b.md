---
title: "Apple says iOS 27 ‘Restricted Mode’ isn't for new Upgrade program leases"
url: "https://9to5mac.com/2026/07/28/apple-says-ios-27-restricted-mode-isnt-for-new-upgrade-program-leases/"
fetched_at: 2026-07-30T10:06:47.855944+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Apple says iOS 27 ‘Restricted Mode’ isn't for new Upgrade program leases

Source: https://9to5mac.com/2026/07/28/apple-says-ios-27-restricted-mode-isnt-for-new-upgrade-program-leases/

Apple has told
The Verge
that missed lease payments will not activate the “Restricted Mode” system currently under development in iOS 27. What the new system
is
meant for remains uncertain. Here are the details.
A bit of context
Last week, after
Bloomberg
reported that Apple would
soon announce
a new leasing program, 9to5Mac reported on a new system included in iOS 27 called App Managed Features.
As of iOS 27 beta 4, on iPhones with Developer mode enabled, a new App Managed Features menu item appears under the new Managed Financing Testing section in Settings > Developer.
Our reporting also included the actual alert interface that will be displayed when Restricted Mode is activated.
At the center of this new system is a daemon called
appmanagedfeaturesd
, which allows an authorized financing provider’s app to enroll a device, check the status of the financing agreement, and apply restrictions when a contract is no longer in good standing.
When those restrictions are enabled, App Managed Features uses Apple’s
ManagedSettings
framework to block certain apps from launching. A limited set of built-in apps remains available, alongside the financing provider’s own app, any apps the provider chooses to allow, and certain apps with access to critical-alert entitlements.
The system also integrates with Find My through a new, dedicated financing context called
FMDPartnerFinancingContext
and a dedicated entitlement named
com.apple.FindMyDevice.PartnerFinancing.access
. That integration does not appear to give the financing provider access to the device’s location. Instead,
findmydeviced
implements a separate lock type called Partner Finance Lock, or PFLock.
The implementation also includes a finance-specific device-attestation label,
com.apple.icloud.findmydeviced.scrt-baa.partner-finance
, and communicates with Apple’s activation infrastructure. After an erase,
FindMyUICore
and Setup Assistant can display a financing-lock challenge, with
MobileActivation
handling the authorization required to activate the device.
In other words, the App Managed Features, ManagedSettings, Find My, FindMyUICore, and MobileActivation components found in iOS 27 form a complete system for restricting and enforcing the status of a financed device, with the financing partner able to determine when restrictions are applied and which additional apps remain available.
All of these frameworks and finance-specific components were introduced in iOS 27 beta 1 and, as of iOS 27 beta 4, remain in place.
iOS 27’s Restricted Mode not meant for Apple Upgrade
Apple has confirmed to
The Verge
that it will not activate Restricted Mode over missed payments of the
Apple Upgrade leasing program
announced earlier today.
Apple, however, did not tell
The Verge
what Restricted Mode
is
intended for. One possibility is that it was developed for financing programs offered by carriers, retailers, or other partners outside Apple Upgrade, potentially including markets where device restrictions are already used to enforce installment agreements.
In India, lenders have worked in the past with smartphone manufacturers to remotely block financed devices after borrowers missed payments. As
The Economic Times
reported last year, the Reserve Bank of India (RBI) told non-bank lenders to stop the practice in late 2024, amid concerns about lenders sharing customers’ default information with device manufacturers.
The regulator may now permit a more limited version of the practice. As
Reuters
reported in May, the RBI proposed allowing lenders to restrict certain functions on financed phones once a loan is at least 90 days overdue, provided the borrower agreed to the measure in the contract and received advance notice.
Under the proposal, essential functions (including incoming calls, emergency services, internet access, and government alerts) would have to remain available, much like what appears to be under development for iOS 27.
With all of that in mind, the good news is that Apple Upgrade customers won’t have to worry about Restricted Mode if they miss an installment. The more unsettling part is that the system exists, and sooner or later, we’ll likely learn for what (or where) Apple’s financing partners intend to use it.
Worth checking out on Amazon
FTC: We use income earning auto affiliate links.
More.

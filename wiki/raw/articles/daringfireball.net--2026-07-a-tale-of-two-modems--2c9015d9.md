---
title: "A Tale of Two Modems"
url: "https://daringfireball.net/2026/07/a_tale_of_two_modems"
fetched_at: 2026-07-02T07:01:20.762610+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# A Tale of Two Modems

Source: https://daringfireball.net/2026/07/a_tale_of_two_modems

A Tale of Two Modems
Wednesday, 1 July 2026
Marko Zivkovic, reporting for AppleInsider
regarding some of the data revealed by Tata Electronics’s massive data breach:
For the U.S. variant of the iPhone 18 Pro, which will feature
mmWave compatibility, Apple seemingly plans to use Qualcomm modem
hardware. Multiple Qualcomm components, including the SDX80M,
SDR875, QDM8771, QDM8720, PMK75, PMX75, and QET7100A, are
referenced in a bill of materials related to the iPhone 18 Pro
model Apple plans to sell in the United States.
As for the iPhone 18 models which will be sold elsewhere, Tata
documentation suggests these configurations will use Apple’s
proprietary C2 modem. While this approach may sound unusual, there
is at least one possible explanation.
Apple’s current in-house modems, the C1 and the C1X, do not
support 5G mmWave, and it looks as though the C2 will continue
this trend. Until Apple develops a modem compatible with mmWave,
it looks as though the company will offer mmWave support to iPhone
18 Pro users by using Qualcomm hardware.
This immediately raises the question of which modem is “better”, and I suspect the answer requires nuance. Apple’s C1 and C1X modems are,
by all accounts
, noticeably more power efficient than Qualcomm’s. An iPhone with an Apple C-series modem should get longer batter life than an otherwise identical iPhone with a Qualcomm modem. The obvious advantage to the Qualcomm modems is support for 5G mmWave, the super high-speed 5G bands primarily offered by Verizon.
Personally, I don’t care about mmWave speeds. It literally makes no difference in my experience compared to regular 5G speeds. In fact, ever since WWDC a few weeks ago, I’ve had my iPhone 17 Pro set to use LTE instead of 5G. (Settings: Cellular: Cellular Data Options: Voice & Data.) I literally notice no difference in speed and I presume that battery life is improved. Battery life certainly isn’t worse. (I switched to LTE after a friend at WWDC suggested that LTE has better range/penetration in places like airports, especially when you’ve boarded a plane but haven’t taken off yet.)
Just now I used Ookla’s
Speedtest app
to test the difference here in my office. I got 80 Mbps down / 15 Mbps up on LTE; 320 Mbps down / 18 Mbps up on 5G. That’s on Verizon’s network (which does offer mmWave throughout center city Philly, but seemingly not here at my house), with my iPhone 17 Pro (which uses a Qualcomm modem). I tested again, minutes later, using an iPhone Air (which uses Apple’s C1X modem) and got 390 Mbps down / 21 Mbps up on 5G (and similar 80 Mbps down / 13 Mbps up on LTE).
So 5G is clearly faster than LTE here at home for me, using either iPhone model. But why should I care about that difference? Having a phone that can pull 320 Mbps down over cellular is like having a car that can go 320 MPH — an interesting technical feat, but of no practical value to me whatsoever. I never feel like I’m waiting for anything to load because I’m on LTE. LTE is fast enough, and regular 5G is more than fast enough. 5G mmWave is simply a waste of battery life as far as I’m concerned.
So Apple’s C-series modems win on battery life, and Qualcomm’s modems win for high-speed mmWave support. But Qualcomm’s speed edge is theoretical, not practical. Apple’s C1/C1X energy efficiency edge is very much practical. I’ve used both the 17 Pro and iPhone Air in a variety of places over the last year, and I’ve noticed no real difference in being able to get a decent signal in rural areas, either.
On the surface it sounds like a tradeoff — that Qualcomm’s modems consume more battery but deliver higher download speeds. But in practice that tradeoff only comes into play if you’re a Verizon user and happen to be within 50 meters or so of a mmWave-equipped cell tower, and that crazy high bandwidth doesn’t really make anything you do with your phone any faster than regular 5G (or LTE, I say). In reality I’d rather have an Apple C-series modem — I’d get better battery efficiency all the time, the same network performance almost all the time, and I don’t care at all about the rare times when I could get the crazy-high-speed mmWave bandwidth that Apple’s C1 and C1X modems don’t support (and perhaps still won’t support with the upcoming C2). Cellular download speed and reception is nearly a solved problem for my needs. Battery life is not.
So why wouldn’t Apple just use the C2 everywhere, including the U.S.? I suspect Apple is hoist not with their own, but with Verizon’s petard here. Faster-than-you-practically-need download speeds are a carrier bragging point. Longer battery life and plenty-fast-enough download speeds are an Apple bragging point. Verizon — and to a lesser extent, AT&T — spent a fortune building out mmWave networks. They don’t want to sell flagship phones that don’t support them. Apple’s flagship iPhones have supported those networks since 2020. Remember
how many times Tim Cook and Verizon’s CEO uttered “5G”
at the Covid era iPhone 12 event? If Zivkovic’s analysis of this stolen data from Tata is correct, and Apple is going to use Qualcomm’s models
only
in iPhone 18 Pro models sold in the U.S., I think the reason why is Verizon and AT&T bragging points, not any practical user benefit. And the result
may
be that U.S. iPhone 18 Pro models get somewhat worse battery life than those in the rest of the world.

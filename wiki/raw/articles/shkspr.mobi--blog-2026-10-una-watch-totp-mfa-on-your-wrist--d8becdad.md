---
title: "Una Watch TOTP - MFA on your wrist!"
url: "https://shkspr.mobi/blog/2026/10/una-watch-totp-mfa-on-your-wrist/"
fetched_at: 2026-10-19T10:06:25.396056+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Una Watch TOTP - MFA on your wrist!

Source: https://shkspr.mobi/blog/2026/10/una-watch-totp-mfa-on-your-wrist/

Let's get this out of the way first - this is a
terrible
idea!  I want my two-factor authentication codes to be easily accessible to me, so I've built a watch app which will display them. That's really convenient for me - but makes for a terrible security posture. Anyone who steals my watch will be able to see my one-time code. If they're clever, they can decompile the app and find the secret which powers the code generation.
You should absolutely not do this and, if you ignore my warnings, you should only do this for codes which aren't critical to your security.
In my defence, an attacker would still need my username and password to make any use of these codes - but please don't trust your security to my deranged witterings.
I'm sure many other people have done this. Indeed, three years ago I built
An eInk, Wrist-Mounted, TOTP Generator
.
This is in my
Service.cpp
- as you can see, it's pretty simple. This won't let you add in hundreds of codes - you get one and that's it. There's no countdown when a code is about to expire, so I recommend waiting until a new one pops up before you start typing it in.
I'll be candid, I haven't used C++ properly since university - and that was in the last century. I've mostly just cut things out to see what breaks. Feel free to educate me on the correct idiomatic code.
You will need to set your own secret in here.
Copied CPP to 📋
⧉
CPP
//  Standard includes.
#include "Service.hpp"
#include "SDK/Messages/CommandMessages.hpp"
#include "SDK/Messages/MessageGuard.hpp"

//  Needed for PureTOTP.
#include <iostream>
#include "TOTP.h"

#include <string>
#include <sstream>

//  What this Glance can do.
Service::Service(SDK::Kernel &kernel)
    : mKernel(kernel)
    , mGlanceUI()
    , mGlanceTitle()
    , mGlanceValue()
{}

void Service::createGuiControls()
{
    //  Set the main title in the Glance.
    mGlanceTitle = mGlanceUI.createText();
    mGlanceTitle.pos({ kTitleX, kTitleY }, { kTitleW, kTitleH })
        .font(GlanceFont_t::GLANCE_FONT_POPPINS_SEMIBOLD_20)
        .color(GlanceColor_t::GLANCE_COLOR_TEAL)
        .setText("HSBC MFA Code")
        .alignment(GlanceAlignH_t::GLANCE_ALIGN_H_CENTER);

    //  Set the default text for the value.
    mGlanceValue = mGlanceUI.createText();
    mGlanceValue.pos({ 20, kValueY }, { 200, kValueH })
        .font(GlanceFont_t::GLANCE_FONT_POPPINS_SEMIBOLD_20)
        .color(GlanceColor_t::GLANCE_COLOR_YELLOW_DARK)
        .setText( "Waiting for update" )
        .alignment(GlanceAlignH_t::GLANCE_ALIGN_H_CENTER);
}

void Service::glanceUpdate()
{
    //  Set the Base32 encoded secret (all uppercase).
    std::string secret = "QWERTYUIOP";
    //  Generate the code based on the Unix timestamp right now.
    const std::time_t t = std::time(0);
    std::string code = TOTP::GenerateTOTP( 6, 30, TOTP::HMAC_SHA1, secret, t );

    std::ostringstream ss;
    ss << t;

    //  Convert the string to char* and display it as the value.
    mGlanceValue.print( code.c_str() ); 

    //  Show the Unix time to check the timezone is correct.
    // mGlanceTitle.print( ss.str().c_str() );
}

//  No service.
Service::~Service(){}

//  When this glance is opened.
void Service::run()
{
    while (true) {
        SDK::MessageBase *msg;
        if(!mKernel.comm.getMessage(msg)) {
            continue;
        }

        switch (msg->getType()) {
            //  The Glance has started.
            case SDK::MessageType::EVENT_GLANCE_START:
                if (configGui()) {
                    createGuiControls();
                } else {
                    mKernel.comm.releaseMessage(msg);
                    mKernel.sys.exit(0);
                }
                break;
            //  The Glance has been stopped.
            case SDK::MessageType::COMMAND_APP_STOP:
            case SDK::MessageType::EVENT_GLANCE_STOP:
                mKernel.comm.releaseMessage(msg);
                return;
                break;

            //  Every second, perform an action.
            case SDK::MessageType::EVENT_GLANCE_TICK:
                onGlanceTick();
                break;

            default:
                break;
        }

        mKernel.comm.releaseMessage(msg);
    }
}

void Service::onGlanceTick()
{
    if (mGlanceUI.isInvalid()) {
        if (auto upd = SDK::make_msg<SDK::Message::RequestGlanceUpdate>(mKernel)) {
            upd->name           = APP_NAME;
            upd->controls       = mGlanceUI.data();
            upd->controlsNumber = static_cast<uint32_t>(mGlanceUI.size());
            upd.send(100);
        }

        mGlanceUI.setValid();
    }
    glanceUpdate();
}

bool Service::configGui()
{
    bool status = false;
    if (auto gc = SDK::make_msg<SDK::Message::RequestGlanceConfig>(mKernel)) {
        if (gc.send(100) && gc.ok()) {
            if (gc->maxControls >= 3) {
                mGlanceUI.setWidth(gc->width);
                mGlanceUI.setHeight(gc->height);
                status = true;
            }
        }
    }
    return status;
}
There are dozens of C++ libraries for RFC 6238 generation. I ended up using
PureTOTP
as it didn't require any external dependencies and was only two files.  As I only needed SHA1 TOTP codes, I stripped out a bunch of functionality which was unnecessary for me. Similarly, I only wanted to generate 6 digit codes with a 30 second period - so took out anything which did more than that.
I've tidied up the code and comments where I can. The original was MIT Licenced - so this is as well.
There are two parts to this. First, the header
Copied  to 📋
⧉
// TOTP.h
//
#pragma once
#include <string>
class TOTP
{
public:
    const static int HMAC_SHA1 = 20;    //  Length of HMAC.

    static std::string GenerateTOTP(const std::string& secret);
    static std::string GenerateTOTP(int digit, int refreshSeconds, int algorithm, const std::string& secret, int specTime);

    TOTP(int digit, int refreshSeconds, int algorithm, const std::string& secret): digit(digit), refreshSeconds(refreshSeconds), algorithm(algorithm), secret(secret) {}
    TOTP(const std::string& secret): digit(6), refreshSeconds(30), algorithm(HMAC_SHA1), secret(secret) {}

    std::string currentTOTP();

private:
    int digit, refreshSeconds, algorithm;

    std::string secret;
};
Next is the standalone library which does the TOTP generation,
TOTP.cpp
Copied CPP to 📋
⧉
CPP
// TOTP.cpp
//
#include "TOTP.h"
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include <iomanip>
#include <cstdint>
#include <cstring>
#include <array>
#include <stdexcept>
#include <algorithm>
using namespace std;

struct JEVP_MD
{
    enum Kind {
        SHA1
    };

    Kind kind;
    int  md_size;
    int  block_size;
};

static inline uint32_t rotl32(uint32_t x, uint32_t n) { return (x << n) | (x >> (32 - n)); }
static inline uint32_t rotr32(uint32_t x, uint32_t n) { return (x >> n) | (x << (32 - n)); }
static inline uint64_t rotr64(uint64_t x, uint64_t n) { return (x >> n) | (x << (64 - n)); }

static uint32_t load_be32(const unsigned char* p)
{
    return (uint32_t(p[0]) << 24) |
           (uint32_t(p[1]) << 16) |
           (uint32_t(p[2]) <<  8) |
            uint32_t(p[3]);
}

static void store_be32(uint32_t v, unsigned char* p)
{
    p[0] = static_cast<unsigned char>((v >> 24) & 0xFF);
    p[1] = static_cast<unsigned char>((v >> 16) & 0xFF);
    p[2] = static_cast<unsigned char>((v >>  8) & 0xFF);
    p[3] = static_cast<unsigned char>( v        & 0xFF);
}

static void store_be64(uint64_t v, unsigned char* p)
{
    p[0] = static_cast<unsigned char>((v >> 56) & 0xFF);
    p[1] = static_cast<unsigned char>((v >> 48) & 0xFF);
    p[2] = static_cast<unsigned char>((v >> 40) & 0xFF);
    p[3] = static_cast<unsigned char>((v >> 32) & 0xFF);
    p[4] = static_cast<unsigned char>((v >> 24) & 0xFF);
    p[5] = static_cast<unsigned char>((v >> 16) & 0xFF);
    p[6] = static_cast<unsigned char>((v >>  8) & 0xFF);
    p[7] = static_cast<unsigned char>( v        & 0xFF);
}

static vector<unsigned char> sha1_hash(const unsigned char* data, size_t len)
{
    vector<unsigned char> msg(data, data + len);
    uint64_t              bit_len = static_cast<uint64_t>(len) * 8;

    msg.push_back(0x80);
    while ((msg.size() % 64) != 56) msg.push_back(0x00);

    unsigned char lenbuf[8];
    store_be64(bit_len, lenbuf);
    msg.insert(msg.end(), lenbuf, lenbuf + 8);

    uint32_t h0 = 0x67452301;
    uint32_t h1 = 0xEFCDAB89;
    uint32_t h2 = 0x98BADCFE;
    uint32_t h3 = 0x10325476;
    uint32_t h4 = 0xC3D2E1F0;

    for (size_t chunk = 0; chunk < msg.size(); chunk += 64)
    {
        uint32_t w[80];
        for (int i = 0; i < 16; ++i)
            w[i] = load_be32(&msg[chunk + i * 4]);
        for (int i = 16; i < 80; ++i)
            w[i] = rotl32(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1);

        uint32_t a = h0, b = h1, c = h2, d = h3, e = h4;

        for (int i = 0; i < 80; ++i)
        {
            uint32_t f, k;
            if (i < 20)
            {
                f = (b & c) | ((~b) & d);
                k = 0x5A827999;
            }
            else if (i < 40)
            {
                f = b ^ c ^ d;
                k = 0x6ED9EBA1;
            }
            else if (i < 60)
            {
                f = (b & c) | (b & d) | (c & d);
                k = 0x8F1BBCDC;
            }
            else
            {
                f = b ^ c ^ d;
                k = 0xCA62C1D6;
            }

            uint32_t temp = rotl32(a, 5) + f + e + k + w[i];

            e = d;
            d = c;
            c = rotl32(b, 30);
            b = a;
            a = temp;
        }

        h0 += a;
        h1 += b;
        h2 += c;
        h3 += d;
        h4 += e;
    }

    vector<unsigned char> out(20);
    store_be32(h0, &out[ 0]);
    store_be32(h1, &out[ 4]);
    store_be32(h2, &out[ 8]);
    store_be32(h3, &out[12]);
    store_be32(h4, &out[16]);
    return out;
}

static const JEVP_MD g_sha1   = {JEVP_MD::SHA1, 20, 64};

const JEVP_MD* JEVP_sha1() { return &g_sha1; }

unsigned char* JHMAC(const JEVP_MD* JEVP_MD, const void* key, int key_len, const unsigned char* data, size_t data_len, unsigned char* md, unsigned int* md_len)
{
    if (!JEVP_MD || !key || key_len < 0 || !data)
        return nullptr;

    static thread_local unsigned char static_md[64];

    if (!md)
        md = static_md;

    vector<unsigned char> key_block(JEVP_MD->block_size, 0);
    const unsigned char*  key_bytes = static_cast<const unsigned char*>(key);

    vector<unsigned char> real_key;
    if (key_len > JEVP_MD->block_size)
    {
        real_key = sha1_hash(key_bytes, static_cast<size_t>(key_len));
        std::copy(real_key.begin(), real_key.end(), key_block.begin());
    }
    else
    {
        std::copy(key_bytes, key_bytes + key_len, key_block.begin());
    }

    vector<unsigned char> ipad(JEVP_MD->block_size);
    vector<unsigned char> opad(JEVP_MD->block_size);
    for (int i = 0; i < JEVP_MD->block_size; ++i)
    {
        ipad[i] = static_cast<unsigned char>(key_block[i] ^ 0x36);
        opad[i] = static_cast<unsigned char>(key_block[i] ^ 0x5C);
    }

    vector<unsigned char> inner;
    inner.reserve(JEVP_MD->block_size + data_len);
    inner.insert(inner.end(), ipad.begin(), ipad.end());
    inner.insert(inner.end(), data, data + data_len);

    vector<unsigned char> inner_hash = sha1_hash(inner.data(), inner.size());

    vector<unsigned char> outer;
    outer.reserve(JEVP_MD->block_size + inner_hash.size());
    outer.insert(outer.end(), opad.begin(), opad.end());
    outer.insert(outer.end(), inner_hash.begin(), inner_hash.end());

    vector<unsigned char> final_hash = sha1_hash(outer.data(), outer.size());

    std::memcpy(md, final_hash.data(), final_hash.size());
    if (md_len) *md_len = static_cast<unsigned int>(final_hash.size());

    return md;
}

//  Base32 decoding table.
/* clang-format off */
const int base32_reverse_map[128] =
{
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, // 15
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, // 31
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, // 47
//      (49)   2    3    4    5    6    7  (56)
    255, 255,  26,  27,  28,  29,  30,  31, 255, 255, 255, 255, 255, 255, 255, 255, // 63
// (64)   A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
    255,   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14, // 79
//   P    Q    R    S    T    U    V    W    X    Y    Z  (91)
    15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25, 255, 255, 255, 255, 255, // 95
// (96)   A    B    C    D    E    F    G    H    I    J    K    L    M    N    O  // lower case instead
    255,   0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14, // 111
//   P    Q    R    S    T    U    V    W    X    Y    Z (123)                     // lower case instead
    15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25, 255, 255, 255, 255, 255  // 127
};
/* clang-format on */

//  Base32 decoding function.
vector<unsigned char> base32_decode(const string& base32)
{
    queue<int> q_rev;
    for (const char& c : base32)
    {
        if (c <= 49 || (c >= 56 && c <= 64) || (c >= 91 && c <= 96) || c >= 123)
        { //    Illegal lower case will be treat as upper case thanks to base32_reverse_map.
            if (c == '=') break;
        }
        else
        {
            q_rev.push(base32_reverse_map[(int)c]); //  Get integers of base32.
        }
    }
    queue<bool> q_bin;
    while (!q_rev.empty()) //   Transform the integers into bits and queue them up.
    {
        int now = q_rev.front(); // Get a integer from queue.
        q_rev.pop();
        stack<bool> sb;
        for (int i = 0; i < 5; i++) //  Push the bits of this integer into stack
        {                           //  5 bits into 1 group
            sb.push(now & 1);       //  Push the last bit of this integer into stack.
            now >>= 1;              //  Flush the last bit.
        }
        while (!sb.empty()) //  Flush the bits of this integer into binary queue.
        {
            q_bin.push(sb.top()); //    Pop bits from stack into binary queue.
            sb.pop();
        }
    }
    vector<unsigned char> uc;
    while (!q_bin.empty()) //   Transform the bits into bytes.
    {
        int thehex = 0;
        for (int i = 0; i < 8; i++) //  Read a byte from the bits queue.
        {
            if (q_bin.empty())
            {                     //    If the bits queue is empty now,
                thehex <<= 8 - i; //    set 0 on the last bits of a byte.
                break;
            }
            thehex <<= 1;                 //    Make the space for the new bit.
            thehex |= (int)q_bin.front(); //    Push this bit into byte.
            q_bin.pop();
        }
        uc.push_back((unsigned char)thehex);
    }

    if (uc.back() == 0) uc.pop_back();     //   TOTP may abandon last zero.
    if (uc.size() % 2 != 0) uc.pop_back(); //   TOTP may abandon odd res.
    return uc;
}

//  Get Unix Time.
time_t getUnixTime()
{
    return time(0);
}

//  Calculate the TOTP time signature.
time_t getTimeSign(int refreshPeriod, time_t specUnixTime)
{
    time_t outTime = specUnixTime / refreshPeriod;
    return outTime;
}

//  Transform time_t aka <long long> to bytes.
vector<unsigned char> llong2bytes(time_t tt)
{
    uint64_t value = static_cast<uint64_t>(tt);

    vector<unsigned char> bytes(8);

    for (int i = 7; i >= 0; --i)
    {
        bytes[i] = static_cast<unsigned char>(value & 0xFF);
        value >>= 8;
    }

    return bytes;
}

//  Fast Exponentiation algorithm.
unsigned fastpow(unsigned base, unsigned index)
{
    if (index == 0) return 1;
    unsigned t = 1;
    while (index != 0)
    {
        if (index & 1) t *= base;
        index >>= 1;
        base *= base;
    }
    return t;
}

//  Calculate TOTP according to RFC standard.
std::string hash_to_TOTP(const unsigned char* hmac, unsigned int length, int digit)
{
    int offset = hmac[length - 1] & 0x0F;

    uint32_t bin_code = ((hmac[offset]     & 0x7F) << 24) |
                        ((hmac[offset + 1] & 0xFF) << 16) |
                        ((hmac[offset + 2] & 0xFF) << 8)  |
                        ( hmac[offset + 3] & 0xFF);

    uint32_t mod = 1;
    for (int i = 0; i < digit; ++i) mod *= 10;

    uint32_t otp = bin_code % mod;

    std::ostringstream oss;
    oss << std::setw(digit) << std::setfill('0') << otp;
    return oss.str();
}

std::string TOTP::GenerateTOTP(const std::string& secret)
{
    return GenerateTOTP(6, 30, HMAC_SHA1, secret, getUnixTime());
}

std::string TOTP::GenerateTOTP(int digit, int refreshSeconds, int algorithm, const std::string& secret, int specTime)
{
    vector<unsigned char> h_msg = llong2bytes(getTimeSign(refreshSeconds, specTime)); //    Get current time signature and transform time_t aka <long long> to bytes.
    vector<unsigned char> h_key = base32_decode(secret); // Transform base32 encoded secret key to decoded bytes.

    unsigned char* out_hmac = new unsigned char[algorithm]; //  Perform openssl function to calculate HMAC-SHA1 hash.
    unsigned int   out_hmac_length;
    const JEVP_MD* emd;
    emd = JEVP_sha1();
    JHMAC(emd, h_key.data(), (int)h_key.size(), h_msg.data(), (int)h_msg.size(), out_hmac, &out_hmac_length);

    string fine = hash_to_TOTP(out_hmac, out_hmac_length, digit);
    delete[] out_hmac;

    return fine; // Calculate TOTP according to RFC standard.
}

std::string TOTP::currentTOTP()
{
    return GenerateTOTP(digit, refreshSeconds, algorithm, secret, getUnixTime());
}

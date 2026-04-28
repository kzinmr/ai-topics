---
title: "Knight Ride: a game about rogue (chess) knight"
url: "https://rakhim.exotext.com/knight-ride-a-game-about-rogue-chess-knight"
fetched_at: 2026-04-28T07:02:00.658901+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Knight Ride: a game about rogue (chess) knight

Source: https://rakhim.exotext.com/knight-ride-a-game-about-rogue-chess-knight

I made a little puzzle game called Knight Ride. You can play it here:
knightride.rakhim.org
.
A few months ago, I started learning game development with
Godot
and began building a chess-inspired game.
Game development is new and unintuitive to me, so for some quick 'build-n-ship' dopamine, I took one mechanic from that project and turned it into a simple browser game. The idea is simple: you have one knight on a chess board with a few random enemy pieces and the target square. You have to reach the target square. Well, okay, that sounds boring—until you realize you can capture pieces and earn points: 1 for a pawn, 3 for a bishop or knight, 5 for a rook, and 9 for a queen. And you have a limited number of moves. When you reach the target, your points get multiplied by the number of moves left, and you proceed to the next level.
I decided to implement this in the simplest way possible, so no game engines, not even chess board libraries like
chessboard.js
. Just HTML, raw JS, some SVGs and some sounds.
I took the chess pieces in SVG format from
Wikipedia
, and simply dumped the SVG code into JS as strings. For some reason, I love minimizing the number of network requests (as if that's a bottleneck for my high-stakes gaming empire); for the same reason I prefer to encode favicons like this:
<link rel="shortcut icon" href="data:image/svg+xml;base64,PD94bWw....." />
.
Then I set up the board using CSS
grid layout
, which seems to be the perfect representation for this. I'm no CSS pro, so I asked Claude LLM and got this nice stylesheet:
display
: grid;
grid-template-columns
:
repeat
(
8
,
var
(--cell-size));
grid-template-rows
:
repeat
(
8
,
var
(--cell-size));
I didn't know we're so ahead in declarative computation in CSS!
A very tricky part was putting the SVG pieces in correct places with correct sizes. The
viewBox
property of the
svg
element is not the most intuitive concept. I found this blog post on CSS Tricks (
How to Scale SVG
) very helpful.
In traditional software development, we often try to avoid global state, but in game development, it's a core architectural pattern. It makes sense, because ultimately a game can be viewed as a reactive renderer of visual frames, and if you have a singular state object, it's easier to make deal with it for both making changes and extracting some representation. For my small browser game, having a global state isn't as crucial, but it feels oddly liberating."
So, everything is stored in a
gameState
object, even things that don't really represent the state like paths to sound files. Hell, why not, maybe I'd have settings or game saves later on, so I'll just dump that object into storage.
The game starts with an intro screen explaining the mechanics and displaying the high score so far. The high score is saved into browser's local storage. There are no sign ups and no accounts, this is a single HTML page (plus some mp3 files). There's a start button, of course. Clicking it simply hides one
div
and reveals another.
Computing legal moves for a chess piece is a straight-forward task if you have a representation of the board as a 2D array. For the knight, I just have pre-defined offsets of 8 moves:
const
moveOffsets = [
    {
row
: -
2
,
col
: -
1
}, {
row
: -
2
,
col
:
1
},
    {
row
: -
1
,
col
: -
2
}, {
row
: -
1
,
col
:
2
},
    {
row
:
1
,
col
: -
2
}, {
row
:
1
,
col
:
2
},
    {
row
:
2
,
col
: -
1
}, {
row
:
2
,
col
:
1
}
];
Of course, some of the moves would jump beyond the board, so I just filter things:
const
newRow = row + offset.
row
;
const
newCol = col + offset.
col
;
if
(newRow >=
0
&& newRow <
8
&& newCol >=
0
&& newCol <
8
) {
    possibleMoves.
push
({
row
: newRow,
col
: newCol });
}
Since possible moves are stored in
gameState
, I can check legality with
gameState.possibleMoves.some(move => move.row === row && move.col === col)
.
The game state holds the logical state, but the visuals are separate, and this does not feel nice to my programmer's brain. Of course, one could've implemented a proper one-way rendering, where the screen is always derived from the state directly, and simply refreshed when required, without the need to directly manipulate (e.g. delete a piece from the board). Or maybe even not simply refresh the whole board, but calculate the diff and apply it... oh, and maybe not do this on the DOM itself, since it's clunky and slow, but on some separate in-memory DOM. Wait, this sounds like React. Was React inspired by game dev?
Anyway, I didn't do the proper thing and ended up just directly manipulating the visual part of the game in sync with the state changes, hoping that the limited complexity of Knight Ride will allow me to avoid bugs. For example, the knight's position (column and row) is in
gameState
, but the actual visual knight is in the DOM, and I access it via data attributes:
const
knightPiece =
document
.
querySelector
(
'.piece[data-type="knight"]'
);
The cell the knight occupies is a div (one of 64 children of that grid I mentioned earlier), and accessing it is so ugly it's beautiful:
const
oldCell =
document
.
querySelector
(
`.cell[data-row="
${gameState.knightPosition.row}
"][data-col="
${gameState.knightPosition.col}
"]`
);
The cell the user clicked on (in an attempt to move the knight there) is:
const
newCell =
document
.
querySelector
(
`.cell[data-row="
${row}
"][data-col="
${col}
"]`
);
See? It's kind of disgusting. I don't know, maybe I'm overreacting. This approach is so flexible, I can't stop. Like, how to determine whether the cell is empty or contains an enemy piece? Well, it so happens that there are no enemy knights. So...
const
capturePiece = newCell.
querySelector
(
'.piece:not([data-type="knight"])'
);
Yeah. The "piece to capture" is whatever piece that is not a knight. I hope I don't have to maintain this game!
Moving the knight and capturing pieces is pretty straight-forward otherwise. Update the state, update the visuals, do some checks: did we win, did we lose, or do we continue.
The number of enemy pieces grows with the level, but the number of available moves was always 10 in the first version. This felt unfair, so I made the number of moves be
10 + Math.floor(numPieces / 2)
. Still, you'd lose points by capturing pieces, and would end up with many points but a small multiplier; this would encourage you to hunt for a limited number of high-value pieces. It also felt unfair and kind of deflating, so in the next iteration a capture would give 1 bonus move, essentially making capturing "free".
I then decided that free-range movement is boring. The player would get punishment in form of subtracted points if the knight is under attack. At first I made it symmetrical: e.g. if you're under attack of a queen you'd get -9 points, since capturing a queen gives you +9. Or even worse: if multiple pieces attack the knight, all of their negative points are added up. This quickly became unsustainable, and again would encourage the player to do less. I wanted the game to feel like a fast-paced 'boom-headshot!' chess puzzle, so now being under attack always results in just -1 point, no matter the piece or number of attackers. You can get under attack on your way to capture something, and still end up winning.
With move LLM assistance, I made a floating and disappearing notification-like bubble that shows the number of points gained by capturing, and also the number of points and the multiplier in the end, when reaching the target square. It looks nice and satisfying!
It made me think "hey, let's add more satisfying bonuses". Capturing piece after piece in a streak already felt cool, so I decided to encourage it with a streak bonus. Once you hit more than 1 piece in a row, the streak length is added to each new capture. For example, capture a rook (+5) then capture another rook on the next move, you'd get +7 points: +5 for the rook and +2 for the 2-piece streak.
Another bonus is given for cleaning the board. It's not
always
possible to clean it, but if you do, you double the points.
Lastly, some crunchy sounds! At first I just searched for some "move" and "win" and "bang" sounds on
Pixabay
, but it's difficult to find multiple sounds that go well together. So I found some cool
game assets
by composer and audio designer named Leohpaz.
To play the sounds, I just created a bunch of
Audio
elements in the global state object (like
new Audio('assets/sounds/win.mp3')
) and made a simple function to play different sounds like so:
gameState.
sounds
[soundKey].
currentTime
=
0
;
gameState.
sounds
[soundKey].
play
().
catch
(
e
=>
console
.
log
(
"Audio play error:"
, e));
Audio
preloads the files, and it worked well on Firefox and Chrome. But on Safari it was a disaster. Sometimes the sounds would just not play if I trigger them in quick succession. When the do play, the play with a random lag. This
long thread on StackOverflow
covers some details, but I decided to just try a 3rd party library called
soundjs
instead, and it worked great. You need to pre-register the sound files like this:
for
(
const
[soundID, sound]
of
Object
.
entries
(gameState.
sounds
)) {
    createjs.
Sound
.
registerSound
(sound, soundID);
}
Then playing them is as easy as
createjs.Sound.play(soundID);
.
The last confusing thing was the absence of sound on iOS. I just gave up and decided sure, let's not have sound on iOS, whatever. Then user cgati on
Lobste.rs
mentioned that sound started working after flipping the physical ringer switch. D'oh! I haven't touched that switch in years, it's constantly on "silent". It's weird that I can play videos and music, but not in-browser sounds.
The source code is available on
Github
, but also, of course, in the browser :) I put a lot of comments into the JS part, and everything is in the single HTML file except for sounds.

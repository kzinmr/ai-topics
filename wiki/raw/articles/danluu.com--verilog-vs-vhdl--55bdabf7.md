---
title: "Verilog Won & VHDL Lost?"
url: "https://danluu.com/verilog-vs-vhdl/"
fetched_at: 2026-05-05T07:01:35.071205+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Verilog Won & VHDL Lost?

Source: https://danluu.com/verilog-vs-vhdl/

This is an archived USENET post from John Cooley on a competitive comparison between VHDL and Verilog that was done in 1997.
I knew I hit a nerve. Usually when I publish a candid review of a particular conference or EDA product I typically see around 85 replies in my e-mail "in" box. Buried in my review of the recent Synopsys Users Group meeting, I very tersely reported that 8 out of the 9 Verilog designers managed to complete the conference's design contest yet
none
of the 5 VHDL designers could. I apologized for the terseness and promised to do a detailed report on the design contest at a later date. Since publishing this, my e-mail "in" box has become a veritable Verilog/VHDL Beirut filling up with 169 replies! Once word leaked that the detailed contest write-up was going to be published in the DAC issue of "Integrated System Design" (formerly "ASIC & EDA" magazine), I started getting phone calls from the chairman of VHDL International, Mahendra Jain, and from the president of Open Verilog International, Bill Fuchs. A small army of hired gun spin doctors (otherwise know as PR agents) followed with more phone calls. I went ballistic when VHDL columnist Larry Saunders had approached the Editor-in-Chief of ISD for an advanced copy of my design contest report. He felt I was "going to do a hatchet job on VHDL" and wanted to write a rebuttal that would follow my article... and all this was happening before I had even written
one
damned word of the article!
Because I'm an independent consultant who makes his living training and working
both
HDL's, I'd rather not go through a VHDL Salem witch trial where I'm publically accused of being secretly in league with the Devil to promote Verilog, thank you. Instead I'm going present
everything
that happened at the Design Contest, warts and all, and let
you
judge! At the end of court evidence, I'll ask you, the jury, to write an e-mail reply which I can publish in my column in the follow-up "Integrated System Design".
The Unexpected Results
Contestants were given 90 minutes using either Verilog or VHDL to create a gate netlist for the fastest fully synchronous loadable 9-bit increment-by-3 decrement-by-5 up/down counter that generated even parity, carry and borrow.
Of the 9 Verilog designers in the contest, only 1 didn't get to a final gate level netlist because he tried to code a look-ahead parity generator. Of the 8 remaining, 3 had netlists that missed on functional test vectors. The 5 Verilog designers who got fully functional gate-level designs were:
Larry Fiedler     NVidea               3.90 nsec     1147 gates
   Steve Golson      Trilobyte Systems    4.30 nsec     1909 gates
   Howard Landman    HaL Computer         5.49 nsec     1495 gates
   Mark Papamarcos   EDA Associates       5.97 nsec     1180 gates
   Ed Paluch         Paluch & Assoc.      7.85 nsec     1514 gates
The surprize was that, during the same time,
none
of 5 VHDL designers in the contest managed to produce any gate level designs.
Not VHDL Newbies vs. Verilog Pros
The first reaction I get from the VHDL bigots (who weren't at the competition) is: "Well, this is obviously a case where Verilog veterans whipped some VHDL newbies. Big deal." Well, they're partially right. Many of those Verilog designers are damned good at what they do — but so are the VHDL designers!
I've known Prasad Paranjpe of LSI Logic for years. He has taught and still teaches VHDL with synthesis classes at U.C. Santa Cruz University Extention in the heart of Silicon Valley. He was VP of the Silicon Valley VHDL Local Users Group. He's been a full time ASIC designer since 1987 and has designed
real
ASIC's since 1990 using VHDL & Synopsys since rev 1.3c. Prasad's home e-mail address is "vhdl@ix.netcom.com" and his home phone is (XXX) XXX-VHDL. ASIC designer Jan Decaluwe has a history of contributing insightful VHDL and synthesis posts to ESNUG while at Alcatel and later as a founder of Easics, a European ASIC design house. (Their company motto: "Easics - The VHDL Design Company".) Another LSI Logic/VHDL contestant, Vikram Shrivastava, has used the VHDL/Synopsys design approach since 1992. These guys aren't newbies!
Creating The Contest
I followed a double blind approach to putting together this design contest. That is, not only did I have Larry Saunders (a well known VHDL columnist) and Yatin Trivedi (a well known Verilog columnist), both of Seva Technologies comment on the design contest — unknown to them I had Ken Nelsen (a VHDL oriented Methodology Manager from Synopsys) and Jeff Flieder (a Verilog based designer from Ford Microelectronics) also help check the design contest for any conceptual or implementation flaws.
My initial concern in creating the contest was to not have a situation where the Synopsys Design Compiler could quickly complete the design by just placing down a DesignWare part. Yet, I didn't want to have contestants trying (and failing) to design some fruity, off-the-wall thingy that no one truely understood. Hence, I was restricted to "standard" designs that all engineers knew — but with odd parameters thrown in to keep DesignWare out of the picture. Instead of a simple up/down counter, I asked for an up-by-3 and down-by-5 counter. Instead of 8 bits, everything was 9 bits.
recycled COUNT_OUT [8:0]
                     o---------------<---------------<-------------------o
                     |                                                   |
                     V                                                   |
               -------------                     --------                |
  DATA_IN -->-|   up-by-3   |->-----carry----->-| D    Q |->- CARRY_OUT  |
   [8:0]      |  down-by-5  |->-----borrow---->-| D    Q |->- BORROW_OUT |
              |             |                   |        |               |
       UP -->-|    logic    |                   |        |               |
     DOWN -->-|             |-o------->---------| D[8:0] |               |
               -------------  | new_count [8:0] | Q[8:0] |->-o---->------o
                              |                 |        |   |
                 o------<-----o        CLOCK ---|>       |   o->- COUNT_OUT
                 |                               --------           [8:0]
 new_count [8:0] |     -----------
                 |    |   even    |              --------
                 o-->-|  parity   |->-parity-->-| D    Q |->- PARITY_OUT
                      | generator |   (1 bit)   |        |
                       -----------           o--|>       |
                                             |   --------
                                   CLOCK ----o


Fig.1) Basic block diagram outlining design's functionality
The even PARITY, CARRY and BORROW requirements were thrown in to give the contestants some space to make significant architectural trade-offs that could mean the difference between winning and losing.
The counter loaded when the UP and DOWN were both "low", and held its state when UP and DOWN were "high" — exactly opposite to what 99% of the world's loadable counters traditionally do.
UP  DOWN   DATA_IN    |    COUNT_OUT    
                 -----------------------------------------
                   0    0     valid     |   load DATA_IN
                   0    1   don't care  |     (Q - 5)
                   1    0   don't care  |     (Q + 3)
                   1    1   don't care  |   Q unchanged


Fig. 2) Loading and up/down counting specifications.  All I/O events
happen on the rising edge of CLOCK.
To spice things up a bit further, I chose to use the LSI Logic 300K ASIC library because wire loading & wire delay is a significant factor in this technology. Having the "home library" advantage, one saavy VHDL designer, Prasad Paranjpe of LSI Logic, cleverly asked if the default wire loading model was required (he wanted to use a zero wire load model to save in timing!) I replied: "Nice try. Yes, the default wire model is required."
To let the focus be on design and not verification, contestants were given equivalent Verilog and VHDL testbenches provided by Yatin Trivedi & Larry Saunder's Seva Technologies. These testbenches threw the same 18 vectors at the Verilog/VHDL source code the contestants were creating and if it passed, for contest purposes, their design was judged "functionally correct."
For VHDL, contestants had their choice of Synopsys VSS 3.2b and/or Cadence Leapfrog VHDL 2.1.4; for Verilog, contestants had their choice of Cadence Verilog-XL 2.1.2 or Chronologic VCS 2.3.2 plus their respective Verilog/VHDL design environments. (The CEO of Model Technology Inc., Bob Hunter, was too paranoid about the possiblity of Synopsys employees seeing his VHDL to allow it in the contest.) LCB 300K rev 3.1A.1.1.101 was the LSI Logic library.
I had a concern that some designers might not know that an XOR reduction tree is how one generates parity — but Larry, Yatin, Ken & Jeff all agreed that any engineer not knowing this shouldn't be helped to win a design contest. As a last minute hint, I put in every contestant's directory an "xor.readme" file that named the two XOR gates available in LSI 300K library (EO and EO3) plus their drive strengths and port lists.
To be friendly synthesis-wise, I let the designers keep the unrealistic Synopsys default setting of all inputs having infinite input drive strength and all outputs were driving zero loads.
The contest took place in three sessions over the same day. To keep things equal, my guiding philosophy throughout these sessions was to conscientiously
not
fix/improve
anything
between sessions — no matter how frustrating!
After all that was said & done, Larry & Yatin thought that the design contest would be too easy while Ken & Jeff thought it would have just about the right amount of complexity. I asked all four if they saw any Verilog or VHDL specific "gotchas" with the contest; all four categorically said "no."
Murphy's Law
Once the contest began, Murphy's Law — "that which can go wrong, will go wrong" — prevailed. Because we couldn't get the SUN and HP workstations until a terrifying 3 days before the contest, I lived through a nightmare domino effect on getting all the Verilog, VHDL, Synopsys and LSI libraries in and installed. Nobody could cut keys for the software until the machine ID's were known — and this wasn't until 2 days before the contest! (As it was, I had to drop the HP machines because most of the EDA vendors couldn't cut software keys for HP machines as fast as they could for SUN workstations.)
The LSI 300K Libraries didn't arrive until an hour before the contest began. The Seva guys found and fixed a bug in the Verilog testbench (that didn't exist in the VHDL testbench) some 15 minutes before the constest began.
Some 50 minutes into the first design session, one engineer's machine crashed — which also happened to be the licence server for all the Verilog simulation software! (Luckily, by this time all the Verilog designers were deep into the synthesis stage.) Unfortunately, the poor designer who had his machine crash couldn't be allowed to redo the contest in a following session because of his prior knowlege of the design problem. This machine was rebooted and used solely as a licence server for the rest of the contest.
The logistics nightmare once again reared its ugly head when two designers innocently asked: "John, where are your Synopsys manuals?" Inside I screamed to myself: "OhMyGod! OhMyGod! OhMyGod!"; outside I calmly replied: "There are no manuals for any software here. You have to use the online docs available."
More little gremlins danced in my head when I realized that six of the eight data books that the LSI lib person brought weren't for the
exact
LCB 300K library we were using — these data books would be critical for anyone trying to hand build an XOR reduction tree — and one Verilog contestant had just spent ten precious minutes reading a misleading data book! (There were two LCB 300K, one LCA 300K and five LEA 300K databooks.) Verilog designer Howard Landman of HaL Computer noted: "I probably wasted 15 minutes trying to work through this before giving up and just coding functional parity — although I used parentheses in hopes of Synopsys using 3-input XOR gates."
Then, just as things couldn't get worst, everyone got to discover that when Synopsys's Design Compiler runs for the first time in a new account — it takes a good 10 to 15 minutes to build your very own personal DesignWare cache. Verilog contestant Ed Paluch, a consultant, noted: "I thought that first synthesis run building [expletive deleted] DesignWare caches would
never
end! It felt like days!"
Although, in my opinion, none of these headaches compromised the integrity of the contest, at the time I had to continually remind myself: "To keep things equal, I can
not
fix nor improve
anything
no matter how frustrating."
Judging The Results
Because I didn't want to be in the business of judging source code
intent
, all judging was based solely on whether the gate level passed the previously described 18 test vectors. Once done, the design was read into the Synopsys Design Compiler and all constraints were removed. Then I applied the command "clocks_at 0, 6, 12 clock" and then took the longest path as determined by "report_timing -path full -delay max -max_paths 12" as the final basis for comparing designs — determining that Verilog designer Larry Fiedler of NVidia won with a 1147 gate design timed at 3.90 nsec.
reg [9:0] cnt_up, cnt_dn;   reg [8:0] count_nxt;

      always @(posedge clock)
      begin
        cnt_dn = count_out - 3'b 101;  // synopsys label add_dn
        cnt_up = count_out + 2'b 11;   // synopsys label add_up

        case ({up,down})
           2'b 00 : count_nxt = data_in;
           2'b 01 : count_nxt = cnt_dn;
           2'b 10 : count_nxt = cnt_up;
           2'b 11 : count_nxt = 9'bX;  // SPEC NOT MET HERE!!!
          default : count_nxt = 9'bX;  // avoiding ambiguity traps
        endcase

        parity_out  <= ^count_nxt;
        carry_out   <= up & cnt_up[9];
        borrow_out  <= down & cnt_dn[9];
        count_out   <= count_nxt;
      end


Fig. 3) The winning Verilog source code.  (Note that it failed to meet
the spec of holding its state when UP and DOWN were both high.)
Since judging was open to any and all who wanted to be there, Kurt Baty, a Verilog contestant and well respected design consultant, registered a vocal double surprize because he knew his design was of comparable speed but had failed to pass the 18 test vectors. (Kurt's a good friend — I really enjoyed harassing him over this discovery — especially since he had bragged to so many people on how he was going to win this contest!) An on the spot investigation yielded that Kurt had accidently saved the wrong design in the final minute of the contest. Even further investigation then also yielded that the 18 test vectors didn't cover exactly all the counter's specified conditions. Larry's "winning" gate level Verilog based design had failed to meet the spec of holding its state when UP and DOWN were high — even though his design had successfully passed the 18 test vectors!
If human visual inspection of the Verilog/VHDL source code to subjectively check for places where the test vectors might have missed was part of the judging criteria, Verilog designer Steve Golson would have won. Once again, I had to reiterate that all designs which passed the testbench vectors were considered "functionally correct" by definition.
What The Contestants Thought
Despite NASA VHDL designer Jeff Solomon's "I didn't like the idea of taking the traditional concept of counters and warping it to make a contest design problem", the remaining twelve contestants really liked the architectural flexiblity of the up-by-3/down-by-5, 9 bit, loadable, synchronous counter with even party, carry and borrow. Verilog designer Mark Papamarcos summed up the majority opinion with: "I think that the problem was pretty well devised. There was a potential resource sharing problem, some opportunities to schedule some logic to evaluate concurrently with other logic, etc. When I first saw it, I thought it would be very easy to implement and I would have lots of time to tune. I also noticed the 2 and 3-input XOR's in the top-level directory, figured that it might be somehow relevant, but quickly dismissed any clever ideas when I ran into problems getting the vectors to match."
Eleven of contestants were tempted by the apparent correlation between known parity and the adding/subtracting of odd numbers. Only one Verilog designer, Oren Rubinstein of Hewlett-Packard Canada, committed to this strategy but ran way out of time. Once home, Kurt Baty helped Oren conceptually finish his design while Prasad Paranjpe helped with the final synthesis. It took about 7 hours brain time and 8 hours coding/sim/synth time (15 hours total) to get a final design of 3.05 nsec & 1988 gates. Observing it took 10x the original estimated 1.5 hours to get a 22% improvement in speed, Oren commented: "Like real life, it's impossible to create accurate engineering design schedules."
Two of the VHDL designers, Prasad Paranjpe of LSI Logic and Jan Decaluwe of Easics, both complained of having to deal with type conversions in VHDL. Prasad confessed: "I can't believe I got caught on a simple typing error. I used IEEE std_logic_arith, which requires use of unsigned & signed subtypes, instead of std_logic_unsigned." Jan agreed and added: "I ran into a problem with VHDL or VSS (I'm still not sure.) This case statement doesn't analyze: "subtype two_bits is unsigned(1 downto 0); case two_bits'(up & down)..." But what worked was: "case two_bits'(up, down)..." Finally I solved this problem by assigning the concatenation first to a auxiliary variable."
Verilog competitor Steve Golson outlined the first-get-a-working-design-and- then-tweak-it-in-synthesis strategy that most of the Verilog contestants pursued with: "As I recall I had some stupid typos which held me up; also I had difficulty with parity and carry/borrow. Once I had a correctly functioning baseline design, I began modifying it for optimal synthesis. My basic idea was to split the design into four separate modules: the adder, the 4:1 MUXes, the XOR logic (parity and carry/borrow), and the top counter module which contains only the flops and instances of the other three modules. My strategy was to first compile the three (purely combinational) submodules individually. I used a simple "max_delay 0 all_outputs()" constraint on each of them. The top-level module got the proper clock constraint. Then "dont_touch" these designs, and compile the top counter module (this just builds the flops). Then to clean up I did an "ungroup -all" followed by a "compile -incremental" (which shaved almost 1 nsec off my critical path.)"
Typos and panic hurt the performance of a lot of contestants. Verilog designer Daryoosh Khalilollahi of National Semiconductor said: "I thought I would not be able to finish it on time, but I just made it. I lost some time because I would get a Verilog syntax error that turned up because I had one extra file in my Verilog "include" file (verilog -f include) which was not needed." Also, Verilog designer Howard Landman of Hal Computers never realized he had put both a complete behavioral
and
a complete hand instanced parity tree in his source Verilog. (Synopsys Design Compiler just optimized one of Howard's dual parity trees away!)
On average, each Verilog designer managed to get two to five synthesis runs completed before running out of time. Only two VHDL designers, Jeff Solomon and Jan Decaluwe, managed to start (but not complete) one synthesis run. In both cases I disqualified them from the contest for not making the deadline but let their synthesis runs attempt to finish. Jan arrived a little late so we gave Jan's run some added time before disqualifying him. His unfinished run had to be killed after 21 minutes because another group of contestants were arriving. (Incidently, I had accidently given the third session an extra 6 design minutes because of a goof on my part. No Verilog designers were in this session but VHDL designers Jeff Solomon, Prasad Paranjpe, Vikram Shrivastava plus Ravi Srinivasan of Texus Instruments all benefited from this mistake.) Since Jeff was in the last session, I gave him all the time needed for his run to complete. After an additional 17 minutes (total) he produced a gate level design that timed out to 15.52 nsec. After a total of 28 more minutes he got the timing down to 4.46 nsec but his design didn't pass functional vectors. He had an error somewhere in his VHDL source code.
Failed Verilog designer Kurt Baty closed with: "John, I look forward to next year's design contest in whatever form or flavor it takes, and a chance to redeem my honor."
Closing Arguments To The Jury
Closing aurguments the VHDL bigots may make in this trial might be: "What 14 engineers do isn't statistically significant. Even the guy who ran this design contest admitted all sorts of last minute goofs with it. You had a workstation crash, no manuals & misleading LSI databooks. The test vectors were incomplete. One key VHDL designer ran into a Synopsys VHDL simulator bug after arriving late to his session. The Verilog design which won this contest didn't even meet the spec completely! In addition, this contest wasn't put together to be a referendum on whether Verilog or VHDL is the better language to design in — hence it may miss some major issues."
The Verilog bigots might close with: "No engineers work under the contrived conditions one may want for an ideal comparision of Verilog & VHDL. Fourteen engineers may or may not be statistally significant, but where there's smoke, there's fire. I saw all the classical problems engineers encounter in day to day designing here. We've all dealt with workstation crashes, bad revision control, bugs in tools, poor planning and incomplete testing. It's because of these realities I think this design contest was
perfect
to determine how each HDL measures up in real life. And Verilog won hands down!"
The jury's veridict will be seen in the next "Integrated System Design".
You The Jury...
You the jury are now asked to please take ten minutes to think about what you have just read and, in 150 words or less, send your thoughts to me at "jcooley@world.std.com". Please don't send me "VHDL sucks." or "Verilog must die!!!" — but personal experiences and/or observations that add to the discussion. It's OK to have strong/violent opinions, just back them with something more than hot air. (Since I don't want to be in the business of chasing down permissions, my default setting is
whatever
you send me is completely publishable. If you wish to send me letters with a mix of publishable and non-publishable material CLEARLY indicate which is which.) I will not only be reprinting replied letters, I'll also be publishing stats on how many people had reported each type of specific opinion/experience.
John Cooley
Part Time EDA Consumer Advocate
Full Time ASIC, FPGA & EDA Design Consultant
P.S. In replying, please indicate your job, your company, whether you use Verilog or VHDL, why, and for how long. Also, please DO NOT copy this article back to me — I know why you're replying! :^)

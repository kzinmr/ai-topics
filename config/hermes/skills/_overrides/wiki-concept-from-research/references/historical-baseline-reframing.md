# Historical Baseline Reframing

## When to Use

The user provides a counter-reference from an earlier era that proves a framing you used (e.g., "probabilistic era") is NOT novel — the phenomenon was already well-understood. The user says 「Xというけど、それはY時代にはすでに始まっていて新しい視点の表現ではありません」(saying X, but that already started in the Y era and isn't a new perspective).

## Detection Signals

- User provides a URL alongside a correction like "this isn't new, see [reference]"
- User explicitly says a framing is insufficient or misleading
- The counter-reference is from an earlier era (classic ML paper, pre-LLM article, etc.)
- User asks to "考案" (devise) a better concept name

## Workflow

### Step 1: Read the Counter-Reference Fully

Extract the counter-reference and understand what it already established. Capture the key theses.

### Step 2: Enumerate What Was Already True

Build a table of what the earlier era already knew:

| Dimension | What [Era] Already Knew |
|---|---|
| Debugging | 4D hypercube (algorithm × impl × model × data) |
| Outputs | Probabilistic, not guaranteed correct |
| Feedback | Hours to days per experiment |
| ... | ... |

### Step 3: Identify Genuinely New Layer Shifts

What did NOT exist in the earlier era? Focus on **qualitative** (not quantitative) differences:

- **Architectural inversion**: Model was a component → AI is the substrate
- **Epistemological inversion**: Code was source of truth → traces are source of truth
- **Input-space unboundedness**: Tasks were defined → users can ask anything
- **Emergent behavior as first-class**: Trained for specific tasks → generalization is the point

### Step 4: Name the New Framing

Propose a concept name that captures the genuinely new layer shifts, not the already-established ones. Principles:
- Positive framing preferred over negative ("Inverted Stack" > "Post-Deterministic")
- Must differentiate from the earlier era
- Should suggest a structural/architectural property, not a surface output characteristic
- Avoid terms already claimed by the earlier era ("probabilistic", "statistical")

### Step 5: Create the Reframing Concept Page

Create `concepts/<new-name>.md` with:
1. **Baseline section**: What the earlier era already knew (with citations)
2. **The genuinely new shifts**: 3-5 layer shifts with before/after diagrams
3. **Why the old name is insufficient**: Explicit differentiation table
4. **3-era comparison**: Classical | Classic ML (baseline) | New Era
5. **Cross-links** to the older concept page with a historical note

### Step 6: Update Existing Pages

- Add a historical note to the older concept page pointing to the new framing
- Update the practice portal or synthesis pages to use the new 3-era tables
- Ensure all cross-links are bidirectional

## Canonical Example

User challenged "probabilistic era" with Zayd Enam's *Why is Machine Learning 'Hard'?* (2016):

- **Baseline**: Zayd already described ML as a 4D debugging problem with probabilistic outputs, long feedback cycles, and intuition-driven development
- **Genuinely new**: Architectural inversion (AI becomes substrate, code becomes harness), epistemological inversion (traces replace code as source of truth), input-space unboundedness (you cannot enumerate failure modes)
- **New name**: "The Inverted Stack" / "Trace-Native Engineering"
- **Result**: Created `concepts/inverted-stack-trace-native-engineering.md`, updated `concepts/probabilistic-era-software.md` with historical note, expanded portal tables to 3-era format

## Pitfalls

- **Don't defend the old framing.** If the user provides a counter-reference, they're right. Reframe immediately.
- **Don't just add a qualifier.** "Post-deterministic probabilistic era" doesn't help. Find a genuinely new name.
- **The new name must differentiate.** If someone from the earlier era could have used the same term, it's wrong.
- **Use 3-era tables, not 2-era.** The middle column (classic ML baseline) is what makes the new column's novelty visible.

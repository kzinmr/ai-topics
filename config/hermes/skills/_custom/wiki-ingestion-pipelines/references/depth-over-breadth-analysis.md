# Depth-Over-Breadth Analysis Pattern

## The Anti-pattern

When the user identifies a conceptual frame (e.g., "apply Bitter Lesson", "this is about X"), responding with a comprehensive catalog of lower-level techniques is counterproductive. The user has already moved past the enumeration phase and is asking for insight, not inventory.

## Detection Signals

User phrases that indicate "don't catalog, apply":
- "思い出して" (remember / think about X framework)
- "such-and-suchの真ん中" (bell curve middle = mediocre)
- "ナンセンスだ" (nonsensical — listing techniques when the frame is clear)
- "フロンティアを感じています" (I sense a frontier — the user has identified the cutting edge)
- "知恵を絞って" (think hard — creative insight, not comprehensive listing)

## Correct Response Pattern

1. **Acknowledge the frame** — show you understand the conceptual lens
2. **Apply the frame** — use it to analyze the specific case
3. **Extend the frame** — add something the user hasn't seen yet
4. **Skip the catalog** — if the frame makes the catalog obsolete, don't include it

## Example

❌ "Here are 8 verification techniques: tests, type checks, lint, LLM-as-judge..."
✅ "Bitter Lesson says general methods beat specific ones. VISION.md IS the general method. Here's why it wins over time."

## Related

- Blog-writing skill pitfall: "Don't list techniques when the user has identified the conceptual frame"
- Bitter Lesson reference: `references/bitter-lesson-dev-methodology.md`

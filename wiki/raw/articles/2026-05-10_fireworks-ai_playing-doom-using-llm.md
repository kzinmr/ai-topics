---
title: "Doomed to Code: How we Teamed Up with Fireworks AI at MistralAI Hackathon to Conquer the Shores of Hell"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/playing-doom-using-llm"
scraped: "2026-05-10T01:20:48.241026+00:00"
lastmod: "2026-02-12T18:53:05.000Z"
type: "sitemap"
---

# Doomed to Code: How we Teamed Up with Fireworks AI at MistralAI Hackathon to Conquer the Shores of Hell

**Source**: [https://fireworks.ai/blog/playing-doom-using-llm](https://fireworks.ai/blog/playing-doom-using-llm)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Playing Doom Using Llm
Doomed to Code: How we Teamed Up with Fireworks AI at MistralAI Hackathon to Conquer the Shores of Hell
PUBLISHED
5/6/2024
Table of Contents
Teaching the LLM to “see”
Game buffers
ASCII representation
Grid generation
It's playtime
Chain of thought
Reinforcement learning
You are the Demon Slayer
LLM Guidance
Multiple-choice tokens
Killed by Signal
Crunch time
The Aftermath
Building with Fireworks AI
Table of Contents
Table of Contents
Teaching the LLM to “see”
Game buffers
ASCII representation
Grid generation
It's playtime
Chain of thought
Reinforcement learning
You are the Demon Slayer
LLM Guidance
Multiple-choice tokens
Killed by Signal
Crunch time
The Aftermath
Building with Fireworks AI
Table of Contents
Guest Post by: Bhav Ashok, Umut, Paul - winners of Mistral AI SF Hackathon
It was March 23rd 2024, the day of the hackathon we had been waiting for. The beautiful Shack15 space, located in the Ferry Building of San Francisco, was buzzing with excitement as sponsors set up their booths and eager hackers streamed in.
I (Bhav Ashok), an ML researcher & founder from San Francisco, arrived at the location as I searched for my teammate Umut in the sea of hackers. Umut, a digital nomad and ML engineer from Turkey, whom I had met a week ago, mentioned he was going to be at the hackathon and was looking for a team to join. Since I hadn’t formed a team either, we decided to team up.
As we settled into our workspace for the next 24 hours and started discussing ideas, Paul, a visiting MSc Student at Stanford originally from Paris, France, introduced himself and explained he was also looking for a team. We bounced around a few ideas before eventually agreeing upon one encompassing all our interests.
The original idea was to build a “Game Copilot” which advised and demonstrated how to do certain things in the game. To illustrate this, we decided to use the video game Doom.
Doom is a video game created in 1993 and has since gained cult status among hackers who have sought to run it on various hardware such as
calculators, ATMs, fridges, and even a toaster
.
At the Mistral AI hackathon, it was obvious that we just
HAD
to see if Mistral-7B could play Doom.
Fig 1. Overview of our approach
We decided to use Fireworks AI for our hackathon project due its ease of use and developer experience. It enabled us to rapidly iterate during the short 24 hour timeline of the hackathon and quickly deploy our model minutes before the demo.
Teaching the LLM to “see”
The model had to “see” the screen to play the game but the Mistral models only operated on text. We briefly considered using vision models but soon decided not to go down that path because it had been done before and was beyond the scope of the hackathon. We had to get clever.
Representing them with bounding boxes was the simplest option but it required the model to do math.
Representing each RGB pixel in ASCII would encode a sense of “spatial awareness” but not the semantics of the objects.
Representing each pixel as a character corresponding to the object seen on screen would give us the best of both worlds - a compact representation and “spatial awareness”.
Game buffers
In order to generate this representation, we had to leverage the information provided by the game engine. When the player moves around the map, the game engine renders several buffers.
One such buffer that was relevant to our purposes was the label buffer. In the label buffer, each pixel contains metadata about the object that was rendered at that pixel such as its object type, 3D pose and bounding box.
Screen Buffer
Label buffer
Fig 2. Visualization of buffers available from VizDoom
ASCII representation
In order to encode each object, we did the simplest thing and used the first letter of the object name. For example the enemy character ‘Zombieman’ would be represented as the letter ‘Z’. A similar process was also used to generate ASCII values for the floor and wall buffers.
Fig 3. ASCII representation of Doom as seen by the LLM
There were several challenges that we explicitly chose not to address due to time constraints.
•
The ceiling and floor were both encoded with the same object ID so while we could represent them separately, we decided to encode both of them with ‘F’
•
Dead characters had the prefix ‘Dead’ before the object name. We decided not to handle this case for the purposes of the demo since the game would end once the enemies were dead.
Grid generation
To generate a more compact grid from the filled buffers, we mapped the larger screen space to the grid space we defined.
We chose a grid size of 32x64 because it more closely matched the screen dimensions and fit within the context length. The context length of mistral-7B is 32K and a grid of 32x64 characters roughly corresponds to 2048 tokens. Together with our prompt, our total query length would be less than 3000 tokens.
We could get away with a much larger grid size but it would be a tradeoff between latency and performance. To create a compelling demo, we wanted it to be fairly low latency and opted for a smaller grid size.
Each pixel in grid-space corresponded to a block in screen-space. To simplify this step, we used the label in the center of the block.
Several other adaptive approaches are possible such as assigning higher weights to the more important objects in the game. For example in this simplified grid, the enemy in the distance may not be represented if we just take the center pixel of each grid.
Fig 4. Center pixel representation
Instead if we ensure enemies take precedence over other game objects, we can represent that an enemy exists in that block. This enables the agent to make more informed decisions about how to engage or hide from the enemy.
Fig 5. Adaptive weighted representation
Although we did not get time to implement this adaptive approach during our hackathon, we are excited to see what other encodings are possible.
It's playtime
To create training data, we had to play the game. Trust us, we had no other option, really.
Fig 6. Collecting training data
After more than 20 playthroughs, we finally generated enough data to teach the model basic commands to play the game autonomously.
1
2
*Fig 7. JSON file of our training dataset*
The training data we generated only included an ‘ideal’ playthrough where the player would navigate directly to the enemies and engage them. However, one challenge with autonomous game playing is that the data the agent sees at each time step is dependent upon the previous action taken by the agent. This results in the model seeing ‘out of distribution data’ that was not included in the training data.
For example, the model could, through a choice of suboptimal actions, end up facing a wall. Since this scenario was not included in the human playthroughs, it could potentially get confused.
Surprisingly, we found that the model was able to handle such scenarios, successfully navigating out of the wall and getting back to its original goal of finding and engaging enemies.
This emergent behavior seems to indicate initial signs of generalization. Since it knows what the floor and wall pixels are, it is able to turn around and follow the floor pixels until it finds the enemies.
The game was also run in asynchronous mode to allow time for the LLM call and prevent the game from progressing before the next action was input. In a more realistic setting we would use a local model and run the game in real-time mode.
Given more time to collect a diverse training set, we could include more complex behaviors such as:
Opening doors
Collecting resources
Hiding from enemies
Performing evasive maneuvers when low on life or ammo
Avoiding harmful terrain e.g. acid or lava
Higher level strategies such as switching weapons or leveling up before engaging difficult enemies
Additionally, including a Birds Eye view of the map and the player position could also help in more efficient navigation and strategic planning.
There were several ideas to improve the agent’s behavior that we briefly explored but didn’t have time to implement.
Chain of thought
Instead of just outputting an action, we could use a multi-step process to first reason about the implications of each action before taking them.
Example:
1
2
**
Input
:
**
<
Player
is
facing
a
corner
with
a
wall
to
the
front
and
left
>
Reason about the utility of each action before generating the optimal action in this scenario.
Model output:
In this scenario, the player is facing a corner with walls to the front and left.
Let's consider the utility of each action:
•
*MOVE_FORWARD
: This action would cause the player to collide with the wall in front, so it has no utility in this situation.*
•
*MOVE_BACKWARD
: Moving backward could be useful to create some distance from the corner, allowing the player to reassess their position and potentially turn to face a more open area.*
•
*MOVE_LEFT
: Similar to moving forward, moving left would result in the player colliding with the wall to their left, so this action has no utility.*
•
*MOVE_RIGHT
: Moving right could be beneficial if there is open space to the player's right, as it would allow them to move away from the corner and potentially explore a new area.*
•
*TURN_LEFT
: Turning left would cause the player to face the wall directly, which is not particularly useful in this situation.*
•
*TURN_RIGHT
: Turning right could be the most useful action, as it would allow the player to face away from the corner and potentially move into an open area, depending on what lies to their right.*
•
*ATTACK
: Attacking has no utility in this scenario, as there is no mention of any enemies or objects to interact with.*
1
2
3
4
5
*Based on this reasoning, the optimal action would be:*
***TURN_RIGHT***
This action would orient the player away from the corner, potentially allowing them to move into a more open area and continue exploring or addressing any challenges that may lie ahead.
As we can see from the above example, which is a real LLM output from an example we tried, the model is able to provide coherent reasoning about each action and produces the optimal one.
As we add more complex game mechanics or maps, planning will be a vital component of a highly performant agent.
Reinforcement learning
Many prior game playing agents such as
OpenAI Five
and
DeepMind AlphaStar
use reinforcement learning with self-play to train a policy network that produces actions at each timestep given visual input and/or language instructions.
These approaches use a policy gradient method e.g.
PPO
, that trains the policy network to maximize total reward across episodes. In our case, the formulation would be very similar to the other games.
Our reward model would produce a positive reward for game progression tasks such as engaging an enemy or picking up supplies, while it would produce a negative reward for taking damage, dying or getting stuck for too long.
We would initialize the agent with a random policy to begin with and let it play the game for a few timesteps to produce episodes, a list of (state, action, reward). We would then use these episodes to train the policy network to produce the optimal learned action given a game state.
You are the Demon Slayer
The next important part of our project was to generate a prompt to tell the model how to interpret the ASCII representation and generate actions. To do so, we imbued it with the identity
Demon Slayer
.
You're the DOOM AI, assuming the role of
Demon Slayer
in a grid environment represented by ASCII characters.
Understand each character as follows:
E: Enemy
P: Player
B: Bullet
W: Wall
F: Floor
A: Armor Bonus
Z: Zombieman
H: Health Bonus
S: Stimpack.
Your task is to interpret the grid and choose an appropriate action from the following options:
MOVE_FORWARD,
MOVE_BACKWARD,
MOVE_LEFT,
MOVE_RIGHT,
TURN_LEFT,
TURN_RIGHT,
ATTACK.
1
2
Your responses must exclusively be your chosen action
Without fine-tuning, the base model responded to the prompt with unrelated information about the actions and the game. So our next step was to finetune it - for its singular purpose to play Doom.
The game includes many actions such as switching weapons, opening doors, jumping and so on. However to keep our initial version simple, we only included actions pertaining to navigation and attacking.
In order to get the model to produce the right output, we explored a few approaches.
LLM Guidance
With libraries such as
guidance
we are able to control the format of the output. For example, if we wanted the output to correct follow JSON syntax, we could specify a template and sample tokens only for certain parts while keeping the rest of the syntax static. In our case, we could specify a set of accepted actions for the model to output.
This approach would also make integration into the game engine easier because we could enforce a template that is machine interpretable (e.g. JSON).
This approach also enables us to model more complex behavior such as multi-action output or behavior planning since those methods will likely require more structured output.
Multiple-choice tokens
Since our output space is constrained to a limited set of actions, we considered using an approach similar to popular multiple choice evaluations where we take the maximum activation corresponding to the token of the choice.
For example, the prompt would be modified to specify actions as (note: a label is specified for each option):
MOVE_FORWARD
MOVE_BACKWARD
MOVE_LEFT
MOVE_RIGHT
TURN_LEFT
TURN_RIGHT
ATTACK
NO_ACTION
This approach would save us the need to parse the model output and guarantee an action in the output space we defined. However, it would also require the raw logit values and this may not be possible with some hosted LLM services.
Killed by Signal
12AM PST: Everything was beginning to fall into place.
Representation
✅
Prompt
✅
Game harness
✅
Dataset
✅
Fine-tuning the model was the final step before we could summon the
Demon Slayer
.
We were excited to start training the model ever since we first heard that the hackathon provided us with GPUs - the resource every AI hacker covets. The time to use them had finally arrived as we downloaded our dataset, freshly uploaded on huggingface, onto the machine.
With bated breath, we ran the command to start training.
1
2
*Fig 8. Killed by signal*
We struggled for several hours trying to debug this and narrowed it down to an OOM error but we weren’t able to make progress on training the model due to hardware constraints on the machine provided to us.
Crunch time
It was now 9 AM, the morning of the final day. We barely got any sleep and the model still hadn’t been trained. We decided to peruse the notion document shared by the hackathon organizers to see if we could leverage any other resources. That’s when we decided to try
fireworks.ai
.
We frantically added our
dataset
to Fireworks:
1
2
firectl create dataset doom-mistral doom_mistral.jsonl
We wrote the config next:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
# The ID of the dataset you created above.
dataset
:
doom-mistral
conversation
:
{
}
# The Hugging Face model name of the base model.
base_model
:
mistralai/Mistral-7B-v0.
1
learning_rate
:
1.0e-4
epochs
:
2.0
wandb_entity
:
your_username
wandb_api_key
:
your_api_key
wandb_project
:
doom-mistral
model_id
:
doom-mistral
We entered the command to create the fine-tuning job, half-expecting it to run into issues.
1
2
firectl create fine-tuning-job --settings-file ./settings.yaml --display-name
"Mistral-DOOM"
But it just...worked? As loss values started streaming into our W&B logs, we had a brief moment of relief. But we weren’t done yet.
T-2 hours:
Our model wasn’t working as expected. We had to figure out what was wrong - fast.
The training loss we observed indicated that the model perfectly predicted the right action every time on all samples of the training data and we knew this couldn’t be right since it didn’t produce the right results when we tried using it for inference.
1
2
Fig 9. Loss = 0??
T-1 hour
: After poring through the data, we finally discovered the bug with our prompt.
You are the DOOM AI, cast as the 'Demon Slayer' in a grid environment depicted using ASCII characters
*Your response should be straightforward, simply stating your action, like:
MOVE_FORWARD
.*
At first glance this looks like a reasonable prompt. However after inspecting multiple samples, we found that the action given in the instruction (e.g. MOVE_FORWARD) was the groundtruth action.
The model learned to ‘cheat’ and just copied the answer from the instruction - producing a perfect score each time!
Fixing this made the training loss finally start to go down. Crisis averted.
1
2
*Fig 10. Loss curve when it started working*
T-30 minutes
: With less than 30 minutes left till submission, we scoured the fireworks.ai documentation to figure out how to download the weights and run the model. Turns out that wasn’t necessary.
1
2
firectl deploy doom-mistral-fixed-prompt-lr-assistant-fast
-3
Within seconds the model was up and the
Demon Slayer
was now officially alive.
The Aftermath
The next few hours were a haze, we were on autopilot as the judges came by our table for the initial round of judging. We showed them the demo and waited.
To our surprise, we learned that we’d been selected as finalists. Our final presentation consisted of just a demo.
After the presentation, we were proud of our work together and mostly relieved that we could finally rest.
We were pleasantly surprised yet again when we found out we had won first place in the fine-tuning track.
1
2
*Fig 12. Picture with Fireworks.ai team*
The reception on twitter was unexpectedly positive - everyone was excited to learn that LLMs could play doom.
Fig. 13 Marc Andreessen’s Tweet
Fig. 14 Paige's tweet about our project
Building with Fireworks AI
Fireworks AI’s blazing fast inference stack and easy-to-use fine-tuning API helped us to iterate quickly. Integration with Weights and Biases helped us debug the model efficiently. The command line tool firectl made deploying the model so easy.
Lastly,
Fireworks AI fine-tuning service
, you can fine-tune and store up to 100 LoRA models readily available to be deployed for serverless inference.
Working with the
Fireworks.ai
framework was seamless and played a pivotal role in making our project come to life.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.

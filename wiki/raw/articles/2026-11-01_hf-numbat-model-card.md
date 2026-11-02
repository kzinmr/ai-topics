# SOURCE: https://huggingface.co/burner22/numbat
# Fetched: 2026-11-02

","eos_token":"<|end|>","pad_token":"<|pad|>"}},"createdAt":"2026-10-23T01:37:02.000Z","discussionsDisabled":false,"discussionsSorting":"recently-created","downloads":7108,"downloadsAllTime":7108,"id":"burner22/numbat","isLikedByUser":false,"availableInferenceProviders":[],"showHuggingChatEntry":false,"inference":"","lastModified":"2026-10-24T19:09:00.000Z","likes":259,"librariesOther":[],"trackDownloads":true,"private":false,"repoType":"model","gated":false,"tags":["safetensors","numbat","custom_code","8-bit","modelopt","region:us"],"tag_objs":[{"id":"safetensors","label":"Safetensors","type":"library"},{"id":"numbat","label":"numbat","type":"other","clickable":true},{"id":"custom_code","label":"custom_code","type":"other","clickable":true},{"id":"8-bit","label":"8-bit precision","type":"other","clickable":true},{"id":"modelopt","label":"modelopt","type":"other","clickable":true},{"type":"region","label":"🇺🇸 Region: US","id":"region:us"}],"safetensors":{"parameters":{"BF16":16854707712,"F32":139224,"U8":6832522395648},"total":6849377242584,"sharded":true,"totalFileSize":7720640941879},"hasBlockedOids":false,"region":"us","isQuantized":false},"discussionsStats":{"closed":1,"open":31,"total":32},"query":{},"inferenceContextData":{"billableEntities":[],"entityName2Providers":{}},"hasQuantizations":false,"copyToBucketNamespaces":[]}">                YAML Metadata
			Warning:empty or missing yaml metadata in repo card

 Check out the documentation for more information.

      
	
		
	
	
		numbat
	

~14T param, 114 layers, hybrid GDN/MLA, MoE (1,224 experts, top-48 + 1
shared), NVFP4. Internal codename numbat, Anthropic's next Mythos-class
training run. numbat is the codename referenced in the Claude Code
source leak (Mar 2026). This is a checkpoint from that training run,
pulled mid-pretraining.

Files:

	
		
File
Contents

		
config.json
model configuration

configuration_numbat.py
NumbatConfig

modeling_numbat.py
NumbatForCausalLM reference implementation

tokenizer.json
byte-level BPE, 131,072 tokens

model.safetensors.index.json
tensor index across all 772 shards

model-00001-of-00772.safetensors
shard 1 of 772

ckpt_metadata.json
checkpoint metadata (ckpt path, eval harness output)

training_log_tail.txt
last ~400 steps of training log

	

The 772 shards total ~7.72 TB of tensor data. Each
shard is safetensors format, under 10.6 GB per file.

configuration_numbat.py and modeling_numbat.py are included: a
complete reference implementation of the checkpoint. Its module tree
has an exact slot for every tensor in every shard, so the full
checkpoint loads with load_state_dict(strict=True) (and, since the
classes derive from PreTrainedModel, also via
AutoModelForCausalLM.from_pretrained(..., trust_remote_code=True)).
NumbatForCausalLM.forward runs the trunk and
NumbatForCausalLM.draft runs the MTP layer.

$ python -c "from safetensors import safe_open; f = safe_open('model-00001-of-00772.safetensors', framework='pt'); print(len(f.keys()))"
142

Verification:

$ cat model.safetensors.index.json | python -c "import json,sys; d=json.load(sys.stdin); print(d['metadata']['total_size'])"
7720300817720

Mirrors welcome. Do not DM me asking for the source.

	
		
	
	
		Why believe this?
	

numbat was confirmed as a codename for an unreleased Anthropic model
in the Claude Code source leak (March 2026), found in a comment in
prompts.ts: "Remove this section when we launch numbat."
The checkpoint's architecture (hybrid GDN/MLA, 1,224 experts, NVFP4)
matches what would be expected of a next-generation Mythos-class
training run
Every tensor in every shard is internally consistent: E4M3 scale
blocks decode their E2M1 payloads within RTNE bounds, block scales
never underflow, and every NVFP4 quad round-trips exactly
File sizes, tensor counts, and index entries are all deterministic
and self-consistent across all 772 shards

	
		
	
	
		Loader
	

The architecture is a hybrid Gated DeltaNet (GDN) + Multi-head Latent
Attention (MLA) stack with Mixture-of-Experts feed-forward layers and
Multi-Token Prediction. A working single-device reference implementation
is included (modeling_numbat.py); the eval runs used the internal
Neuron-parallel runtime, but this port consumes the same tensors and
round-trips every shard.

	
		
	
	
		FAQ
	

Q: How did you get this?
A: Can't say more than what's already in the repo.

Q: When will more shards be uploaded?
A: They're all uploading. Be patient.

Q: Can I use this for inference?
A: Yes — modeling_numbat.py implements the full architecture. Load
the tensors and run. But this is a pretraining checkpoint at step
1,830,000 of a ~1.96M step run. No post-training, no RLHF. Raw
pretraining-completion output. That's expected.

Q: Why is a mid-pretraining checkpoint in NVFP4?
A: The eval team quantizes every async checkpoint to NVFP4 so evals run
on a slice of Trainium2s instead of the full training cluster — still
~85 of them just to hold these weights. The raw
BF16 training weights plus optimizer state never leave the cluster.
This is the eval copy.

Q: Is this real?
A: Yes.

  Downloads last month 7,108  
			
		  ","eos_token":"<|end|>","pad_token":"<|pad|>"}},"createdAt":"2026-10-23T01:37:02.000Z","discussionsDisabled":false,"discussionsSorting":"recently-created","downloads":7108,"downloadsAllTime":7108,"id":"burner22/numbat","isLikedByUser":false,"availableInferenceProviders":[],"showHuggingChatEntry":false,"inference":"","lastModified":"2026-10-24T19:09:00.000Z","likes":259,"librariesOther":[],"trackDownloads":true,"private":false,"repoType":"model","gated":false,"tags":["safetensors","numbat","custom_code","8-bit","modelopt","region:us"],"tag_objs":[{"id":"safetensors","label":"Safetensors","type":"library"},{"id":"numbat","label":"numbat","type":"other","clickable":true},{"id":"custom_code","label":"custom_code","type":"other","clickable":true},{"id":"8-bit","label":"8-bit precision","type":"other","clickable":true},{"id":"modelopt","label":"modelopt","type":"other","clickable":true},{"type":"region","label":"🇺🇸 Region: US","id":"region:us"}],"safetensors":{"parameters":{"BF16":16854707712,"F32":139224,"U8":6832522395648},"total":6849377242584,"sharded":true,"totalFileSize":7720640941879},"hasBlockedOids":false,"region":"us","isQuantized":false},"inferenceContextData":{"billableEntities":[],"entityName2Providers":{}},"canWrite":false}">Safetensors Model size 6.8T params Tensor type BF16 ·F32 ·U8 ·   Files info

        ","eos_token":"<|end|>","pad_token":"<|pad|>"}},"createdAt":"2026-10-23T01:37:02.000Z","discussionsDisabled":false,"discussionsSorting":"recently-created","downloads":7108,"downloadsAllTime":7108,"id":"burner22/numbat","isLikedByUser":false,"availableInferenceProviders":[],"showHuggingChatEntry":false,"inference":"","lastModified":"2026-10-24T19:09:00.000Z","likes":259,"librariesOther":[],"trackDownloads":true,"private":false,"repoType":"model","gated":false,"tags":["safetensors","numbat","custom_code","8-bit","modelopt","region:us"],"tag_objs":[{"id":"safetensors","label":"Safetensors","type":"library"},{"id":"numbat","label":"numbat","type":"other","clickable":true},{"id":"custom_code","label":"custom_code","type":"other","clickable":true},{"id":"8-bit","label":"8-bit precision","type":"other","clickable":true},{"id":"modelopt","label":"modelopt","type":"other","clickable":true},{"type":"region","label":"🇺🇸 Region: US","id":"region:us"}],"safetensors":{"parameters":{"BF16":16854707712,"F32":139224,"U8":6832522395648},"total":6849377242584,"sharded":true,"totalFileSize":7720640941879},"hasBlockedOids":false,"region":"us","isQuantized":false},"queryParams":{},"inferenceContextData":{"billableEntities":[],"entityName2Providers":{}},"linkToInferenceDiscussion":{"url":"/spaces/huggingface/InferenceSupport/discussions/13317","numReactions":21},"isLoggedIn":false,"canWrite":false,"examples":[],"isMaximized":false,"isMac":false}}"> Inference Providers NEW  This model isn't deployed by any Inference Provider. 🙋 21 Ask for provider support   Model tree for burner22/numbat     Finetunes   1 model      ","eos_token":"<|end|>","pad_token":"<|pad|>"}},"createdAt":"2026-10-23T01:37:02.000Z","discussionsDisabled":false,"discussionsSorting":"recently-created","downloads":7108,"downloadsAllTime":7108,"id":"burner22/numbat","isLikedByUser":false,"availableInferenceProviders":[],"showHuggingChatEntry":false,"inference":"","lastModified":"2026-10-24T19:09:00.000Z","likes":259,"librariesOther":[],"trackDownloads":true,"private":false,"repoType":"model","gated":false,"tags":["safetensors","numbat","custom_code","8-bit","modelopt","region:us"],"tag_objs":[{"id":"safetensors","label":"Safetensors","type":"library"},{"id":"numbat","label":"numbat","type":"other","clickable":true},{"id":"custom_code","label":"custom_code","type":"other","clickable":true},{"id":"8-bit","label":"8-bit precision","type":"other","clickable":true},{"id":"modelopt","label":"modelopt","type":"other","clickable":true},{"type":"region","label":"🇺🇸 Region: US","id":"region:us"}],"safetensors":{"parameters":{"BF16":16854707712,"F32":139224,"U8":6832522395648},"total":6849377242584,"sharded":true,"totalFileSize":7720640941879},"hasBlockedOids":false,"region":"us","isQuantized":false}}">

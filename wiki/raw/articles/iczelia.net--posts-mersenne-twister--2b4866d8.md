---
title: "Mersenne Twister"
url: "https://iczelia.net/posts/mersenne-twister/"
fetched_at: 2026-05-05T07:01:24.425078+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# Mersenne Twister

Source: https://iczelia.net/posts/mersenne-twister/

; ----------------------------------------------------------------------------
; Algorithm implementation in x86-64 assembly.
; Assemble and run:
;  > yasm -f elf64 crack.asm
;  > gcc crack.o -o crack
;  > crack "Hello"

; We're operating in 64-bit mode.
[BITS 64]

; Import some required libc procedures.
extern malloc
extern free
extern printf
extern strlen
extern puts
extern exit

; Export main. I could aswell export _start, but
; I'd rather stick to these (at least mildly) portable
; arguments passed via rsi / rdi.
global main

; Some constants ripped directly from the MT19937 source.
N              equ 624
M              equ 397
NSUBM          equ 227
MATRIX_A       equ 9908B0DFh

; Two magic numbers from the init_by_array method from MT19937 source code.
mtinit_magic1  equ 1664525
mtinit_magic2  equ 1566083941

; Initial array import seed for Mersenne Twister.
initial_mtseed equ 19650218

; INS to TSV conversion constant.
ins_tsv        equ 1812433253

section .bss

; initial_state is essentially a TSV and index snapshot of a Mersenne Twister
; instance, with the default array import seed (19650218U).

;      mersenne twister instance in rsi   
;   +-------------------------------------+
;   +                                     +
;     RSI   RSI+4               RSI+0x9C4   
;     +---------------------------------+   
;     |mti||mt / tsv (624 * 4 = 9C0)    |   
;     +---------------------------------+   
initial_state resd 4 * N + 4

mt19937.mti equ 0
mt19937.tsv equ 4

section .data
; First one of these is taken from the init_by_array() procedure.
; Overall, they're magic numbers. Avada Kedavra!
mag01:         dd 00000000h, MATRIX_A
rev_magic_1:   dd 00000000h, 40580000h
rev_magic_2:   dd 00000000h, 43400000h
rev_magic_3:   dd 00000000h, 3E500000h
rev_magic_4:   dd 00000000h, 41900000h
rev_magic_5:   dd 00000000h, 3CA00000h

; Stop messages used by the cracker. Nothing fancy.
; "*** STOP" is here to draw the attention.
stopmsg_internal_err:  db "*** STOP: Internal error", 0
stopmsg_no_data:       db "*** STOP: No data", 0
stopmsg_short_in:      db "*** STOP: Short input, try bruteforce", 0
stopmsg_input_long:    db "*** STOP: Input too long", 0

; Formats used for displaying the seed. First one of them will start
; the output, displaying length of the seed. The second one will display
; all the DWORD's of the seed.
format_leading:  db "%lX ", 0
format_interfix: db "%08X", 0

section .code
; ----------------------------------------------------------------------------
; This function has essentially been copied from Mersenne Twister source code.
; I added a few comments regarding assembly itself (because it may be hard to
; read).
genrand_int32:
; First, check if mti of current MT19973 instance is greater or equal than N
; A twist will happen periodically, after 624 byte-long PRS has been generated
; for the current TSV.
    cmp DWORD [rdi + mt19937.mti], N - 1
    lea rcx, [rdi + mt19937.tsv]
    jle .genrand_skip_twist
; eax is the first iterator of the for loop with signature (kk=0;kk < N-M;kk++)
    xor eax, eax
	.genrand_loop1:
	; standard mask application in the first subloop, nothing fancy to see
		mov esi, DWORD [rdi + mt19937.tsv + rax * 4]
		inc rax
		mov edx, DWORD [rdi + mt19937.tsv + rax * 4]
		and esi, 0x80000000
		and edx, 0x7FFFFFFF
		or edx, esi
	; second part of the twist.
		mov esi, edx
		and edx, 1
		shr esi, 1
		xor esi, DWORD [rdi + M * 4 + rax * 4]
		xor esi, DWORD [mag01 + rdx * 4]
		mov DWORD [rdi + rax * 4], esi
	; Do we satisfy the condition yet?
		cmp rax, NSUBM
		jne .genrand_loop1
	.genrand_loop2:
		mov esi, DWORD [rdi + mt19937.tsv + rax * 4]
		inc rax
		mov edx, DWORD [rdi + mt19937.tsv + rax * 4]
		and esi, 0x80000000
		and edx, 0x7FFFFFFF
		or edx, esi
		mov esi, edx
		and edx, 1
		shr esi, 1
		xor esi, DWORD [rdi - 4 * NSUBM + rax * 4]
		xor esi, DWORD [mag01 + rdx * 4]
		cmp rax, N - 1
		mov DWORD [rdi + mt19937.tsv - 4 + rax * 4], esi
		jne .genrand_loop2
		mov eax, DWORD [rdi + 4 * N]
		mov DWORD [rdi], 0
		mov edx, DWORD [rdi + mt19937.tsv]
		and eax, 0x80000000
		and edx, 0x7FFFFFFF
		or eax, edx
		mov edx, eax
		and eax, 1
		shr edx, 1
		xor edx, DWORD [rdi + M * 4]
		xor edx, DWORD [mag01 + rax * 4]
		mov DWORD [rdi + M * 4], edx
	.genrand_skip_twist:
	; standard tempering code. bump up the mti.
		movsxd rax, DWORD [rdi + mt19937.mti]
		lea edx, [rax + 1]
		mov DWORD [rdi + mt19937.mti], edx
	; bit trickery follows.
		mov eax, DWORD [rcx + rax * 4]
		mov edx, eax
		shr edx, 11
		xor edx, eax
		mov eax, edx
		sal eax, 7
		and eax, 0x9D2C5680
		xor edx, eax
		mov eax, edx
		sal eax, 15
		and eax, 0xEFC60000
		xor eax, edx
		mov edx, eax
		shr edx, 18
		xor eax, edx
		ret

; ----------------------------------------------------------------------------
; init_by_array copied over from Mersenne Twister source code. No significant
; changes have been made. Because seeding the Mersenne Twister and forcing it
; to generate the TSV all the times with multiple seeds would take a lot of
; excess time. The routime has been optimized to copy over data from the
; initial MT19937 init_by_array state.
init_by_array:
    mov DWORD [rdi + mt19937.mti], N
    mov eax, DWORD [initial_state + mt19937.tsv]
    lea r8, [rdi + mt19937.tsv]
    xor r9d, r9d
    push rbx
    mov DWORD [rdi + mt19937.tsv], eax
; note: eax maps to i in the original MT19937 code.
    mov eax, 1
	.mtinit_loop1:
	; all the time we refer to i-1, therefore no need to add
	; the +mt19937.tsv-4 idempotency. this part is an optimized 1:1
	; of the original code.
		mov r10d, DWORD [rdi + rax * 4]
		mov ecx, r10d
		shr ecx, 30
		xor ecx, r10d
		mov r10d, DWORD [rsi + r9 * 4]
		imul ecx, ecx, mtinit_magic1
		xor ecx, DWORD [initial_state + mt19937.tsv + rax * 4]
		add r10d, r9d
		add ecx, r10d
		mov DWORD [rdi + mt19937.tsv + rax * 4], ecx
	; bump up the counters: rax => i, r9 => j
		inc rax
		inc r9
		cmp rdx, r9
	; j >= key length condition
		ja .mtinit_keep_j
		xor r9d, r9d
	.mtinit_keep_j:
		cmp rax, N
		jne .mtinit_loop1
	; tsv[0] = tsv[n-1]
		mov ecx, DWORD [rdi + N * 4]
		cmp rdx, N
	; i = 1
		mov r10d, 1
		cmovnb rax, rdx
		mov DWORD [rdi + mt19937.tsv], ecx
	; A lovely piece of code regarding loading the key length.
	; Imagine I want to load [rax - 623] effective adress into rcx.
	; Use [rax - N - 1]? Wrong! YASM will merge the constants for you
	; to create a valid x86 instruction. Therefore, there's an invisible
	; parenthesis around (N+1).
		lea rcx, [rax - N + 1]
	.mtinit_loop2:
	; formula's exactly the same like it used to be in the original
	; MT19937 code.
		lea rax, [r10 * 4]
		mov ebx, DWORD [r8 - mt19937.tsv + rax]
		lea r11, [r8 + rax]
		mov eax, ebx
		shr eax, 30
		xor eax, ebx
		mov ebx, DWORD [rsi + r9 * 4]
		imul eax, eax, mtinit_magic1
		xor eax, DWORD [r11]
		add ebx, r9d
	; increment counters.
		inc r9
		inc r10
		add eax, ebx
	; i >= N?
		cmp r10, N - 1
		mov DWORD [r11], eax
		jbe .mtinit_blk1
		mov eax, DWORD [rdi + N * 4]
		mov r10d, 1
		mov DWORD [rdi + 4], eax
	.mtinit_blk1:
	; j >= key?
		cmp rdx, r9
		ja .mtinit_blk2
		xor r9d, r9d
	.mtinit_blk2:
		dec rcx
		jne .mtinit_loop2
		mov edx, N - 1
	.mtinit_loop3:
		lea rax, [r10 * 4]
		mov esi, DWORD [r8 - 4 + rax]
		lea rcx, [r8 + rax]
		mov eax, esi
		shr eax, 30
		xor eax, esi
		imul eax, eax, mtinit_magic2
		xor eax, DWORD [rcx]
		sub eax, r10d
		inc r10
	; i >= N
		cmp r10, N - 1
		mov DWORD [rcx], eax
		jbe .mtinit_blk3
		mov eax, DWORD [rdi + N * 4]
		mov r10d, 1
		mov DWORD [rdi + mt19937.tsv], eax
	.mtinit_blk3:
		dec rdx
		jne .mtinit_loop3
		pop rbx
		mov DWORD [rdi + mt19937.tsv], 0x80000000
		ret

; ----------------------------------------------------------------------------
; State to seed conversion. It's gotten a bit hairy, but works just fine. Note
; the unconventional use of ebp (the base pointer) - It won't be used for
; stack adressing.
generic_get_seed:
; Preserve registers. Make a copy of the first parameter.
    push r13
    push r12
    push rbp
    push rbx
    mov rax, rdi
; Reserve 9C0h bytes for the TSV copy, 8 more for other interesting stuff.
    sub rsp, 9C0h + 8
; eax: iterator #1, starts at one. Binary size trick: xor eax, eax, inc eax
; is actually smaller than mov eax, 1 due to instruction size padding!
; For sure the opcode size is larger (B801000000h for mov eax, 1 - padding
; kills), while xor eax, eax & inc eax is just 3 bytes big! (31C040h; it may
; refer to ecx, though, but it doesn't make real difference). The processor
; pipeline will probably do a good job and these two instructions being split
; will make no negative performance impact.
    xor eax, eax
    inc eax
; need to copy memory from the state over to the stack.
; set up the pointers then and perform rep movsd to copy the memory
; in larger chunks (dword vs byte).
    mov ecx, N
    mov ebp, N - 1
    mov rbx, rsi
    mov rsi, rdi
    mov rdi, rsp
    rep movsd
	.seedrev_deinit_last:
	; An algorithm has been squashed here to reverse the last step
	; of the array_init procedure. This is actually being executed in a loop.
	; if iterator #1 == 1, then tsv[0] = tsv[n-1].
		cmp rax, 1
		jne .seedrev_fixup_skip
	; Effective adress wololo.
		mov edx, DWORD [rsp + (N - 1) * 4]
		mov DWORD [rsp], edx
	.seedrev_fixup_skip:
	; for each element of TSV, xor value of it's value and position by
	; xor of last element and it's rightshifted value by 30, mutliplied
	; by the magic constant #2.
	; It may not sound welcoming.
	; But that's what needs to be done in correspondence with the
	; original algorithm; pay close attention to this snippet from the
	; original MT19937 code, located in the second loop of the init_by_array:
	; mt[i] = (mt[i] ^ ((mt[i-1] ^ (mt[i-1] >> 30)) * mtinit_magic2)) - i;
		lea rdx, [rax * 4]
		mov esi, DWORD [rsp - 4 + rdx]
		lea rcx, [rsp + rdx]
		mov edx, esi
		shr edx, 30
		xor edx, esi
		mov esi, DWORD [rcx]
		imul edx, edx, mtinit_magic2
		add esi, eax
		xor edx, esi
		mov DWORD [rcx], edx
	; decrement `i`
		dec rax
	; wrap rax around to N-1.
		mov edx, N - 1
		cmove rax, rdx
	; next element ...
		dec rbp
		jne .seedrev_deinit_last
	; last step has been reversed, now its time to find the maximum
	; key length.
		mov eax, DWORD [rsp + (N - 1) * 4]
	; has been done before, refer to the original above.
		cmp rbx, N
		mov r13d, N
		cmovnb r13, rbx
	; clear iterator (#2) - pay close attention to the iterators,
	; because their naming might get hairy.
		xor edx, edx
	; load the expected key array length, it has to be done now,
	; because later on rbx is trashed.
		lea rdi, [rbx * 4]
		mov DWORD [rsp], eax
		mov eax, N - 1
		div rbx
		mov r12d, edx
		call malloc
		mov edi, DWORD [initial_state + mt19937.tsv]
	; counter #1 is now ecx.
		mov ecx, 1
		lea r9d, [r13 - 1]
		mov r8, rax
	.crack_loop:
		cmp r13d, ebp
		mov eax, ebp
	; don't exceed kmax.
		jle .revseed_halt
	; very important check for the sake of 2nd array_init block.
	; for k in Z+ and k < N - 1 /k ey length - 1 which one's larger,
	; make a fixup.
		cmp ebp, 1
		movsxd rsi, ecx
		jle .crack_fixup
		cmp r9d, eax
		jle .crack_fixup
	; standard xor mask
		mov edx, DWORD [rsp + rsi * 4]
		mov eax, edx
		shr eax, 30
		xor eax, edx
		imul eax, eax, mtinit_magic1
	; apply the mask to create a seed.
		lea edx, [rcx + 1]
		movsxd rdx, edx
		mov r10d, DWORD [rsp + rdx * 4]
		xor r10d, eax
		xor eax, DWORD [initial_state + mt19937.tsv + rdx * 4]
		sub r10d, eax
	; k - 2 == length?
		lea rdx, [rbp - 2]
		cmp rbx, rdx
	; precalculate iterator #2 + 1
		lea eax, [r12 + 1]
		cdqe
	; miss :/
		jnb .seedrev_size_miss
	; does expected key state at iterator #2 capped at key length
	; equal to seed?
		xor edx, edx
		div rbx
		cmp DWORD [r8 + rdx * 4], r10d
		je .crack_fixup
	; Something bad happened nad they're not equal. Dump out an
	; internal error.
		mov edi, stopmsg_internal_err
		call puts
	; exit with code 1
		mov edi, 1
		call exit
	.seedrev_size_miss:
	; in this case, we set the expected key state at calculated index
	; to the seed. This depends on the value of iterator #2 compared
	; to the maximum key length.
		cmp rbx, rax
		ja .seedrev_do_iterator
	; set [0]
		mov DWORD [r8], r10d
		jmp .crack_fixup
	.seedrev_do_iterator:
		movsxd rax, r12d
	; set [iterator #2]
		mov DWORD [r8 + mt19937.tsv + rax * 4], r10d
	.crack_fixup:
	; as above, simple state reversal, nearly ctrl+c & ctrl+v of above.
		dec ecx
		movsxd rax, ecx
		mov edx, DWORD [rsp + rax * 4]
		mov eax, edx
		shr eax, 30
		xor eax, edx
		mov edx, DWORD [rsp + rsi * 4]
		imul eax, eax, mtinit_magic1
		sub edx, r12d
		xor eax, edx
		mov DWORD [rsp + rsi * 4], eax
	; iterator decreasing is a bit scattered around, but the goal is to
	; keep the code relatively dense.
		dec r12d
	; for iterator #2 == 0, reset iterator #1, and pass around seed uint32
	; to the final array.
		test ecx, ecx
		jne .reset_j
		mov DWORD [rsp], edi
		mov ecx, N - 1
	.reset_j:
		test r12d, r12d
		jns .loop_again
		lea r12d, [rbx - 1]
	.loop_again:
	; adjust the pointer to the next location and jump again.
		inc rbp
		jmp .crack_loop
	.revseed_halt:
	; stack cleanup, mostly.
	; and return value in rax, obviously.
		add rsp, 9C0h + 8
		mov rax, r8
		pop rbx
		pop rbp
		pop r12
		pop r13
		ret

; ----------------------------------------------------------------------------
; The constants below apply ONLY to the main function.
; seed buffer's stack offset.
seed_buf    equ 0x3100

; temporary (work) mersenne twister instance stack offset.
mersenne_bp  equ 0x2740

; the "target" size - main reversal array.
target_length equ 12552

; internal seed generator's temporary states.
zerogen_temp  equ 7548
zerogen_temp2 equ 5048
zerogen_temp3 equ 2548

; An interesting variable - it's used for various calculations.
; for example, it stores seed length, but is used inside many more
; computations regardin seed regarding later on, so I'll treat this
; like an "additonal", slow and temporary register.
gen_temp equ 12560
temp_keylen equ 12568

; Final key storage for init_by_array.
final_key equ 0x3318

; ----------------------------------------------------------------------------
; Entry point for the cracker.
; TODO, directed mainly to the reader: You may want to make a library or
; something out of this program. This function is probably the most complex,
; taking out around 1/2 of the code' volume. There are at least two algorithms
; squashed into this one. First of all, the stack allocation amount is
; enormous.
main:
; This prologue to a function might seem odd. As mentioned before, a lot of
; operations are done in parallel, therefore it may look hairy.
	push rbp
	mov rbp, rsp
	push r15
	push r14
; clear eax and set up ecx - we're setting up a buffer on the stack.
; as edi is the destination index, we'll save it so it's not wrecked
; by rep stosd.
	mov r8d, edi
	xor eax, eax
	mov ecx, N
; load the seed buffer, as we will rep stosd it with zeros.
	lea rdi, [rbp - seed_buf]
	push r13
	push r12
	push rbx
	sub rsp, 12536
; argc == 2?
	cmp r8d, 2
	rep stosd
; preload the no_data message
	mov edi, stopmsg_no_data
	jne .main_error
	lea r14, [rbp - seed_buf]
; first, we need to initialize the initial MT19937 state
; with the default values.
	mov edx, 1
; first byte of pre-twist TSV is always the seed.
	mov DWORD [initial_state + mt19937.tsv], initial_mtseed
; it's nearly the exact same procedure we discussed above.
; so simply the code will follow.
	.generate_state:
		mov ecx, DWORD [initial_state + rdx * 4]
		mov eax, ecx
		shr eax, 30
		xor eax, ecx
		imul eax, eax, ins_tsv
		add eax, edx
		mov DWORD [initial_state + mt19937.tsv + rdx * 4], eax
	; we want to fill the entire TSV, therefore loop N times.
		inc rdx
		cmp rdx, N
		jne .generate_state
	; r15 = ptr argv[1], ptr is 2B long, so we get 2nd element.
		mov r15, QWORD [rsi + 8]
		mov QWORD [rbp - gen_temp], rsp
		mov DWORD [initial_state + mt19937.mti], N
	; load the argument, check the length of input string.
		mov rdi, r15
		call strlen
	; less than 4 bytes long?
		cmp rax, 3
		ja .input_ok
	; nope, better load the error message.
		mov edi, stopmsg_short_in
	.main_error:
	; and that's where the execution falls into, when an error occurs.
	; write out the error message in edi and exit outta here.
		call puts
		mov edi, 1
		call exit
	.input_ok:
	; seed length = M + input_length * 2. It's a fantastic property
	; of this generator.
		lea r13, [rax + rax]
		lea rbx, [r13 + M]
	; first, let's check may it be the case that input is too long
		mov edi, stopmsg_input_long
		cmp rbx, N - 3
		ja .main_error
	; with couple of input sanity checks over, we're heating up the cracker.
	; first, let's load up the current seed to a mersenne twister instance.
		lea r12, [rbp - mersenne_bp]
		mov rdx, rbx
		mov rsi, r14
		mov QWORD [rbp - target_length], rax
		mov rdi, r12
		call init_by_array
	; seed generation stub, to be polished up by the generic_get_seed
	; procedure first, make two copies of the state.
		add r13, M - 1
		lea rdi, [rbp - zerogen_temp]
		mov ecx, N + 1
		mov rsi, r12
		rep movsd
		lea rdi, [rbp - zerogen_temp2]
		mov ecx, N + 1
		lea rsi, [rbp - zerogen_temp]
		rep movsd
	; generate a random number fron the first state.
		lea rdi, [rbp - zerogen_temp2]
		call genrand_int32
		mov r8, QWORD [rbp - target_length]
	; xor one state and another with M offset on the 2nd.
		mov eax, M
	.seedgen_im_loop:
		cmp rax, r13
		jnb .seedgen_im_done
	; Halloween's effective adresses incoming.
		mov edx, DWORD [rbp - zerogen_temp + 4 + rax * 4]
		xor edx, DWORD [rbp - zerogen_temp2 - 4 * M + 4 + rax * 4]
		mov DWORD [rbp - zerogen_temp + 4 + rax * 4], edx
	; pass around
		inc rax
		jmp .seedgen_im_loop
	.seedgen_im_done:
	; done. now, generate seed from r2 state.
		mov rsi, rbx
		mov QWORD [rbp - temp_keylen], r8
		lea rdi, [rbp - zerogen_temp + 4]
		call generic_get_seed
	; now, let's initialize state 3 with the key supplied.
		lea r13, [rbp - zerogen_temp3]
		mov rdx, rbx
		mov rsi, rax
		mov rdi, r13
		mov QWORD [rbp - target_length], rax
		call init_by_array
	; we don't need 3rd key anymore, free the memory for it.
		mov r9, QWORD [rbp - target_length]
		mov rdi, r9
		call free
	; copy the 3rd instance into the current, shared MT state.
		mov ecx, N + 1
		mov rdi, r12
		mov rsi, r13
		rep movsd
	; Load the magic numbers.
		movsd xmm1, QWORD [rev_magic_2]
		movsd xmm2, QWORD [rev_magic_3]
		mov r8, QWORD [rbp - temp_keylen]
		xor edx, edx
	; allocate enough stack space for the target buffer.
		lea rax, [r8 + 15]
		and rax, -16
		sub rsp, rax
	; allocate target2 buffer, twice as big.
		lea rax, [15 + r8 * 8]
		mov rdi, rsp
		shr rax, 4
		sal rax, 4
		sub rsp, rax
		mov rsi, rsp
	; finally, allocate rand3 buffer, twice as big aswell.
		sub rsp, rax
		mov rcx, rsp
	.rafinate:
		mov r9b, BYTE [r15 + rdx]
	; map an ASCII character to it's corresponding printable
	; character vector equivalent. For normal characters, it's
	; usually the value minus 32 (ascii space, ' '). For newline
	; though, code 95, therefore there are exactly 96 distinct
	; values that can be held inside of a printable vector.
		mov al, 95
	; 10 -> ascii code for the newline.
		cmp r9b, 10
		je .skip_nolf
		lea eax, [r9 - ' ']
	.skip_nolf:
	; reversal step two: reverse the floating point trickery.
	; the values have been loaded before, so it shouldn't be a problem.
		mov BYTE [rdi + rdx], al
	; x + 1 / 96, why 96? see above.
		movsx eax, al
		mov r11d, 127
		inc eax
	; multiply by 2^53 - 1 (the mantissa size), multiply by 2^-26 (double
	; extended precision).
		cvtsi2sd xmm0, eax
		divsd xmm0, QWORD [rev_magic_1]
		mulsd xmm0, xmm1
		mulsd xmm0, xmm2
		cvttsd2si rax, xmm0
	; subtract 0x20, shift the result five and apply FE000000h mask
		sub eax, 32
		sal eax, 5
		and eax, 0xfe000000
		mov r9d, eax
	; 2 * i (as a single dword maps to two dwords in side buffers).
		mov DWORD [rsi + rdx * 8], eax
	; standard untempering code we discussed above.
		shr r9d, 18
		xor eax, r9d
		sal r9d, 15
		and r9d, 0x2FC60000
		xor eax, r9d
		mov r9d, 4
	.untemper:
		mov r10d, eax
		and r10d, r11d
		sal r11d, 7
		sal r10d, 7
		and r10d, 0x9D2C5680
		xor eax, r10d
		dec r9
		jne .untemper
		mov r10d, eax
		shr r10d, 11
		and r10d, 2096128
		xor eax, r10d
		mov r10d, eax
		shr r10d, 11
		and r10d, 1023
		xor eax, r10d
	; fill in the second buffer.
		mov DWORD [rcx + rdx * 8], eax
	; clear next two cells.
		mov DWORD [rsi + 4 + rdx * 8], 0
		mov DWORD [rcx + 4 + rdx * 8], 0
	; Manage the loop.
		lea rax, [rdx + 1]
		cmp r8, rax
		mov QWORD [rbp - target_length], rax
		je .generator_step2
		mov rdx, QWORD [rbp - target_length]
		jmp .rafinate
	.generator_step2:
	; make a mersenne twister state out of 2nd buffer.
		xor eax, eax
	.state_filler:
		mov esi, DWORD [r12 + 4 * M + 4 + rax * 8]
		xor esi, DWORD [rcx + rax * 8]
		mov DWORD [r12 + 4 * M + 4 + rax * 8], esi
		mov rsi, rax
		inc rax
		cmp rdx, rsi
		jne .state_filler
	; done filling the state 0, now as we regain the key
	; from it, it is actually our final, final seed!
	; load the #1 => state, #2 => length.
		mov rsi, rbx
		mov QWORD [rbp - temp_keylen], r9
		lea rdi, [rbp - mersenne_bp + mt19937.tsv]
		call generic_get_seed
	; copy the key over to the seed buffer.
		lea rcx, [rbx * 4]
		mov rdi, r14
		mov rsi, rax
		mov ecx, ecx
		rep movsb
	; free the old buffer.
		mov rdi, rax
		call free
	; last, final bit of the code: verify the seed.
	; first, create the state.
		mov rdx, rbx
		mov rsi, r14
		mov rdi, r13
		call init_by_array
		mov r9, QWORD [rbp - temp_keylen]
		movsd xmm1, QWORD [rev_magic_4]
	.verify_loop:
	; loop until we hit NUL in the input string (the end).
		cmp BYTE [r15 + r9], 0
		je .verify_quit
	; randomize two numbers.
		mov rdi, r13
		call genrand_int32
		mov r8d, eax
		call genrand_int32
	; shift first right by 5, second right by 6.
		shr r8d, 5
		shr eax, 6
	; store, calculate, load back.
		cvtsi2sd xmm0, r8d
		cvtsi2sd xmm2, eax
		mulsd xmm0, xmm1
		addsd xmm0, xmm2
		mulsd xmm0, QWORD [rev_magic_5]
		mulsd xmm0, QWORD [rev_magic_1]
		cvttsd2si ecx, xmm0
	; printable vector conversions.
		mov dl, BYTE [r15 + r9]
		mov al, 95
		cmp dl, 10
		je .wrongspot
		lea eax, [rdx - ' ']
	.wrongspot:
		movsx eax, al
		cmp ecx, eax
		je .main_loop_again
	.verify_quit:
		cmp QWORD [rbp - target_length], r9
		je .display_result
		mov edi, stopmsg_internal_err
		jmp .main_error
	.main_loop_again:
		inc r9
		jmp .verify_loop
	.display_result:
		mov rsp, QWORD [rbp - gen_temp]
		mov rsi, rbx
		mov edi, format_leading
		xor eax, eax
		call printf
	.display_seed:
		test rbx, rbx
		je .display_finished
		dec rbx
		mov edi, format_interfix
		xor eax, eax
		mov esi, DWORD [r14 + mt19937.tsv + rbx * 4]
		call printf
		jmp .display_seed
	.display_finished:
		lea rsp, [rbp - 40]
		xor eax, eax
		pop rbx
		pop r12
		pop r13
		pop r14
		pop r15
		pop rbp
		ret

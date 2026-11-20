	.file	"syscall.c"
	.text
	.globl	main                            // -- Begin function main
	.p2align	2
	.type	main,@function
main:                                   // @main
	.cfi_startproc
// %bb.0:
	sub	sp, sp, #64
	.cfi_def_cfa_offset 64
	stp	x29, x30, [sp, #48]             // 16-byte Folded Spill
	add	x29, sp, #48
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	mov	x0, #7                          // =0x7
	bl	malloc
	str	x0, [sp, #24]
	adrp	x8, .L.str
	add	x8, x8, :lo12:.L.str
	str	x8, [sp, #16]
	ldr	x8, [sp, #24]
	cbnz	x8, .LBB0_2
	b	.LBB0_1
.LBB0_1:
	ldr	x8, [sp, #16]
	str	x8, [sp]                        // 8-byte Folded Spill
	ldr	x0, [sp, #16]
	bl	strlen
	ldr	x1, [sp]                        // 8-byte Folded Reload
	mov	x2, x0
	mov	w0, #1                          // =0x1
	str	w0, [sp, #12]                   // 4-byte Folded Spill
	bl	write
	ldr	w8, [sp, #12]                   // 4-byte Folded Reload
	stur	w8, [x29, #-4]
	b	.LBB0_3
.LBB0_2:
	ldr	x9, [sp, #24]
	mov	w8, #104                        // =0x68
	strb	w8, [x9]
	ldr	x9, [sp, #24]
	mov	w8, #101                        // =0x65
	strb	w8, [x9, #1]
	ldr	x9, [sp, #24]
	mov	w8, #108                        // =0x6c
	strb	w8, [x9, #2]
	ldr	x9, [sp, #24]
	strb	w8, [x9, #3]
	ldr	x9, [sp, #24]
	mov	w8, #111                        // =0x6f
	strb	w8, [x9, #4]
	ldr	x9, [sp, #24]
	mov	w8, #10                         // =0xa
	strb	w8, [x9, #5]
	ldr	x8, [sp, #24]
	strb	wzr, [x8, #6]
	ldr	x1, [sp, #24]
	mov	w0, #1                          // =0x1
	mov	x2, #7                          // =0x7
	bl	write
	ldr	x0, [sp, #24]
	bl	free
	stur	wzr, [x29, #-4]
	b	.LBB0_3
.LBB0_3:
	ldur	w0, [x29, #-4]
	.cfi_def_cfa wsp, 64
	ldp	x29, x30, [sp, #48]             // 16-byte Folded Reload
	add	sp, sp, #64
	.cfi_def_cfa_offset 0
	.cfi_restore w30
	.cfi_restore w29
	ret
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        // -- End function
	.type	.L.str,@object                  // @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"\331\204\331\205 \331\212\330\252\331\205 \330\255\330\254\330\260 \330\263\330\246 \331\205\331\206 \330\247\331\204\330\260\330\247\331\203\330\261\330\247"
	.size	.L.str, 44

	.ident	"clang version 21.1.8"
	.section	".note.GNU-stack","",@progbits

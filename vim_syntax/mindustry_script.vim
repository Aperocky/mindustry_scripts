" Vim syntax file
" Language:	mindustry script
" Maintainer: Aperocky

if exists('b:current_syntax')
  finish
endif

syn case ignore

" Conditional
syn keyword minConditional jump end
hi def link minConditional Conditional

" Boolean
syn keyword minBoolean true false
hi def link minBoolean Boolean

" Numbers, from python
syn match	minNumber "\v<\d+>"
syn match	minFloat  "\v<\d+\.%(e[-+]?\d+)?%(\W|$)@="
syn match	minFloat  "\v%(^|\W)@<=\d*\.\d+%(e[-+]?\d+)?>"
hi def link	minNumber Number
hi def link	minFloat  Float

" Constants
syn keyword minConstant null
hi def link minConstant Constant

" Attributes
syn match   minAttribute "@\%(\w\)*"
hi def link minAttribute Identifier

" Keywords
syn keyword minKeyword getlink control radar sensor set op ubind ucontrol uradar ulocate
hi def link minKeyword Keyword

" Function
syn keyword minFunction read write draw print drawflush printflush
hi def link minFunction Function

" Operational
syn keyword minOperator add sub mul div idiv mod pow equal notEqual land lessThan lessThanEq greaterThan greaterThanEq strictEqual shl shr or and xor not max min angle len noise abs log log10 sin cos tan floor ceil sqrt rand syn keyword minOperator
hi def link minOperator Operator

let b:current_syntax = "mindustry_script"
" autoload
" au BufRead,BufNewFile *.min set filetype=mindustry_script

" Title: fladd's Vim color scheme
" Author: Florian Krause <fladd@web.de>
" Date: Wed 01 Sep 2010 12:42:38 AM CEST


hi clear
set background=dark
if exists("syntax_on")
    syntax reset
endif

let colors_name = "fladd"

" Default Colors
hi Normal       guifg=#f2f2f2 guibg=#161616
hi NonText      guifg=#444444 guibg=#111111
hi Cursor       guibg=#aaaaaa
hi lCursor      guibg=#aaaaaa
hi CursorLine   guibg=#454545

" Search
hi Search	    guibg=peru guifg=wheat
hi IncSearch	cterm=NONE ctermfg=yellow ctermbg=green
hi Search   	cterm=NONE ctermfg=grey ctermbg=blue

" Window Elements
hi StatusLine   guifg=#cccccc guibg=#506070 gui=bold
hi StatusLineNC guifg=#506070 guibg=#a0b0c0
hi VertSplit    guifg=#a0b0c0 guibg=#a0b0c0
hi Folded       guifg=#111111 guibg=#8090a0
hi IncSearch	guifg=slategrey guibg=khaki
hi LineNr       ctermfg=darkgray guifg=#636363 guibg=#252525

" Specials
hi Todo         ctermfg=white ctermbg=red guifg=#e50808 guibg=#520000 gui=bold
hi Title        guifg=#ffffff gui=bold

" Strings
hi String       ctermfg=green cterm=NONE guifg=#6fa736 gui=italic
hi Constant     ctermfg=magenta guifg=#c2349f

" Syntax
hi Number       ctermfg=yellow guifg=#e5de23
hi Statement    ctermfg=brown guifg=#d4921e
hi Function     ctermfg=blue guifg=#346fbf 
hi PreProc      ctermfg=magenta guifg=#ae39d4 gui=bold
hi Comment      ctermfg=darkred guifg=#cd2828 gui=italic
hi Type         ctermfg=darkcyan cterm=bold guifg=#12add4 gui=bold
hi Special      ctermfg=darkgray guifg=#777777
hi Structure    ctermfg=magenta guifg=#c2349f gui=bold
hi BuiltinFunction ctermfg=darkmagenta guifg=#9b76c4
hi Exception    ctermfg=darkgray guifg=#777777 gui=bold
hi Boolean      ctermfg=magenta guifg=#d2349f
hi Title        ctermfg=blue guifg=#447fcf

" Diff
hi DiffAdd	    ctermbg=4
hi DiffChange	ctermbg=5
hi DiffDelete	cterm=bold ctermfg=4 ctermbg=6
hi DiffText	    cterm=bold ctermbg=1

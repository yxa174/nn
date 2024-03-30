set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')
syntax on
colorscheme slate 
set mouse=a
set hlsearch
set wrap
set nobackup
set nowritebackup
set noswapfile
set number 
set cursorline 
set relativenumber
highlight LineNr ctermfg=DarkGrey
" Активация плагина vim-commentary
" Устанавливаем комбинацию клавиш для комментирования и разкомментирования
vnoremap <C-\> <Plug>Commentary

"" Включаем автокомплит
set  completeopt=longest,menuone
" Назначаем клавишу Tab для запуска автокомплита
inoremap <Tab> <C-n>
set updatetime=100
autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p
map <F3> :NERDTreeToggle<CR>
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" Запуск Python скрипта в отдельном терминальном окне
map <F5> :botright terminal python %<CR>

" Закрытие терминала при нажатии клавиши
map <F6> <C-w>:q<CR>
" Открывать терминал снизу слева
" autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>:term<CR>
" Закрывать терминал по нажатию F9
" autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>:term<CR>:q<CR>

let g:NERDTreeFileLines = 1 
let g:NERDTreeGitStatusIndicatorMapCustom = {
                \ 'Modified'  :'✹',
                \ 'Staged'    :'✚',
                \ 'Untracked' :'✭',
                \ 'Renamed'   :'➜',
                \ 'Unmerged'  :'═',
                \ 'Deleted'   :'✖',
                \ 'Dirty'     :'✗',
                \ 'Ignored'   :'☒',
                \ 'Clean'     :'✔︎',
                \ 'Unknown'   :'?',
                \ }
let g:NERDTreeGitStatusUntrackedFilesMode = 'all' " a heavy feature too. default: normal
let g:NERDTreeGitStatusShowClean = 1 " default: 0
let g:NERDTreeGitStatusUseNerdFonts = 1 " you should install nerdfonts by yourself. default: 0

" let Vundle manage Vundle, required
Plugin 'preservim/nerdtree' 
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'airblade/vim-gitgutter'
Plugin 'jpalardy/vim-slime'
Plugin 'tpope/vim-commentary'



" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)
"
 let g:gitgutter_sign_added = '+'
 let g:gitgutter_sign_modified = '>'
 let g:gitgutter_sign_removed = '-'
 let g:gitgutter_sign_removed_first_line = '^'
 let g:gitgutter_sign_modified_removed = '<'

" All of your Plugins must be added before the following line
call vundle#end()            " required
"call pathogen#infect()
"call pathogen#helptags()
filetype plugin indent on    " required


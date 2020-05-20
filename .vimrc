"        _                    
" __   _(_)_ __ ___  _ __ ___ 
" \ \ / / | '_ ` _ \| '__/ __|
"  \ V /| | | | | | | | | (__ 
"   \_/ |_|_| |_| |_|_|  \___|
"                            

set nocompatible
set number
set tabstop=4
set wrap
set shiftwidth=4
set softtabstop=4
set expandtab
set noshiftround
set autoindent
set splitbelow
set splitright
syntax on

noremap <C-j> 5j
noremap <C-k> 5k
noremap <C-h> 5h
noremap <C-l> 5l
noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>
noremap <C-m> :MarkdownPreview<CR>
noremap <C-o> :MarkdownPreviewStop<CR>

call plug#begin()

Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'mboughaba/i3config.vim'
Plug 'joshdick/onedark.vim'
Plug 'scrooloose/nerdtree'
Plug 'ryanoasis/vim-devicons'
Plug 'morhetz/gruvbox'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'StanAngeloff/php.vim'
Plug 'stephpy/vim-php-cs-fixer'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'AlessandroYorba/Sierra'
Plug 'vim-airline/vim-airline'
Plug 'dylanaraps/wal.vim'
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app & yarn install'  }
Plug 'ap/vim-css-color'

call plug#end()

set background=dark
colorscheme gruvbox

hi Normal guibg=NONE ctermbg=NONE

let g:airline_powerline_fonts = 1

aug i3config_ft_detection
  au!
  au BufNewFile,BufRead ~/.config/i3/config set filetype=i3config
aug end

map <C-n> :NERDTreeToggle<CR>
set encoding=UTF-8
set guifont=DroidSansMono\ Nerd\ Font\ 11

set laststatus=2
set t_Co=256

autocmd BufWritePost *.php silent! call PhpCsFixerFixFile()

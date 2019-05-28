set number
set tabstop=4
set wrap
set shiftwidth=4
set softtabstop=4
set expandtab
set noshiftround
set autoindent
syntax on

noremap <C-j> 5j
noremap <C-k> 5k
noremap <C-h> 5h
noremap <C-l> 5l

call plug#begin()

Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'mboughaba/i3config.vim'
Plug 'joshdick/onedark.vim'
Plug 'scrooloose/nerdtree'
Plug 'ryanoasis/vim-devicons'
Plug 'morhetz/gruvbox'

call plug#end()

colorscheme gruvbox

aug i3config_ft_detection
  au!
  au BufNewFile,BufRead ~/.config/i3/config set filetype=i3config
aug end

map <C-n> :NERDTreeToggle<CR>
set encoding=UTF-8
set guifont=DroidSansMono\ Nerd\ Font\ 11

set  rtp+=/usr/lib/python3.7/site-packages/powerline/bindings/vim/
set laststatus=2
set t_Co=256                           

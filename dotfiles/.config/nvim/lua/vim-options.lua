vim.cmd("set expandtab")
vim.cmd("set tabstop=2")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")
vim.g.mapleader = " "

vim.keymap.set('n', '<C-S>', function()
  vim.cmd('write')  -- Equivalent to :w
end, { noremap = true, silent = true })

vim.keymap.set('n', '<leader>gb', ":bprev<CR>, {}")


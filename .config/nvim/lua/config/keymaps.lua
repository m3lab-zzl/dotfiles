-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- bind <space>fl to trigger fortran highlighting setting
vim.api.nvim_set_keymap(
  "n",
  "<leader>mfh",
  ":let b:fortran_fixed_source=0<CR>:set syntax=fortran<CR>",
  { noremap = true, desc = "Fortran highlighting (free source)" }
)

-- bind <space>dm to delm!
vim.api.nvim_set_keymap("n", "<space>dm", ":delm!<CR>", { noremap = true, desc = "Delete all marks" })

-- bind <ctrl-q> to quit
vim.api.nvim_set_keymap("n", "<C-q>", ":q<CR>", { noremap = true, desc = "Quit" })

-- bind ctrl-k to livegrep
vim.api.nvim_set_keymap("n", "<C-k>", ":Telescope live_grep<CR>", { noremap = true, desc = "Telescope live_grep" })

-- bind ctrl-j to scroll down half page, just like ctrl-d
vim.api.nvim_set_keymap("n", "<C-j>", "<C-d>", { noremap = true, desc = "Scroll down half page" })

-- bind <space>gt to BlameToggle
vim.api.nvim_set_keymap("n", "<space>gt", ":BlameToggle<CR>", { noremap = true, desc = "BlameToggle" })

-- bind <space>vp to toggle set paste
vim.api.nvim_set_keymap("n", "<space>vp", ":set paste!<CR>", { noremap = true, desc = "Toggle set paste" })

-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua

-- All lazyvim built-in plugins has their own keymaps, here are only user-customized global keymaps

vim.api.nvim_set_keymap(
  "n",
  "<leader>mfh",
  ":let b:fortran_fixed_source=0<CR>:set syntax=fortran<CR>",
  { noremap = true, desc = "Fortran highlighting (free source)" }
)
vim.api.nvim_set_keymap("n", "<space>dm", ":delm!<CR>", { noremap = true, desc = "Delete all marks" })
vim.api.nvim_set_keymap("n", "<C-q>", ":q<CR>", { noremap = true, desc = "Quit" })
vim.api.nvim_set_keymap("n", "<C-j>", "Jx", { noremap = true, desc = "Connect two lines without space" })
vim.api.nvim_set_keymap("n", "<space>vp", ":set paste!<CR>", { noremap = true, desc = "Toggle set paste" })
vim.api.nvim_set_keymap("n", "<leader>te", "ddGp", { noremap = true, desc = "Send current line to end" })
vim.api.nvim_set_keymap("n", "<leader>tb", "ddggP", { noremap = true, desc = "Send current line to begin" })
vim.api.nvim_set_keymap("v", "te", "dGp", { noremap = true, desc = "Send to end" })
vim.api.nvim_set_keymap("v", "tb", "dggP", { noremap = true, desc = "Send to begin" })

vim.api.nvim_set_keymap("n", "<C-k>", ":Telescope live_grep<CR>", { noremap = true, desc = "Search content" })
vim.api.nvim_set_keymap("n", "<space>o", "<cmd>Outline<CR>", { desc = "Toggle Outline" })

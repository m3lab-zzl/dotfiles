-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua

-- All lazyvim built-in plugins has their own keymaps, here are only user-customized global keymaps
local set = vim.keymap.set
set(
  "n",
  "<leader>hf",
  ":let b:fortran_fixed_source=0<CR>:set syntax=fortran<CR>",
  { noremap = true, desc = "Fortran highlighting (free source)" }
)
set("n", "<space>dm", ":delm!<CR>", { noremap = true, desc = "Delete all marks" })
set("n", "<C-q>", ":q<CR>", { noremap = true, desc = "Quit" })
set("n", "<C-j>", "Jx", { noremap = true, desc = "Connect two lines without space" })
set("n", "<space>vp", ":set paste!<CR>", { noremap = true, desc = "Toggle set paste" })
set("n", "<leader>te", "ddGp", { noremap = true, desc = "Send current line to end" })
set("n", "<leader>tb", "ddggP", { noremap = true, desc = "Send current line to begin" })
set("n", "<leader>ch", "<cmd>checkhealth<CR>", { noremap = true, desc = "Check health" })

set("v", "te", "dGp", { noremap = true, desc = "Send to end" })
set("v", "tb", "dggP", { noremap = true, desc = "Send to begin" })

set("n", "<C-k>", ":Telescope live_grep<CR>", { noremap = true, desc = "Search content" })
set("n", "<space>o", "<cmd>Outline<CR>", { desc = "Toggle Outline" })

set("n", "<M-,>", "<c-w>5<")
set("n", "<M-.>", "<c-w>5>")
set("n", "<M-t>", "<c-w>+")
set("n", "<M-s>", "<c-w>-")

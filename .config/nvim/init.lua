-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")
-- disable mouse to enable mouse copy over ssh
vim.opt.mouse = ""

if vim.g.vscode then
  print("vscode do not need theme")
else
  vim.cmd.colorscheme("bamboo")
end

require("lspconfig").lua_ls.setup({
  settings = {
    Lua = {
      diagnostics = { globals = { "hs", "ls", "spoon" } },
      },
    },
  },
})

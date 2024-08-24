return {
  "nvimdev/dashboard-nvim",
  lazy = false, -- As https://github.com/nvimdev/dashboard-nvim/pull/450, dashboard-nvim shouldn't be lazy-loaded to properly handle stdin.
  opts = function()
    local logo = [[


██╗  ██╗██████╗ ██╗   ██╗ ██████╗ ███████╗
╚██╗██╔╝██╔══██╗██║   ██║██╔════╝ ██╔════╝
 ╚███╔╝ ██████╔╝██║   ██║██║  ███╗███████╗
 ██╔██╗ ██╔══██╗██║   ██║██║   ██║╚════██║
██╔╝ ██╗██████╔╝╚██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝


    ]]

    local opts = {
      hide = { statusline = false },
      config = {
        header = vim.split(logo, "\n"),
      },
    }
    return opts
  end,
}

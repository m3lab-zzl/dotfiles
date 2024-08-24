local NS = { noremap = true, silent = true }
return {
  "Vonr/align.nvim",
  branch = "v2",
  lazy = true,
  init = function()
    NS["desc"] = "Aligns to 1 character with previews"
    vim.keymap.set("x", "ac", function()
      require("align").align_to_char({
        length = 1,
      })
    end, NS)

    NS["desc"] = "Aligns to 2 characters with previews"
    vim.keymap.set("x", "ad", function()
      require("align").align_to_char({
        preview = true,
        length = 2,
      })
    end, NS)

    NS["desc"] = "Aligns to a word with previews"
    vim.keymap.set("x", "aw", function()
      require("align").align_to_string({
        preview = true,
        regex = false,
      })
    end, NS)

    NS["desc"] = "Aligns to a Vim regex with previews"
    vim.keymap.set("x", "ar", function()
      require("align").align_to_string({
        preview = true,
        regex = true,
      })
    end, NS)

    NS["desc"] = "align a paragraph to a word with previews"
    vim.keymap.set("n", "<leader>aw", function()
      local a = require("align")
      a.operator(a.align_to_string, {
        regex = false,
        preview = true,
      })
    end, NS)

    NS["desc"] = "align a paragraph to 1 character"
    vim.keymap.set("n", "<leader>ac", function()
      local a = require("align")
      a.operator(a.align_to_char)
    end, NS)
  end,
}

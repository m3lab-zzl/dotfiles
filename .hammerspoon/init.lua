require("mylua.clipboard")
require("mylua.launchAlacrittyHere")

-- quickly launch apps
-- option + shift + L: Logseq
hs.hotkey.bind({ "option", "shift" }, "L", function()
	hs.application.launchOrFocus("Logseq")
end)
-- option + shift + C: Code
hs.hotkey.bind({ "option", "shift" }, "C", function()
	hs.application.launchOrFocus("Code")
end)
-- option + shift + F: FireFox
hs.hotkey.bind({ "option", "shift" }, "F", function()
	hs.application.launchOrFocus("FireFox")
end)
-- option + shift + E: Finder
hs.hotkey.bind({ "option", "shift" }, "E", function()
	hs.application.launchOrFocus("Finder")
end)
-- option + shift + A: Alacritty
hs.hotkey.bind({ "option", "shift" }, "A", function()
	hs.application.launchOrFocus("alacritty")
end)

-- automatically reload config whenever init.lua changes
hs.loadSpoon("ReloadConfiguration")
spoon.ReloadConfiguration:start()

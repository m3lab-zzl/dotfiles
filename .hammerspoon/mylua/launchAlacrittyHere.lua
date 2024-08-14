-- 绑定 Option + Shift + I 快捷键
hs.hotkey.bind({ "alt", "shift" }, "I", function()
	-- 获取 Finder 当前打开的文件夹路径
	local success, finderPath = hs.osascript.applescript([[
        tell application "Finder"
            try
                set theFolder to (folder of the front window as alias)
                set thePath to POSIX path of theFolder
            on error
                set thePath to POSIX path of (path to desktop folder)
            end try
        end tell
        return thePath
    ]])

	-- 确保 finderPath 是字符串
	if success and finderPath then
		local alacrittyCmd =
			string.format("/Applications/Alacritty.app/Contents/MacOS/alacritty --working-directory '%s'", finderPath)
		hs.execute(alacrittyCmd)
	else
		hs.alert.show("无法获取 Finder 的当前路径")
	end
end)

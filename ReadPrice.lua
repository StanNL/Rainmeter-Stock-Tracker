function Initialize()

	sFileToRead = SELF:GetOption('FileToRead')
	
end

function sleep(n)
	if n > 0 then os.execute("ping -n " .. tonumber(n+1) .. " localhost > NUL") end
end

function Update()
	hReadingFile = io.open(sFileToRead)
	if not hReadingFile then
		print('LuaTextFile: unable to open file at ' .. sFileToRead)
		return
	end
	
	sAllText = hReadingFile:read("*all")
	
	sAllText = string.gsub(sAllText, "\t", "     ")
	
	io.close(hReadingFile)
	
	return tostring(sAllText)	
	
end

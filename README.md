# dbgwine
A helper to enable the many kinds of debug logging for wine runing windows applications.

I noticed that Ghidra now is including "gdb + wine" as a debug option. So if its good enough for the NSA, its good enough for me.
This morning I decided to see what I can do with wine from a reverse engineering standpoint. The logging of wine is fantastic but I 
dont hear about it much from fellow researchers.  So I made this wrapper that parsed the 639 debug channels avaiable and puts it in 
a list for you to choose to launch wine from it with those options or just a helpful list and you can copy it into your own frontend.

Why is this helpful? Unless you are using DEBUG_CHANNEL on a regular basis, no one is going to remeber which ones ara avaiable 
and the names it uses to enable that.

You can treat dbgwine as if it was wine, meaning using WINEPREFIX can be passed (or not, its fine) and a windows binary.


![output](https://github.com/user-attachments/assets/414ee356-f5b5-40e6-923d-3f8c1763c488)

**Requirments**
None 
Lean and Mean

**Install**
copy dbgwine and channels.txt to your path.

**Running**
Using a WINEPREFIX

`WINEPREFIX=/app/wine/dotnet4 dbgwine /app/wine/dotnet4/drive_c/windows/notepad.exe`

or
`WINEPREFIX=/app/wine/dotnet4 python dbgwine /app/wine/dotnet4/drive_c/windows/notepad.exe`

or 
`dbgwine ~/.wine/drive_c/windows/notepad.exe`

**Future?**
If I find it useful, I would like the menu to be in curses and have logging cleanup/options, better arg parsing


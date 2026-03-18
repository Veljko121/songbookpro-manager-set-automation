[Setup]
AppName=Set Creator
AppVersion=1.0
AppPublisher=Veljko121
DefaultDirName={userappdata}\SetCreator
DefaultGroupName=Set Creator
DisableProgramGroupPage=yes
OutputBaseFilename=set-creator-installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Files]
Source: "dist\set-creator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Set Creator"; Filename: "{app}\set-creator.exe"
Name: "{commondesktop}\Set Creator"; Filename: "{app}\set-creator.exe"

[Run]
Filename: "{app}\set-creator.exe"; Description: "Launch Set Creator"; Flags: nowait postinstall skipifsilent

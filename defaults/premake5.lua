workspace("Project")
architecture "x64"
configurations { "debug", "release", "dist" }
flags { "MultiProcessorCompile" }


OutputDir = "compiled-%{cfg.buildcfg}"
RuntimeDir = "runtime-%{cfg.buildcfg}"


filter "system:linux"
linkoptions { '-Wl,-rpath=\\$$ORIGIN' }
filter ""

project "App"
kind "ConsoleApp"
language "C++"
cppdialect "C++23"
targetdir "Binaries/%{cfg.buildcfg}"
staticruntime "off"

targetdir("%{wks.location}/Binaries/" .. OutputDir .. "/%{prj.name}")
objdir("%{wks.location}/Binaries/Intermediates/" .. OutputDir .. "/%{prj.name}")
debugdir("%{wks.location}/Binaries/" .. RuntimeDir .. "\\")
debugcommand("%{wks.location}/Binaries/" .. RuntimeDir .. "/%{prj.name}")
targetname("%{prj.name}")


postbuildcommands {"{MKDIR} %{wks.location}/Binaries/" .. RuntimeDir .. "/",
                  "{COPYFILE} %{cfg.buildtarget.relpath} %{wks.location}/Binaries/" .. RuntimeDir .. "/"}

files {"Source/**.h", "Source/**.cpp"}


filter "configurations:Debug"
defines {"DEBUG"}
runtime "Debug"
symbols "On"

filter "configurations:Release"
defines {"RELEASE"}
runtime "Release"
optimize "On"
symbols "On"

filter "configurations:Dist"
defines {"DIST"}
runtime "Release"
optimize "On"
symbols "Off"